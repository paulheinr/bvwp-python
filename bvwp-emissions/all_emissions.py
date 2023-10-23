from utils.soup_extraction import *
from utils.utils import string_to_float, float_to_string, get_output_file_path

from utils.write_files import write_to_csv, PROJECT_KEYS_STREET

BASE_URL = "https://www.bvwp-projekte.de/strasse/"


def analyze_all_emissions(file):
    logging.info("Scraping links of all projects.")
    links = get_links(BASE_URL)

    logging.info("Scraping values for projects.")
    values_of_project = get_values_of_projects(BASE_URL, links, Type.STREET)

    logging.info("Cleaning up values.")
    clean_up_values(values_of_project)

    logging.info("Adding new cost benefit ratios.")
    calc_and_add_new_cost_benefit(values_of_project)

    logging.info("Writing csv file.")
    write_to_csv_custom(values_of_project, file)


def clean_up_values(values_of_project):
    to_remove = []
    for project_id, project_values in values_of_project.items():
        if all(value is None for key, value in project_values.items() if key != 'project-name'):
            to_remove.append(project_id)
    for project_id in to_remove:
        if project_id in values_of_project:
            del values_of_project[project_id]


def calc_and_add_new_cost_benefit(values_of_project):
    for val in values_of_project.values():
        barwert_lifecycle_em = string_to_float(val['barwert_lifecycle_em'])
        barwert_co2 = string_to_float(val['barwert_co2'])
        barwert_nox = string_to_float(val['barwert_nox'])
        barwert_co = string_to_float(val['barwert_co'])
        barwert_hc = string_to_float(val['barwert_hc'])
        barwert_pm = string_to_float(val['barwert_pm'])
        barwert_so2 = string_to_float(val['barwert_so2'])
        kosten = string_to_float(val['kosten'])
        gesamtnutzen = string_to_float(val['gesamtnutzen'])

        val['nkv'] = float_to_string((gesamtnutzen / kosten))
        val['nkv_670'] = float_to_string((gesamtnutzen - (
                barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2) + (
                                                  670 / 145) * (
                                                  barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2)) / kosten)  # bei Fünfach werden 4 zusätzliche addiert
        val['nkv_1000'] = float_to_string((gesamtnutzen - (
                barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2) + (
                                                   1000 / 145) * (
                                                   barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2)) / kosten)
        val['nkv_1500'] = float_to_string((gesamtnutzen - (
                barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2) + (
                                                   1500 / 145) * (
                                                   barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2)) / kosten)
        val['nkv_2000'] = float_to_string((gesamtnutzen - (
                barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2) + (
                                                   2000 / 145) * (
                                                   barwert_lifecycle_em + barwert_co2 + barwert_nox + barwert_co + barwert_hc + barwert_pm + barwert_so2)) / kosten)


def write_to_csv_custom(values_of_project, file):
    anz_nkv_unter1_670 = 0
    anz_nkv_unter1_1000 = 0
    anz_nkv_unter1_1500 = 0
    anz_nkv_unter1_2000 = 0
    for v in values_of_project.values():
        if string_to_float(v['nkv_670']) < 1:
            anz_nkv_unter1_670 += 1

        if string_to_float(v['nkv_1000']) < 1:
            anz_nkv_unter1_1000 += 1

        if string_to_float(v['nkv_1500']) < 1:
            anz_nkv_unter1_1500 += 1

        if string_to_float(v['nkv_2000']) < 1:
            anz_nkv_unter1_2000 += 1

    extra_line = {'gesamtnutzen': 'Rausgefallene Projekte', 'nkv_670': anz_nkv_unter1_670,
                  'nkv_1000': anz_nkv_unter1_1000, 'nkv_1500': anz_nkv_unter1_1500, 'nkv_2000': anz_nkv_unter1_2000}

    write_to_csv(values_of_project, PROJECT_KEYS_STREET, file, extra_line=extra_line)


if __name__ == '__main__':
    file_path = get_output_file_path("all_emissions")
    analyze_all_emissions(file_path)
