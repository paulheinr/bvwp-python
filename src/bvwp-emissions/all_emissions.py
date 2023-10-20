import csv

from utils.soup_extraction import *
from utils.utils import string_to_float, float_to_string

BASE_URL = "https://www.bvwp-projekte.de/strasse/"


def analyze_all_emissions():
    logging.info("Scraping links of all projects.")
    links = get_links(BASE_URL)

    logging.info("Scraping values for projects.")
    values_of_project = get_values_of_projects(BASE_URL, links, True)

    logging.info("Cleaning up values.")
    clean_up_values(values_of_project)

    logging.info("Adding new cost benefit ratios.")
    calc_and_add_new_cost_benefit(values_of_project)

    logging.info("Writing csv file.")
    write_to_csv(values_of_project)


def clean_up_values(values_of_project):
    global project_values
    to_remove = []
    for project_id, project_values in values_of_project.items():
        if all(value is None for key, value in project_values.items() if key != 'project-name'):
            to_remove.append(project_id)
    for project_id in to_remove:
        if project_id in values_of_project:
            del values_of_project[project_id]


def calc_and_add_new_cost_benefit(values_of_project):
    global project_values
    for project_values in values_of_project.values():
        barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
        barwert_co2 = string_to_float(project_values['barwert_co2'])
        barwert_nox = string_to_float(project_values['barwert_nox'])
        barwert_co = string_to_float(project_values['barwert_co'])
        barwert_hc = string_to_float(project_values['barwert_hc'])
        barwert_pm = string_to_float(project_values['barwert_pm'])
        barwert_so2 = string_to_float(project_values['barwert_so2'])
        kosten = string_to_float(project_values['kosten'])
        gesamtnutzen = string_to_float(project_values['gesamtnutzen'])

        project_values['nkv'] = float_to_string((gesamtnutzen / kosten))
        project_values['nkv_670'] = float_to_string((gesamtnutzen - (
                barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2) + (
                                                             670 / 145) * (
                                                             barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2)) / kosten)  # bei Fünfach werden 4 zusätzliche addiert
        project_values['nkv_1000'] = float_to_string((gesamtnutzen - (
                barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2) + (
                                                              1000 / 145) * (
                                                              barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2)) / kosten)
        project_values['nkv_1500'] = float_to_string((gesamtnutzen - (
                barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2) + (
                                                              1500 / 145) * (
                                                              barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2)) / kosten)
        project_values['nkv_2000'] = float_to_string((gesamtnutzen - (
                barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2) + (
                                                              2000 / 145) * (
                                                              barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2)) / kosten)


def write_to_csv(values_of_project):
    anz_nkv_unter1_670 = 0
    anz_nkv_unter1_1000 = 0
    anz_nkv_unter1_1500 = 0
    anz_nkv_unter1_2000 = 0
    for project_values in values_of_project.values():
        if string_to_float(project_values['nkv_670']) < 1:
            anz_nkv_unter1_670 += 1

        if string_to_float(project_values['nkv_1000']) < 1:
            anz_nkv_unter1_1000 += 1

        if string_to_float(project_values['nkv_1500']) < 1:
            anz_nkv_unter1_1500 += 1

        if string_to_float(project_values['nkv_2000']) < 1:
            anz_nkv_unter1_2000 += 1
    # creating the excel-file
    header = ['project-name', 'lifec_em', 'lifecycle_em', 'barwert_lifecycle_em', 'nox_value', 'barwert_nox',
              'co_value',
              'barwert_co', 'co2_em', 'co2_value', 'barwert_co2', 'hc_value', 'barwert_hc', 'pm_value', 'barwert_pm',
              'so2_value', 'barwert_so2', 'gesamtnutzen', 'kosten', 'nkv', 'nkv_670', 'nkv_1000', 'nkv_1500',
              'nkv_2000']  # hier im Header hinzufügen
    with open("BVWP_alleEm.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=header)
        writer.writeheader()
        writer.writerows(list(values_of_project.values()))
        writer.writerow({})
        writer.writerow(
            {'gesamtnutzen': 'Rausgefallene Projekte', 'nkv_670': anz_nkv_unter1_670, 'nkv_1000': anz_nkv_unter1_1000,
             'nkv_1500': anz_nkv_unter1_1500, 'nkv_2000': anz_nkv_unter1_2000})
