from utils.soup_extraction import *
from utils.utils import string_to_float, float_to_string, get_output_file_path
from utils.write_files import write_to_csv, PROJECT_KEYS_STREET

BASE_URL = "https://www.bvwp-projekte.de/strasse/"


def analyze_co2(file):
    logging.info("Scraping links of all projects.")
    links = get_links(BASE_URL)

    logging.info("Scraping values for projects.")
    values_of_project = get_values_of_projects(BASE_URL, links, Type.STREET)

    logging.info("Cleaning up values.")
    n0, n1, n2, n3 = clean_up_values(values_of_project)

    logging.info("Adding new cost benefit ratios.")
    calc_and_add_new_cost_benefit(values_of_project, n0, n1, n2, n3)

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

    # CO2 saving scenarios

    # for saving 90 %
    sum_90_1 = sum(
        [string_to_float(project_values['barwert_co2']) for project_values in values_of_project.values()]) * 0.9
    sum_90_2 = sum(
        [string_to_float(project_values['barwert_lifecycle_em']) for project_values in
         values_of_project.values()]) * 0.9
    sum_co2_90 = sum_90_1 + sum_90_2

    n = 1

    while True:
        sum_co2_n = 0

        for project_values in values_of_project.values():
            barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
            barwert_co2 = string_to_float(project_values['barwert_co2'])
            kosten = string_to_float(project_values['kosten'])
            gesamtnutzen = string_to_float(project_values['gesamtnutzen'])

            faktor_n = ((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + ((n + 145) / 145) * (
                    barwert_lifecycle_em + barwert_co2)) / kosten)  # formula for calculating the necessary co2-price

            if faktor_n < 1:
                sum_co2_n += barwert_co2 + barwert_lifecycle_em

        if sum_co2_90 >= sum_co2_n:
            print(n)
            break
        n = n + 1

        # for saving 95 %
    sum_95_1 = sum(
        [string_to_float(project_values['barwert_co2']) for project_values in values_of_project.values()]) * 0.95
    sum_95_2 = sum(
        [string_to_float(project_values['barwert_lifecycle_em']) for project_values in
         values_of_project.values()]) * 0.95
    sum_co2_95 = sum_95_1 + sum_95_2

    n1 = 1

    while True:
        sum_co2_n1 = 0

        for project_values in values_of_project.values():
            barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
            barwert_co2 = string_to_float(project_values['barwert_co2'])
            kosten = string_to_float(project_values['kosten'])
            gesamtnutzen = string_to_float(project_values['gesamtnutzen'])

            faktor_n1 = ((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + ((n1 + 145) / 145) * (
                    barwert_lifecycle_em + barwert_co2)) / kosten)  # bei Fünfach werden 4 zusätzliche addiert

            if faktor_n1 < 1:
                sum_co2_n1 += barwert_co2 + barwert_lifecycle_em

        if sum_co2_95 >= sum_co2_n1:
            print(n1)
            break
        n1 = n1 + 1

        # for saving 97,5 %
    sum_975_1 = sum(
        [string_to_float(project_values['barwert_co2']) for project_values in values_of_project.values()]) * 0.975
    sum_975_2 = sum(
        [string_to_float(project_values['barwert_lifecycle_em']) for project_values in
         values_of_project.values()]) * 0.975
    sum_co2_975 = sum_975_1 + sum_975_2

    n2 = 1

    while True:
        sum_co2_n2 = 0

        for project_values in values_of_project.values():
            barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
            barwert_co2 = string_to_float(project_values['barwert_co2'])
            kosten = string_to_float(project_values['kosten'])
            gesamtnutzen = string_to_float(project_values['gesamtnutzen'])

            faktor_n2 = ((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + ((n2 + 145) / 145) * (
                    barwert_lifecycle_em + barwert_co2)) / kosten)

            if faktor_n2 < 1:
                sum_co2_n2 += barwert_co2 + barwert_lifecycle_em

        if sum_co2_975 >= sum_co2_n2:
            print(n2)
            break
        n2 = n2 + 1

        # for saving 99,5 %
    sum_995_1 = sum(
        [string_to_float(project_values['barwert_co2']) for project_values in values_of_project.values()]) * 0.995
    sum_995_2 = sum(
        [string_to_float(project_values['barwert_lifecycle_em']) for project_values in
         values_of_project.values()]) * 0.995
    sum_co2_995 = sum_995_1 + sum_995_2

    n3 = 1

    while True:
        sum_co2_n3 = 0

        for project_values in values_of_project.values():
            barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
            barwert_co2 = string_to_float(project_values['barwert_co2'])
            kosten = string_to_float(project_values['kosten'])
            gesamtnutzen = string_to_float(project_values['gesamtnutzen'])

            faktor_n3 = ((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + ((n3 + 145) / 145) * (
                    barwert_lifecycle_em + barwert_co2)) / kosten)

            if faktor_n3 < 1:
                sum_co2_n3 += barwert_co2 + barwert_lifecycle_em

        if sum_co2_995 >= sum_co2_n3:
            print(n3)
            break
        n3 = n3 + 1

    return (n, n1, n2, n3)

    # calculation of new cost-benefit ratios


def calc_and_add_new_cost_benefit(values_of_project, n0, n1, n2, n3):
    for project_values in values_of_project.values():
        barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
        barwert_co2 = string_to_float(project_values['barwert_co2'])
        kosten = string_to_float(project_values['kosten'])
        gesamtnutzen = string_to_float(project_values['gesamtnutzen'])

        project_values['nkv'] = float_to_string((gesamtnutzen / kosten))
        project_values['nkv_670'] = float_to_string(
            ((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (670 / 145) * (
                    barwert_lifecycle_em + barwert_co2)) / kosten))
        project_values['nkv_1000'] = float_to_string(
            ((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (1000 / 145) * (
                    barwert_lifecycle_em + barwert_co2)) / kosten))
        project_values['nkv_1500'] = float_to_string(
            ((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (1500 / 145) * (
                    barwert_lifecycle_em + barwert_co2)) / kosten))
        project_values['nkv_2000'] = float_to_string(
            ((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (2000 / 145) * (
                    barwert_lifecycle_em + barwert_co2)) / kosten))
        project_values['nkv_90'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (
                (n0 + 145) / 145) * (barwert_lifecycle_em + barwert_co2)) / kosten))
        project_values['nkv_95'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (
                (n1 + 145) / 145) * (barwert_lifecycle_em + barwert_co2)) / kosten))
        project_values['nkv_975'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (
                (n2 + 145) / 145) * (barwert_lifecycle_em + barwert_co2)) / kosten))
        project_values['nkv_995'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (
                (n3 + 145) / 145) * (barwert_lifecycle_em + barwert_co2)) / kosten))


# creating the excel-file
def write_to_csv_custom(values_of_project, file):
    anz_nkv_unter1_670 = 0
    anz_nkv_unter1_1000 = 0
    anz_nkv_unter1_1500 = 0
    anz_nkv_unter1_2000 = 0
    anz_nkv_unter1_90 = 0
    anz_nkv_unter1_95 = 0
    anz_nkv_unter1_975 = 0
    anz_nkv_unter1_995 = 0

    for project_values in values_of_project.values():
        if string_to_float(project_values['nkv_670']) < 1:
            anz_nkv_unter1_670 += 1

        if string_to_float(project_values['nkv_1000']) < 1:
            anz_nkv_unter1_1000 += 1

        if string_to_float(project_values['nkv_1500']) < 1:
            anz_nkv_unter1_1500 += 1

        if string_to_float(project_values['nkv_2000']) < 1:
            anz_nkv_unter1_2000 += 1

        if string_to_float(project_values['nkv_90']) < 1:
            anz_nkv_unter1_90 += 1

        if string_to_float(project_values['nkv_95']) < 1:
            anz_nkv_unter1_95 += 1

        if string_to_float(project_values['nkv_975']) < 1:
            anz_nkv_unter1_975 += 1

        if string_to_float(project_values['nkv_995']) < 1:
            anz_nkv_unter1_995 += 1

    extra_line = {'gesamtnutzen': 'Rausgefallene Projekte', 'nkv_670': anz_nkv_unter1_670,
                  'nkv_1000': anz_nkv_unter1_1000, 'nkv_1500': anz_nkv_unter1_1500, 'nkv_2000': anz_nkv_unter1_2000,
                  'nkv_90': anz_nkv_unter1_90, 'nkv_95': anz_nkv_unter1_95, 'nkv_975': anz_nkv_unter1_975,
                  'nkv_995': anz_nkv_unter1_995}
    write_to_csv(values_of_project, PROJECT_KEYS_STREET, file, extra_line=extra_line)


if __name__ == '__main__':
    file_path = get_output_file_path("co2")
    analyze_co2(file_path)
