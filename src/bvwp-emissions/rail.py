import csv
import logging
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup

from utils.utils import string_to_float, float_to_string


def get_links(url):
    # generating list of URLs
    req = Request(url)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []

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
    return links


def get_values_of_projects(links):
    values_of_project = dict()

    for link in links:
        get_values_of_project(link, values_of_project)

    # manual project-additions
    add_projects_manually(values_of_project)

    return values_of_project


def get_values_of_project(link, values_of_project):
    url = f'https://www.bvwp-projekte.de/schiene/{link}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    project_id = link.split('/')[0]

    logging.info(f"Project ID: {project_id}. Extracting values.")

    values_of_project[project_id] = get_initial_project_data(project_id)
    try:
        extract_values_of_project(project_id, values_of_project, soup)
    except IndexError:
        logging.warning(f"Project ID: {project_id}. Couldn't extract some value. Is a subproject.")
        values_of_project.pop(project_id)


def extract_values_of_project(project_id, values_of_project, soup):
    get_project_name(project_id, values_of_project, soup)
    get_project_priority(project_id, values_of_project, soup)
    get_project_co2(project_id, values_of_project, soup)
    get_project_nox(project_id, values_of_project, soup)
    get_project_co(project_id, values_of_project, soup)
    get_project_hc(project_id, values_of_project, soup)
    get_project_pm(project_id, values_of_project, soup)
    get_project_so2(project_id, values_of_project, soup)
    get_project_benefit(project_id, values_of_project, soup)
    get_project_costs(project_id, values_of_project, soup)


def handle_subproject(project_id, values_of_project):
    key = ""
    logging.warning(
        f"Project ID: {project_id}. Key not found: '{key}'. Project is Continue with next project")
    values_of_project.pop(project_id)


def get_initial_project_data(project_id):
    return {
        "project-name": project_id,
        "name": None,
        "gesamt_co2": None,
        "co2_em": None,
        "barwert_gesamt_co2": None,
        "nox_value": None,
        "barwert_nox": None,
        "co_value": None,
        "barwert_co": None,
        "hc_value": None,
        "barwert_hc": None,
        "pm_value": None,
        "barwert_pm": None,
        "so2_value": None,
        "barwert_so2": None,
        "gesamtnutzen": None,
        "kosten": None,
    }


def add_projects_manually(values_of_project):
    values_of_project["2-013-v01"] = {
        "project-name": "2-013-v01",
        "name": "ABS Burgsinn - Gemünden - Würzburg - Nürnberg",
        "Dringlichkeit": "VB-E",
        "co2_em": "-32703",
        "gesamt_co2": "4681",
        "barwert_gesamt_co2": "82,700",
        "nox_value": "102",
        "barwert_nox": "1800",
        "co_value": "2",
        "barwert_co": "0",
        "hc_value": "-35",
        "barwert_hc": "-0,6",
        "pm_value": "0",
        "barwert_pm": "0",
        "so2_value": "-62",
        "barwert_so2": "-1,1",
        "gesamtnutzen": "719,2",
        "kosten": "138,9",
    }
    values_of_project["2-014-v01"] = {
        "project-name": "2-014-v01",
        "name": "ABS Nürnberg - Passau",
        "Dringlichkeit": "VB",
        "co2_em": "-22254",
        "gesamt_co2": "3187",
        "barwert_gesamt_co2": "63,9",
        "nox_value": "301",
        "barwert_nox": "2",
        "co_value": "0",
        "barwert_co": "0",
        "hc_value": "-21",
        "barwert_hc": "-0,4",
        "pm_value": "19",
        "barwert_pm": "0,4",
        "so2_value": "-36",
        "barwert_so2": "-0,7",
        "gesamtnutzen": "516,6",
        "kosten": "350,6",
    }
    values_of_project["2-015-v01"] = {
        "project-name": "2-015-v01",
        "name": "ABS Paderborn - Halle (Kurve Mönchehof - Ihringshausen)",
        "Dringlichkeit": "VB-E",
        "co2_em": "-24627",
        "gesamt_co2": "3537",
        "barwert_gesamt_co2": "82,7",
        "nox_value": "245",
        "barwert_nox": "5,7",
        "co_value": "2",
        "barwert_co": "0",
        "hc_value": "-3",
        "barwert_hc": "-0,1",
        "pm_value": "21",
        "barwert_pm": "0,5",
        "so2_value": "-7",
        "barwert_so2": "-0,2",
        "gesamtnutzen": "806,4",
        "kosten": "51,8",
    }
    values_of_project["2-020-v01"] = {
        "project-name": "2-020-v01",
        "name": "Ausbau Köln - Düsseldorf - Dortmund",
        "Dringlichkeit": "VB-E",
        "co2_em": "-8582",
        "gesamt_co2": "1238",
        "barwert_gesamt_co2": "26,8",
        "nox_value": "650",
        "barwert_nox": "14,1",
        "co_value": "2",
        "barwert_co": "0",
        "hc_value": "-72",
        "barwert_hc": "-1,6",
        "pm_value": "25",
        "barwert_pm": "0,5",
        "so2_value": "-116",
        "barwert_so2": "-2,5",
        "gesamtnutzen": "2503",
        "kosten": "1401,7",
    }
    values_of_project["2-020-v02"] = {
        "project-name": "2-020-v02",
        "name": "Kompletierung des 6-Gleisigkeit zwischen Düsseldorf und Duisburg",
        "Dringlichkeit": "VB",
        "co2_em": "-6770",
        "gesamt_co2": "976",
        "barwert_gesamt_co2": "21,5",
        "nox_value": "333",
        "barwert_nox": "7,3",
        "co_value": "1",
        "barwert_co": "0",
        "hc_value": "-28",
        "barwert_hc": "-0,6",
        "pm_value": "33",
        "barwert_pm": "0,7",
        "so2_value": "-5",
        "barwert_so2": "-0,1",
        "gesamtnutzen": "1372,8",
        "kosten": "378,3",
    }
    values_of_project["2-020-v03"] = {
        "project-name": "2-020-v03",
        "name": "RRX-Halt Düsseldorf-Benrath",
        "Dringlichkeit": "VB",
        "co2_em": "-799",
        "gesamt_co2": "116",
        "barwert_gesamt_co2": "2,7",
        "nox_value": "16",
        "barwert_nox": "0,4",
        "co_value": "0",
        "barwert_co": "0",
        "hc_value": "0",
        "barwert_hc": "0",
        "pm_value": "2",
        "barwert_pm": "0",
        "so2_value": "0",
        "barwert_so2": "0",
        "gesamtnutzen": "166,2",
        "kosten": "112,6",
    }


def get_project_costs(project_id, values_of_project, soup):
    Tables = soup.findAll('table', attrs={'class': 'table_kosten'})
    for table in Tables:
        for row in table:
            if 'Summe bewertungsrelevante Investitionskosten' in row.text:
                kosten = row.contents[2].text
                values_of_project[project_id]["kosten"] = kosten


def get_project_benefit(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[10]
    for row in Table:
        if 'Summe Nutzen' in row.text:
            gesamtnutzen = row.contents[3].text
            values_of_project[project_id]["gesamtnutzen"] = gesamtnutzen


def get_project_so2(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Schwefeldioxid-Emissionen' in row.text:
            so2_value = row.contents[4].text
            values_of_project[project_id]["so2_value"] = so2_value
            barwert_so2 = row.contents[5].text
            values_of_project[project_id]["barwert_so2"] = barwert_so2


def get_project_pm(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Feinstaub-Emissionen' in row.text:
            pm_value = row.contents[4].text
            values_of_project[project_id]["pm_value"] = pm_value
            barwert_pm = row.contents[5].text
            values_of_project[project_id]["barwert_pm"] = barwert_pm


def get_project_hc(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Kohlenwasserstoff-Emissionen' in row.text:
            hc_value = row.contents[4].text
            values_of_project[project_id]["hc_value"] = hc_value
            barwert_hc = row.contents[5].text
            values_of_project[project_id]["barwert_hc"] = barwert_hc


def get_project_co(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Kohlenmonoxid-Emissionen' in row.text:
            co_value = row.contents[4].text
            values_of_project[project_id]["co_value"] = co_value
            barwert_co = row.contents[5].text
            values_of_project[project_id]["barwert_co"] = barwert_co


def get_project_nox(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Stickoxid-Emissionen' in row.text:
            nox_value = row.contents[4].text
            values_of_project[project_id]["nox_value"] = nox_value
            barwert_nox = row.contents[5].text
            values_of_project[project_id]["barwert_nox"] = barwert_nox


def get_project_co2(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Äquivalenten aus Lebenszyklusemissionen' in row.text:
            co2_em = row.contents[2].text
            values_of_project[project_id]["co2_em"] = co2_em
            gesamt_co2 = row.contents[4].text
            values_of_project[project_id]["gesamt_co2"] = gesamt_co2
            barwert_gesamt_co2 = row.contents[5].text
            values_of_project[project_id]["barwert_gesamt_co2"] = barwert_gesamt_co2


def get_project_priority(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_grunddaten'})[1]
    for row in Table:
        if 'Dringlichkeitseinstufung' in row.text:
            DE = row.contents[1].text
            values_of_project[project_id]["Dringlichkeit"] = DE


def get_project_name(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_grunddaten'})[0]
    for row in Table:
        if 'Maßnahmetitel' in row.text:
            name = row.contents[1].text
            values_of_project[project_id]["name"] = name


def write_to_csv(values_of_project):
    header = ['name', 'project-name', 'Dringlichkeit', 'co2_em', 'gesamt_co2', 'barwert_gesamt_co2', 'nox_value',
              'barwert_nox', 'co_value', 'barwert_co', 'hc_value', 'barwert_hc', 'pm_value', 'barwert_pm', 'so2_value',
              'barwert_so2', 'gesamtnutzen', 'kosten', 'nkv', 'nkv_670', 'nkv_1000', 'nkv_1500', 'nkv_2000']
    with open("BVWP-_Schiene.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=header)
        writer.writeheader()
        writer.writerows(list(values_of_project.values()))


def analyze_rail():
    logging.info("Scraping links of all projects.")
    links = get_links("https://www.bvwp-projekte.de/schiene/")

    logging.info("Beginning value extraction for project.")
    values_of_project = get_values_of_projects(links)

    # calculation of new benefit-cost ratios
    for project_values in values_of_project.values():
        kosten = string_to_float(project_values['kosten'])
        gesamtnutzen = string_to_float(project_values['gesamtnutzen'])
        barwert_gesamt_co2 = string_to_float(project_values['barwert_gesamt_co2'])
        barwert_nox = string_to_float(project_values['barwert_nox'])
        barwert_co = string_to_float(project_values['barwert_co'])
        barwert_hc = string_to_float(project_values['barwert_hc'])
        barwert_pm = string_to_float(project_values['barwert_pm'])
        barwert_so2 = string_to_float(project_values['barwert_so2'])

        project_values['nkv'] = float_to_string(gesamtnutzen / kosten)
        project_values['nkv_670'] = float_to_string(
            (gesamtnutzen - barwert_gesamt_co2 + (670 / 145) * (barwert_gesamt_co2)) / kosten)
        project_values['nkv_1000'] = float_to_string(
            (gesamtnutzen - barwert_gesamt_co2 + (1000 / 145) * (barwert_gesamt_co2)) / kosten)
        project_values['nkv_1500'] = float_to_string(
            (gesamtnutzen - barwert_gesamt_co2 + (1500 / 145) * (barwert_gesamt_co2)) / kosten)
        project_values['nkv_2000'] = float_to_string(
            (gesamtnutzen - barwert_gesamt_co2 + (2000 / 145) * (barwert_gesamt_co2)) / kosten)

    write_to_csv(values_of_project)

    # create_plots(values_of_project)


if __name__ == '__main__':
    analyze_rail()
