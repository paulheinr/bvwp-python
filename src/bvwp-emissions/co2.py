import csv
import logging
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup


def string_to_float(string):
    if string is not None:
        if string == '-':
            return 0.0
        value = string.replace('.', '')
        value = float(value.replace(',', '.'))
        return value
    return None


def float_to_string(float):  # string to float
    value = str(float).replace('.', ',')
    return value


# generating list of URLs
req = Request("https://www.bvwp-projekte.de/strasse/")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
last_scraped_gesamtnutzen = None

for link in soup.findAll('a'):
    links.append(link.get('href'))

links.remove('index.html')
links.remove('../glossar.html')
links.remove('../impressum.html')
links.remove('../datenschutz.html')
links.remove('../hinweise.html')

for link in links:

    if link.endswith('.pdf'):
        links.remove(link)

print(links)

values_of_project = dict()

for link in links:

    url = f'https://www.bvwp-projekte.de/strasse/{link}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    project_id = link.split('/')[0]
    # defining the needed variables
    values_of_project[project_id] = {
        "project-name": project_id,
        "lifecycle_em": None,
        "barwert_lifecycle_em": None,
        "nox_value": None,
        "barwert_nox": None,
        "co_value": None,
        "barwert_co": None,
        "co2_value": None,
        "barwert_co2": None,
        "hc_value": None,
        "barwert_hc": None,
        "pm_value": None,
        "barwert_pm": None,
        "so2_value": None,
        "barwert_so2": None,
        "gesamtnutzen": None,
        "kosten": None,
    }
    # lifecycle-emissions
    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[0]
        for row in Table:
            if 'Lebenszyklusemissionen' in row.text:
                lifecycle_em = row.contents[2].text
                values_of_project[project_id]["lifecycle_em"] = lifecycle_em
                barwert_lifecycle_em = row.contents[3].text
                values_of_project[project_id]["barwert_lifecycle_em"] = barwert_lifecycle_em
    except IndexError:
        logging.warning(
            f"lifecycle emissions not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    # CO2-emissions in total
    try:
        Tables = soup.findAll('table', attrs={'class': 'table_webprins'})[1]
        lifecycle_gesamt = False
        for row in Tables.find_all('tr'):
            if 'Kriterium' in row.text:
                lifecycle_gesamt = True
            if 'bestehend aus CO2 aus Betrieb und CO2-Äquivalenten aus Lebenszyklusemissionen' in row.text and lifecycle_gesamt:
                lifec_em = row.find_all('td')[2].text
                values_of_project[project_id]["lifec_em"] = lifec_em
    except IndexError:
        logging.warning(
            f"co value  not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"co value is {lifec_em}")

    # search nox value
    try:
        Tables = soup.findAll('table', attrs={'class': 'table_webprins'})
        for table in Tables:
            abgasbelastung = False
            for row in table:
                if 'Veränderung der Abgasbelastungen' in row.text:
                    abgasbelastung = True
                if 'Stickoxid-Emissionen' in row.text and abgasbelastung:
                    nox_value = row.contents[2].text
                    values_of_project[project_id]["nox_value"] = nox_value
                    barwert_nox = row.contents[3].text
                    values_of_project[project_id]["barwert_nox"] = barwert_nox
    except IndexError:
        logging.warning(
            f"nox value  not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"nox value is {nox_value}")

    # search for co value
    try:
        Tables = soup.findAll('table', attrs={'class': 'table_webprins'})
        for table in Tables:
            abgasbelastung = False
            for row in table:
                if 'Veränderung der Abgasbelastungen' in row.text:
                    abgasbelastung = True
                if 'Kohlenmonoxid-Emissionen' in row.text and abgasbelastung:
                    co_value = row.contents[2].text
                    values_of_project[project_id]["co_value"] = co_value
                    barwert_co = row.contents[3].text
                    values_of_project[project_id]["barwert_co"] = barwert_co
    except IndexError:
        logging.warning(
            f"co value  not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"co value is {co_value}")

    # search for co2 emissions
    try:
        Tables = soup.findAll('table', attrs={'class': 'table_wirkung_strasse'})
        for table in Tables:
            abgasemission = False
            for row in table:
                if 'Veränderung der Abgasemission' in row.text:
                    abgasemission = True
                if 'Kohlendioxid-Emissionen' in row.text and abgasemission:
                    co2_em = row.contents[3].text
                    values_of_project[project_id]["co2_em"] = co2_em
    except IndexError:
        logging.warning(
            f"co value  not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    # search for co2 value
    try:
        Tables = soup.findAll('table', attrs={'class': 'table_webprins'})
        for table in Tables:
            abgasbelastung = False
            for row in table:
                if 'Veränderung der Abgasbelastungen' in row.text:
                    abgasbelastung = True
                if 'Kohlendioxid-Emissionen' in row.text and abgasbelastung:
                    co2_value = row.contents[2].text
                    values_of_project[project_id]["co2_value"] = co2_value
                    barwert_co2 = row.contents[3].text
                    values_of_project[project_id]["barwert_co2"] = barwert_co2
    except IndexError:
        logging.warning(
            f"co value  not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    # search for hc value
    try:
        Tables = soup.findAll('table', attrs={'class': 'table_webprins'})
        for table in Tables:
            abgasbelastung = False
            for row in table:
                if 'Veränderung der Abgasbelastungen' in row.text:
                    abgasbelastung = True
                if 'Kohlenwasserstoff-Emissionen' in row.text and abgasbelastung:
                    hc_value = row.contents[2].text
                    values_of_project[project_id]["hc_value"] = hc_value
                    barwert_hc = row.contents[3].text
                    values_of_project[project_id]["barwert_hc"] = barwert_hc

    except IndexError:
        logging.warning(
            f"hc value not found for project {project_id}. So project is subproject. Continue with next project")

        if project_id in values_of_project:
            del values_of_project[project_id]
        continue

    if not barwert_hc or barwert_hc.strip() == '-':
        logging.warning(f"barwert_hc entire project from the dictionary")
        if project_id in values_of_project:
            del values_of_project[project_id]
        continue

    # search for pm value
    try:
        Tables = soup.findAll('table', attrs={'class': 'table_webprins'})
        for table in Tables:
            abgasbelastung = False
            for row in table:
                if 'Veränderung der Abgasbelastungen' in row.text:
                    abgasbelastung = True
                if 'Feinstaub-Emissionen' in row.text and abgasbelastung:
                    pm_value = row.contents[2].text
                    values_of_project[project_id]["pm_value"] = pm_value
                    barwert_pm = row.contents[3].text
                    values_of_project[project_id]["barwert_pm"] = barwert_pm
    except IndexError:
        logging.warning(
            f"pm emission not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)

        continue

    print(f"pm emissions is {pm_value}")

    # search so2 value
    try:
        Tables = soup.findAll('table', attrs={'class': 'table_webprins'})
        for table in Tables:
            abgasbelastung = False
            for row in table:
                if 'Veränderung der Abgasbelastungen' in row.text:
                    abgasbelastung = True
                if 'Schwefeldioxid-Emissionen' in row.text and abgasbelastung:
                    so2_value = row.contents[2].text
                    values_of_project[project_id]["so2_value"] = so2_value
                    barwert_so2 = row.contents[3].text
                    values_of_project[project_id]["barwert_so2"] = barwert_so2
    except IndexError:
        logging.warning(
            f"co value  not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"so2 emissions is {so2_value}")

    # cost in total

    try:
        Tables = soup.findAll('table', attrs={'class': 'table_kosten'})
        for table in Tables:
            for row in table:
                if 'Summe bewertungsrelevanter Investitionskosten' in row.text:
                    kosten = row.contents[2].text
                    values_of_project[project_id]["kosten"] = kosten
    except IndexError:
        logging.warning(
            f"Kosten not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"Für {project_id} Kosten entspricht {kosten}")

    # benefit in total

    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[0]
        for row in Table:
            if 'Gesamtnutzen' in row.text:
                gesamtnutzen = row.contents[3].text

                if gesamtnutzen == last_scraped_gesamtnutzen:
                    print(f"Gesamtnutzen {gesamtnutzen} bereits gescraped. Überspringe Website.")

                    if project_id in values_of_project:
                        del values_of_project[project_id]
                    continue
                last_scraped_gesamtnutzen = gesamtnutzen
                values_of_project[project_id]["gesamtnutzen"] = gesamtnutzen

    except IndexError:
        logging.warning(
            f"gesamtnutzen not found for project {project_id}. So project is subproject. Continue with next project")
        if project_id in values_of_project:
            del values_of_project[project_id]
        continue

    print(gesamtnutzen)

to_remove = []
for project_id, project_values in values_of_project.items():
    if all(value is None for key, value in project_values.items() if key != 'project-name'):
        to_remove.append(project_id)

for project_id in to_remove:
    if project_id in values_of_project:
        del values_of_project[project_id]

# CO2 saving scenarios

# for saving 90 %
sum_90_1 = sum([string_to_float(project_values['barwert_co2']) for project_values in values_of_project.values()]) * 0.9
sum_90_2 = sum(
    [string_to_float(project_values['barwert_lifecycle_em']) for project_values in values_of_project.values()]) * 0.9
sum_co2_90 = sum_90_1 + sum_90_2

n = 1

while True:
    sum_co2_n = 0

    for project_values in values_of_project.values():
        barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
        co2_value = string_to_float(project_values['co2_value'])
        barwert_co2 = string_to_float(project_values['barwert_co2'])
        barwert_nox = string_to_float(project_values['barwert_nox'])
        barwert_co = string_to_float(project_values['barwert_co'])
        barwert_hc = string_to_float(project_values['barwert_hc'])
        barwert_pm = string_to_float(project_values['barwert_pm'])
        barwert_so2 = string_to_float(project_values['barwert_so2'])
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
sum_95_1 = sum([string_to_float(project_values['barwert_co2']) for project_values in values_of_project.values()]) * 0.95
sum_95_2 = sum(
    [string_to_float(project_values['barwert_lifecycle_em']) for project_values in values_of_project.values()]) * 0.95
sum_co2_95 = sum_95_1 + sum_95_2

n1 = 1

while True:
    sum_co2_n1 = 0

    for project_values in values_of_project.values():
        barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
        co2_value = string_to_float(project_values['co2_value'])
        barwert_co2 = string_to_float(project_values['barwert_co2'])
        barwert_nox = string_to_float(project_values['barwert_nox'])
        barwert_co = string_to_float(project_values['barwert_co'])
        barwert_hc = string_to_float(project_values['barwert_hc'])
        barwert_pm = string_to_float(project_values['barwert_pm'])
        barwert_so2 = string_to_float(project_values['barwert_so2'])
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
    [string_to_float(project_values['barwert_lifecycle_em']) for project_values in values_of_project.values()]) * 0.975
sum_co2_975 = sum_975_1 + sum_975_2

n2 = 1

while True:
    sum_co2_n2 = 0

    for project_values in values_of_project.values():
        barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
        co2_value = string_to_float(project_values['co2_value'])
        barwert_co2 = string_to_float(project_values['barwert_co2'])
        barwert_nox = string_to_float(project_values['barwert_nox'])
        barwert_co = string_to_float(project_values['barwert_co'])
        barwert_hc = string_to_float(project_values['barwert_hc'])
        barwert_pm = string_to_float(project_values['barwert_pm'])
        barwert_so2 = string_to_float(project_values['barwert_so2'])
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
    [string_to_float(project_values['barwert_lifecycle_em']) for project_values in values_of_project.values()]) * 0.995
sum_co2_995 = sum_995_1 + sum_995_2

n3 = 1

while True:
    sum_co2_n3 = 0

    for project_values in values_of_project.values():
        barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
        co2_value = string_to_float(project_values['co2_value'])
        barwert_co2 = string_to_float(project_values['barwert_co2'])
        barwert_nox = string_to_float(project_values['barwert_nox'])
        barwert_co = string_to_float(project_values['barwert_co'])
        barwert_hc = string_to_float(project_values['barwert_hc'])
        barwert_pm = string_to_float(project_values['barwert_pm'])
        barwert_so2 = string_to_float(project_values['barwert_so2'])
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

# calculation of new cost-benefit ratios

for project_values in values_of_project.values():
    lifecycle_em = string_to_float(project_values['lifecycle_em'])
    barwert_lifecycle_em = string_to_float(project_values['barwert_lifecycle_em'])
    co2_value = string_to_float(project_values['co2_value'])
    barwert_co2 = string_to_float(project_values['barwert_co2'])
    nox_value = string_to_float(project_values['nox_value'])
    barwert_nox = string_to_float(project_values['barwert_nox'])
    co_value = string_to_float(project_values['co_value'])
    barwert_co = string_to_float(project_values['barwert_co'])
    hc_value = string_to_float(project_values['hc_value'])
    barwert_hc = string_to_float(project_values['barwert_hc'])
    pm_value = string_to_float(project_values['pm_value'])
    barwert_pm = string_to_float(project_values['barwert_pm'])
    so2_value = string_to_float(project_values['so2_value'])
    barwert_so2 = string_to_float(project_values['barwert_so2'])
    kosten = string_to_float(project_values['kosten'])
    gesamtnutzen = string_to_float(project_values['gesamtnutzen'])

    project_values['nkv'] = float_to_string((gesamtnutzen / kosten))
    project_values['nkv_670'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (670 / 145) * (
                barwert_lifecycle_em + barwert_co2)) / kosten))
    project_values['nkv_1000'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (1000 / 145) * (
                barwert_lifecycle_em + barwert_co2)) / kosten))
    project_values['nkv_1500'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (1500 / 145) * (
                barwert_lifecycle_em + barwert_co2)) / kosten))
    project_values['nkv_2000'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (2000 / 145) * (
                barwert_lifecycle_em + barwert_co2)) / kosten))
    project_values['nkv_90'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (
                (n + 145) / 145) * (barwert_lifecycle_em + barwert_co2)) / kosten))
    project_values['nkv_95'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (
                (n1 + 145) / 145) * (barwert_lifecycle_em + barwert_co2)) / kosten))
    project_values['nkv_975'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (
                (n2 + 145) / 145) * (barwert_lifecycle_em + barwert_co2)) / kosten))
    project_values['nkv_995'] = float_to_string(((gesamtnutzen - barwert_lifecycle_em - barwert_co2 + (
                (n3 + 145) / 145) * (barwert_lifecycle_em + barwert_co2)) / kosten))

# number of cancelled projects

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

# creating the excel-file

header = ['project-name', 'lifec_em', 'lifecycle_em', 'barwert_lifecycle_em', 'nox_value', 'barwert_nox', 'co_value',
          'barwert_co', 'co2_em', 'co2_value', 'barwert_co2', 'hc_value', 'barwert_hc', 'pm_value', 'barwert_pm',
          'so2_value', 'barwert_so2', 'gesamtnutzen', 'kosten', 'nkv', 'nkv_670', 'nkv_1000', 'nkv_1500', 'nkv_2000',
          'nkv_90', 'nkv_95', 'nkv_975', 'nkv_995']  # hier im Header hinzufügen

with open("BVWP_CO2.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=header)
    writer.writeheader()
    writer.writerows(list(values_of_project.values()))
    writer.writerow({})
    writer.writerow(
        {'gesamtnutzen': 'Rausgefallene Projekte', 'nkv_670': anz_nkv_unter1_670, 'nkv_1000': anz_nkv_unter1_1000,
         'nkv_1500': anz_nkv_unter1_1500, 'nkv_2000': anz_nkv_unter1_2000, 'nkv_90': anz_nkv_unter1_90,
         'nkv_95': anz_nkv_unter1_95, 'nkv_975': anz_nkv_unter1_975, 'nkv_995': anz_nkv_unter1_995})
