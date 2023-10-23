import csv

PROJECT_KEYS_STREET = ['project-name', 'lifec_em', 'lifecycle_em', 'barwert_lifecycle_em', 'nox_value', 'barwert_nox',
                       'co_value', 'barwert_co', 'co2_em', 'co2_value', 'barwert_co2', 'hc_value', 'barwert_hc',
                       'pm_value', 'barwert_pm', 'so2_value', 'barwert_so2', 'gesamtnutzen', 'kosten', 'nkv', 'nkv_670',
                       'nkv_1000', 'nkv_1500', 'nkv_2000', 'nkv_90', 'nkv_95', 'nkv_975', 'nkv_995']

PROJECT_KEYS_RAIL = ['name', 'project-name', 'Dringlichkeit', 'co2_em', 'gesamt_co2', 'barwert_gesamt_co2', 'nox_value',
                     'barwert_nox', 'co_value', 'barwert_co', 'hc_value', 'barwert_hc', 'pm_value', 'barwert_pm',
                     'so2_value', 'barwert_so2', 'gesamtnutzen', 'kosten', 'nkv', 'nkv_670', 'nkv_1000', 'nkv_1500',
                     'nkv_2000']


def write_to_csv(values_of_project, header, file_name, extra_line=None):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=header)
        writer.writeheader()
        writer.writerows(list(values_of_project.values()))

        if extra_line:
            writer.writerow({})
            writer.writerow(extra_line)
