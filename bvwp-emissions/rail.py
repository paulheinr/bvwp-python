import pathlib
import sys

from utils.soup_extraction import *
from utils.utils import string_to_float, float_to_string
from utils.write_files import write_to_csv

BASE_URL = "https://www.bvwp-projekte.de/schiene/"


def analyze_rail(output_file):
    logging.info("Scraping links of all projects.")
    links = get_links(BASE_URL)

    logging.info("Scraping values for projects.")
    values_of_project = get_values_of_projects(BASE_URL, links, Type.RAIL)

    add_projects_manually(values_of_project)

    # calculation of new benefit-cost ratios
    logging.info("Adding new cost benefit ratios.")
    calc_and_add_new_cost_benefit(values_of_project)

    logging.info("Writing csv file.")
    write_to_csv(values_of_project, PROJECT_KEYS_RAIL, output_file)


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


def calc_and_add_new_cost_benefit(values_of_project):
    for project_values in values_of_project.values():
        kosten = string_to_float(project_values['kosten'])
        gesamtnutzen = string_to_float(project_values['gesamtnutzen'])
        barwert_gesamt_co2 = string_to_float(project_values['barwert_gesamt_co2'])

        project_values['nkv'] = float_to_string(gesamtnutzen / kosten)
        project_values['nkv_670'] = float_to_string(
            (gesamtnutzen - barwert_gesamt_co2 + (670 / 145) * (barwert_gesamt_co2)) / kosten)
        project_values['nkv_1000'] = float_to_string(
            (gesamtnutzen - barwert_gesamt_co2 + (1000 / 145) * (barwert_gesamt_co2)) / kosten)
        project_values['nkv_1500'] = float_to_string(
            (gesamtnutzen - barwert_gesamt_co2 + (1500 / 145) * (barwert_gesamt_co2)) / kosten)
        project_values['nkv_2000'] = float_to_string(
            (gesamtnutzen - barwert_gesamt_co2 + (2000 / 145) * (barwert_gesamt_co2)) / kosten)


if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        logging.info(f"Called rail analysis with argument: {file_path}")
    else:
        file_path = "./output/rail.csv"
        logging.info(f"Called rail analysis without argument. Writing to default file: {file_path}")

    pathlib.Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    analyze_rail(file_path)
