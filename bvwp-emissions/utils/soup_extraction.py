import logging
from enum import Enum
from urllib.request import urlopen, Request

import requests
from bs4 import BeautifulSoup

PROJECT_KEYS_STREET = ['project-name', 'lifec_em', 'lifecycle_em', 'barwert_lifecycle_em', 'nox_value', 'barwert_nox',
                       'co_value', 'barwert_co', 'co2_em', 'co2_value', 'barwert_co2', 'hc_value', 'barwert_hc',
                       'pm_value', 'barwert_pm', 'so2_value', 'barwert_so2', 'gesamtnutzen', 'kosten', 'nkv', 'nkv_670',
                       'nkv_1000', 'nkv_1500', 'nkv_2000', 'nkv_90', 'nkv_95', 'nkv_975', 'nkv_995']

PROJECT_KEYS_RAIL = ['name', 'project-name', 'Dringlichkeit', 'co2_em', 'gesamt_co2', 'barwert_gesamt_co2', 'nox_value',
                     'barwert_nox', 'co_value', 'barwert_co', 'hc_value', 'barwert_hc', 'pm_value', 'barwert_pm',
                     'so2_value', 'barwert_so2', 'gesamtnutzen', 'kosten', 'nkv', 'nkv_670', 'nkv_1000', 'nkv_1500',
                     'nkv_2000']


class Type(Enum):
    RAIL = 0
    STREET = 1


def fill_project_costs(project_id, values_of_project, soup):
    Tables = soup.findAll('table', attrs={'class': 'table_kosten'})
    for table in Tables:
        for row in table:
            if 'Summe bewertungsrelevante Investitionskosten' in row.text:
                kosten = row.contents[2].text
                values_of_project[project_id]["kosten"] = kosten


def fill_rail_project_benefit(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[10]
    for row in Table:
        if 'Summe Nutzen' in row.text:
            gesamtnutzen = row.contents[3].text
            values_of_project[project_id]["gesamtnutzen"] = gesamtnutzen


def fill_street_project_benefit(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[0]
    for row in Table:
        if 'Gesamtnutzen' in row.text:
            gesamtnutzen = row.contents[3].text

            # TODO
            if gesamtnutzen == last_scraped_gesamtnutzen:
                print(f"Gesamtnutzen {gesamtnutzen} bereits gescraped. Überspringe Website.")

                if project_id in values_of_project:
                    del values_of_project[project_id]
                continue
            last_scraped_gesamtnutzen = gesamtnutzen
            values_of_project[project_id]["gesamtnutzen"] = gesamtnutzen


def fill_rail_project_so2(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Schwefeldioxid-Emissionen' in row.text:
            so2_value = row.contents[4].text
            values_of_project[project_id]["so2_value"] = so2_value
            barwert_so2 = row.contents[5].text
            values_of_project[project_id]["barwert_so2"] = barwert_so2


def fill_street_project_so2(project_id, values_of_project, soup):
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


def fill_rail_project_pm(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Feinstaub-Emissionen' in row.text:
            pm_value = row.contents[4].text
            values_of_project[project_id]["pm_value"] = pm_value
            barwert_pm = row.contents[5].text
            values_of_project[project_id]["barwert_pm"] = barwert_pm


def fill_street_project_pm(project_id, values_of_project, soup):
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


def fill_rail_project_hc(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Kohlenwasserstoff-Emissionen' in row.text:
            hc_value = row.contents[4].text
            values_of_project[project_id]["hc_value"] = hc_value
            barwert_hc = row.contents[5].text
            values_of_project[project_id]["barwert_hc"] = barwert_hc


def fill_street_project_hc(project_id, values_of_project, soup):
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

    if not barwert_hc or barwert_hc.strip() == '-':
        logging.warning(f"barwert_hc entire project from the dictionary")
        if project_id in values_of_project:
            del values_of_project[project_id]


def fill_rail_project_co(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Kohlenmonoxid-Emissionen' in row.text:
            co_value = row.contents[4].text
            values_of_project[project_id]["co_value"] = co_value
            barwert_co = row.contents[5].text
            values_of_project[project_id]["barwert_co"] = barwert_co


def fill_street_project_co(project_id, values_of_project, soup):
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


def fill_rail_project_nox(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Stickoxid-Emissionen' in row.text:
            nox_value = row.contents[4].text
            values_of_project[project_id]["nox_value"] = nox_value
            barwert_nox = row.contents[5].text
            values_of_project[project_id]["barwert_nox"] = barwert_nox


def fill_street_project_nox(project_id, values_of_project, soup):
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


def fill_rail_project_co2(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
    for row in Table:
        if 'Äquivalenten aus Lebenszyklusemissionen' in row.text:
            co2_em = row.contents[2].text
            values_of_project[project_id]["co2_em"] = co2_em
            gesamt_co2 = row.contents[4].text
            values_of_project[project_id]["gesamt_co2"] = gesamt_co2
            barwert_gesamt_co2 = row.contents[5].text
            values_of_project[project_id]["barwert_gesamt_co2"] = barwert_gesamt_co2


def fill_street_project_co2(project_id, values_of_project, soup):
    Tables = soup.findAll('table', attrs={'class': 'table_wirkung_strasse'})
    for table in Tables:
        abgasemission = False
        for row in table:
            if 'Veränderung der Abgasemission' in row.text:
                abgasemission = True
            if 'Kohlendioxid-Emissionen' in row.text and abgasemission:
                co2_em = row.contents[3].text
                values_of_project[project_id]["co2_em"] = co2_em

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


def fill_rail_project_priority(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_grunddaten'})[1]
    for row in Table:
        if 'Dringlichkeitseinstufung' in row.text:
            DE = row.contents[1].text
            values_of_project[project_id]["Dringlichkeit"] = DE


def fill_rail_project_name(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_grunddaten'})[0]
    for row in Table:
        if 'Maßnahmetitel' in row.text:
            name = row.contents[1].text
            values_of_project[project_id]["name"] = name


def fill_lifecycle_em(project_id, values_of_project, soup):
    Table = soup.findAll('table', attrs={'class': 'table_webprins'})[0]
    for row in Table:
        if 'Lebenszyklusemissionen' in row.text:
            lifecycle_em = row.contents[2].text
            values_of_project[project_id]["lifecycle_em"] = lifecycle_em
            barwert_lifecycle_em = row.contents[3].text
            values_of_project[project_id]["barwert_lifecycle_em"] = barwert_lifecycle_em


def fill_lifec_em(project_id, values_of_project, soup):
    Tables = soup.findAll('table', attrs={'class': 'table_webprins'})[1]
    lifecycle_gesamt = False
    for row in Tables.find_all('tr'):
        if 'Kriterium' in row.text:
            lifecycle_gesamt = True
        if 'bestehend aus CO2 aus Betrieb und CO2-Äquivalenten aus Lebenszyklusemissionen' in row.text and lifecycle_gesamt:
            lifec_em = row.find_all('td')[2].text
            values_of_project[project_id]["lifec_em"] = lifec_em


def extract_and_fill_values_of_rail_project(project_id, values_of_project, soup):
    fill_rail_project_name(project_id, values_of_project, soup)
    fill_rail_project_priority(project_id, values_of_project, soup)
    fill_rail_project_co2(project_id, values_of_project, soup)
    fill_rail_project_nox(project_id, values_of_project, soup)
    fill_rail_project_co(project_id, values_of_project, soup)
    fill_rail_project_hc(project_id, values_of_project, soup)
    fill_rail_project_pm(project_id, values_of_project, soup)
    fill_rail_project_so2(project_id, values_of_project, soup)
    fill_rail_project_benefit(project_id, values_of_project, soup)
    fill_project_costs(project_id, values_of_project, soup)


def extract_and_fill_values_of_street_project(project_id, values_of_project, soup):
    fill_lifecycle_em(project_id, values_of_project, soup)
    fill_lifec_em(project_id, values_of_project, soup)
    fill_street_project_nox(project_id, values_of_project, soup)
    fill_street_project_co(project_id, values_of_project, soup)
    fill_street_project_co2(project_id, values_of_project, soup)
    fill_street_project_hc(project_id, values_of_project, soup)
    fill_street_project_pm(project_id, values_of_project, soup)
    fill_street_project_so2(project_id, values_of_project, soup)
    fill_project_costs(project_id, values_of_project, soup)


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


def get_values_of_projects(base_url, links, project_type):
    values_of_project = dict()

    for link in links:
        get_values_of_project(base_url, link, values_of_project, project_type)

    return values_of_project


def get_values_of_project(base_url, link, values_of_project, project_type):
    url = f'{base_url}{link}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    project_id = link.split('/')[0]

    logging.info(f"Project ID: {project_id}. Extracting values.")
    values_of_project[project_id] = {}
    values_of_project[project_id]["project-name"] = project_id

    try:
        if project_type == Type.RAIL:
            extract_and_fill_values_of_rail_project(project_id, values_of_project, soup)
        else:
            extract_and_fill_values_of_street_project(project_id, values_of_project, soup)

    except IndexError:
        logging.warning(f"Project ID: {project_id}. Couldn't extract some value. Is a subproject.")
        values_of_project.pop(project_id)
