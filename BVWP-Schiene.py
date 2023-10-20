import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import logging
import csv
import matplotlib.pyplot as plt
import numpy as np

def string_to_float(string):
    if string is not None:
        if string == '-':
            return 0.0
        value = string.replace('.', '')
        value = float(value.replace(',', '.'))
        return value
    return None

def float_to_string(float):      #string to float
    value = str(float).replace('.',',')
    return value

# generating list of URLs
req = Request("https://www.bvwp-projekte.de/schiene/")
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

print(links)

values_of_project = dict()


for link in links:

    url = f'https://www.bvwp-projekte.de/schiene/{link}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    project_id = link.split('/')[0]
# definition of needed variables
    values_of_project[project_id] = {
        "project-name": project_id,
        "name": None,
        "gesamt_co2": None,
        "co2_em" : None,
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

    #project-name

    try:
        Table = soup.findAll('table', attrs={'class': 'table_grunddaten'})[0]
        for row in Table:
            if 'Maßnahmetitel' in row.text:
                name = row.contents[1].text
                values_of_project[project_id]["name"] = name

    except IndexError:
        logging.warning(
                f"Name not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    #priority-level

    try:
        Table = soup.findAll('table', attrs={'class': 'table_grunddaten'})[1]
        for row in Table:
            if 'Dringlichkeitseinstufung' in row.text:
                DE = row.contents[1].text
                values_of_project[project_id]["Dringlichkeit"] = DE

    except IndexError:
        logging.warning(
                f"Name not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue


    # CO2-emissions
    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
        for row in Table:
            if 'Äquivalenten aus Lebenszyklusemissionen' in row.text:
                co2_em = row.contents[2].text
                values_of_project[project_id]["co2_em"] = co2_em
                gesamt_co2 = row.contents[4].text
                values_of_project[project_id]["gesamt_co2"] = gesamt_co2
                barwert_gesamt_co2 = row.contents[5].text
                values_of_project[project_id]["barwert_gesamt_co2"] = barwert_gesamt_co2
    except IndexError:
        logging.warning(f"Gesamt CO2 not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"Gesamt CO2  is {gesamt_co2}")
    print(f"barwert von CO2 is {barwert_gesamt_co2}")

    #nox-value

    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
        for row in Table:
            if 'Stickoxid-Emissionen' in row.text:
                nox_value = row.contents[4].text
                values_of_project[project_id]["nox_value"] = nox_value
                barwert_nox = row.contents[5].text
                values_of_project[project_id]["barwert_nox"] = barwert_nox
    except IndexError:
        logging.warning(f"Gesamt Nox not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"Stickoxid  is {nox_value}")
    print(f"barwert von Stickoxid is {barwert_nox}")

    #co-value

    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
        for row in Table:
            if 'Kohlenmonoxid-Emissionen' in row.text:
                co_value = row.contents[4].text
                values_of_project[project_id]["co_value"] = co_value
                barwert_co = row.contents[5].text
                values_of_project[project_id]["barwert_co"] = barwert_co
    except IndexError:
        logging.warning(f"Gesamt Co not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"Stickoxid  is {co_value}")
    print(f"barwert von Stickoxid is {barwert_co}")

    #hc-value

    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
        for row in Table:
            if 'Kohlenwasserstoff-Emissionen' in row.text:
                hc_value = row.contents[4].text
                values_of_project[project_id]["hc_value"] = hc_value
                barwert_hc = row.contents[5].text
                values_of_project[project_id]["barwert_hc"] = barwert_hc
    except IndexError:
        logging.warning(f"Gesamt HC not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"Stickoxid  is {hc_value}")
    print(f"barwert von Stickoxid is {barwert_hc}")

    #pm-value

    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
        for row in Table:
            if 'Feinstaub-Emissionen' in row.text:
                pm_value = row.contents[4].text
                values_of_project[project_id]["pm_value"] = pm_value
                barwert_pm = row.contents[5].text
                values_of_project[project_id]["barwert_pm"] = barwert_pm
    except IndexError:
        logging.warning(f"Gesamt PM not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"Stickoxid  is {pm_value}")
    print(f"barwert von Stickoxid is {barwert_pm}")

    #so2-value

    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[12]
        for row in Table:
            if 'Schwefeldioxid-Emissionen' in row.text:
                so2_value = row.contents[4].text
                values_of_project[project_id]["so2_value"] = so2_value
                barwert_so2 = row.contents[5].text
                values_of_project[project_id]["barwert_so2"] = barwert_so2
    except IndexError:
        logging.warning(f"Gesamt Co not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"Stickoxid  is {so2_value}")
    print(f"barwert von Stickoxid is {barwert_so2}")

    #benefit in total

    try:
        Table = soup.findAll('table', attrs={'class': 'table_webprins'})[10]
        for row in Table:
            if 'Summe Nutzen' in row.text:
                gesamtnutzen = row.contents[3].text
                values_of_project[project_id]["gesamtnutzen"] = gesamtnutzen
    except IndexError:
        logging.warning(
            f"gesamtnutzen not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(gesamtnutzen)

    # cost in total

    try:

        Tables = soup.findAll('table', attrs={'class': 'table_kosten'})
        for table in Tables:
            for row in table:
                if 'Summe bewertungsrelevante Investitionskosten' in row.text:
                    kosten = row.contents[2].text
                    values_of_project[project_id]["kosten"] = kosten
    except IndexError:
        logging.warning(
            f"Kosten not found for project {project_id}. So project is subproject. Continue with next project")
        values_of_project.pop(project_id)
        continue

    print(f"Für {project_id} Kosten entspricht {kosten}")

# manual project-additions

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
#calculation of new benefit-cost ratios
for project_values in values_of_project.values():
    kosten = string_to_float(project_values['kosten'])
    gesamtnutzen = string_to_float(project_values['gesamtnutzen'])
    barwert_gesamt_co2 = string_to_float(project_values['barwert_gesamt_co2'])
    barwert_nox = string_to_float(project_values['barwert_nox'])
    barwert_co = string_to_float(project_values['barwert_co'])
    barwert_hc = string_to_float(project_values['barwert_hc'])
    barwert_pm = string_to_float(project_values['barwert_pm'])
    barwert_so2 = string_to_float(project_values['barwert_so2'])

    project_values['nkv'] = float_to_string(gesamtnutzen/kosten)
    project_values['nkv_670'] = float_to_string((gesamtnutzen-barwert_gesamt_co2+(670/145)*(barwert_gesamt_co2))/kosten)
    project_values['nkv_1000'] = float_to_string((gesamtnutzen-barwert_gesamt_co2+(1000/145)*(barwert_gesamt_co2))/kosten)
    project_values['nkv_1500'] = float_to_string((gesamtnutzen-barwert_gesamt_co2+(1500/145)*(barwert_gesamt_co2))/kosten)
    project_values['nkv_2000'] = float_to_string((gesamtnutzen-barwert_gesamt_co2+(2000/145)*(barwert_gesamt_co2))/kosten)

#creating the excel-file

header = ['name','project-name','Dringlichkeit','co2_em','gesamt_co2','barwert_gesamt_co2', 'nox_value', 'barwert_nox', 'co_value','barwert_co','hc_value', 'barwert_hc', 'pm_value','barwert_pm', 'so2_value',
              'barwert_so2', 'gesamtnutzen', 'kosten','nkv','nkv_670','nkv_1000','nkv_1500','nkv_2000']

with open("BVWP-_Schiene.csv", 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=header)
    writer.writeheader()
    writer.writerows(list(values_of_project.values()))

#### Scatterplot für Projektgröße zu CO2-Emissionen für Ausgangswerte
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['co2_em']) for project_values in values_of_project.values()])
z = np.array([string_to_float(project_values['nkv']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
z_sorted = z[sorted_indices]
p_sorted = p[sorted_indices]

# Definition der Farben und Symbole
colors = ['red' if val < 1 else 'green' for val in z_sorted]
markers = ['v' if p.startswith('K') else 'o' if p.startswith('V') else 'o' for p in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='VD/VD-E')

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('CO2-Emissionen in t/a')
plt.title('Zusammenhang zwischen Projektgröße und CO2-Emissionen für Ausgangswerte')


# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

#Speicherung der Datei
output_filename = "Scatterplot_CO2_Schiene_base.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

# Diagramm schließen
plt.close()

#### Scatterplot für Projektgröße zu CO2-Emissionen für 670 €/t
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['co2_em']) for project_values in values_of_project.values()])
z = np.array([string_to_float(project_values['nkv_670']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
z_sorted = z[sorted_indices]
p_sorted = p[sorted_indices]

# Definition der Farben und Symbole
colors = ['red' if val < 1 else 'green' for val in z_sorted]
markers = ['v' if p.startswith('K') else 'o' if p.startswith('V') else 'o' for p in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='VD/VD-E')

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('CO2-Emissionen in t/a')

# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_CO2_Schiene_670.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

# Diagramm schließen
plt.close()

#### Scatterplot für Projektgröße zu CO2-Emissionen für 1000 €/t
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['co2_em']) for project_values in values_of_project.values()])
z = np.array([string_to_float(project_values['nkv_1000']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
z_sorted = z[sorted_indices]
p_sorted = p[sorted_indices]

# Definition der Farben und Symbole
colors = ['red' if val < 1 else 'green' for val in z_sorted]
markers = ['v' if p.startswith('K') else 'o' if p.startswith('V') else 'o' for p in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 's':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='VD/VD-E')

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('CO2-Emissionen in t/a')


# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_CO2_Schiene_1000.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

# Diagramm schließen
plt.close()

#### Scatterplot für Projektgröße zu CO2-Emissionen für 1500 €/t
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['co2_em']) for project_values in values_of_project.values()])
z = np.array([string_to_float(project_values['nkv_1500']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
z_sorted = z[sorted_indices]
p_sorted = p[sorted_indices]

# Definition der Farben und Symbole
colors = ['red' if val < 1 else 'green' for val in z_sorted]
markers = ['v' if p.startswith('K') else 'o' if p.startswith('V') else 'o' for p in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='VD/VD-E')

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('CO2-Emissionen in t/a')

# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_CO2_Schiene_1500.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

# Diagramm schließen
plt.close()

#### Scatterplot für Projektgröße zu CO2-Emissionen für 2000 €/t
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['co2_em']) for project_values in values_of_project.values()])
z = np.array([string_to_float(project_values['nkv_2000']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
z_sorted = z[sorted_indices]
p_sorted = p[sorted_indices]

# Definition der Farben und Symbole
colors = ['red' if val < 1 else 'green' for val in z_sorted]
markers = ['v' if p.startswith('K') else 'o' if p.startswith('V') else 'o' for p in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='VD/VD-E')

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('CO2-Emissionen in t/a')

# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_CO2_Schiene_2000.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

# Diagramm schließen
plt.close()

#### Scatterplot für Projektgröße zu NKV für Ausgangsgrößen
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['nkv']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
p_sorted = p[sorted_indices]

# Liste der Farben für die Punkte
colors = ['red' if val < 1 else 'green' for val in y_sorted]
markers = ['v' if name.startswith('K') else 'o' if name.startswith('V') else 'o' for name in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

# Markierungen für Punkte mit Dreieck (A)
for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bedarfsplan')

# Gerade Baseline bei y = 1 zeichnen
plt.axhline(y=1, color='red', linestyle='--')

current_yticks = list(plt.yticks()[0])

current_yticks.append(1)

ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

plt.yticks(current_yticks)
for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
    label.set_color(color)

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('NKV')
plt.title('Zusammenhang zwischen Projektgröße und NKV für Ausgangsgrößen')

# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_NKV_base_alleEm.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

# Diagramm schließen
plt.close()

#### Scatterplot für Projektgröße zu NKV mit CO2 = 670 €/t
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['nkv_670']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
p_sorted = p[sorted_indices]

# Liste der Farben für die Punkte
colors = ['red' if val < 1 else 'green' for val in y_sorted]
markers = ['v' if name.startswith('K') else 'o' if name.startswith('V') else 'o' for name in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

# Markierungen für Punkte mit Dreieck (A)
for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bedarfsplan')

# Gerade Baseline bei y = 1 zeichnen
plt.axhline(y=1, color='red', linestyle='--')

current_yticks = list(plt.yticks()[0])

current_yticks.append(1)

ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

plt.yticks(current_yticks)
for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
    label.set_color(color)

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('NKV')
plt.title('Zusammenhang zwischen Projektgröße und NKV für CO2 = 670 €/t')

# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_NKV_670_alleEm.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

plt.close()

#### Scatterplot für Projektgröße zu NKV für CO2-Preis von 1000€ je t
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['nkv_1000']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
p_sorted = p[sorted_indices]

# Liste der Farben für die Punkte
colors = ['red' if val < 1 else 'green' for val in y_sorted]
markers = ['v' if name.startswith('K') else 'o' if name.startswith('V') else 'o' for name in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

# Markierungen für Punkte mit Dreieck (A)
for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bedarfsplan')


# Gerade Baseline bei y = 1 zeichnen
plt.axhline(y=1, color='red', linestyle='--')

current_yticks = list(plt.yticks()[0])

current_yticks.append(1)

ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

plt.yticks(current_yticks)
for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
    label.set_color(color)

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('NKV')
plt.title('Zusammenhang zwischen Projektgröße und NKV für CO2 = 1000 €/t')

# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_NKV_1000_alleEm.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

# Diagramm schließen
plt.close()

#### Scatterplot für Projektgröße zu NKV mit CO2 = 1500 €/t
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['nkv_1500']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
p_sorted = p[sorted_indices]

# Liste der Farben für die Punkte
colors = ['red' if val < 1 else 'green' for val in y_sorted]
markers = ['v' if name.startswith('K') else 'o' if name.startswith('V') else 'o' for name in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

# Markierungen für Punkte mit Dreieck (A)
for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bedarfsplan')


# Gerade Baseline bei y = 1 zeichnen
plt.axhline(y=1, color='red', linestyle='--')

current_yticks = list(plt.yticks()[0])

current_yticks.append(1)

ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

plt.yticks(current_yticks)
for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
    label.set_color(color)

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('NKV')
plt.title('Zusammenhang zwischen Projektgröße und NKV für CO2 = 1500 €/t')

# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_NKV_1500_alleEm.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()

#### Scatterplot für Projektgröße zu NKV mit CO2 = 2000 €/t
x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
y = np.array([string_to_float(project_values['nkv_2000']) for project_values in values_of_project.values()])
p = np.array([project_values['Dringlichkeit'] for project_values in values_of_project.values()])

# Sortierung der Daten
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]
p_sorted = p[sorted_indices]

# Liste der Farben für die Punkte
colors = ['red' if val < 1 else 'green' for val in y_sorted]
markers = ['v' if name.startswith('K') else 'o' if name.startswith('V') else 'o' for name in p_sorted]

# Punktplot erstellen
plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

# Markierungen für Punkte mit Dreieck (A)
for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
    if marker == 'v':
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Kein Bedarf')
    else:
        plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bedarfsplan')

# Gerade Baseline bei y = 1 zeichnen
plt.axhline(y=1, color='red', linestyle='--')

current_yticks = list(plt.yticks()[0])

current_yticks.append(1)

ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

plt.yticks(current_yticks)
for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
    label.set_color(color)

# Achsentitel und Diagrammtitel
plt.xlabel('Projektgröße in Mio. €')
plt.ylabel('NKV')
plt.title('Zusammenhang zwischen Projektgröße und NKV für CO2 = 2000 €/t')

# Legende erstellen
legend_labels = ['Kein Bedarf', 'Bedarfsplan', 'NKV < 1', 'NKV >= 1']
legend_markers = ['v', 'o', '', '']
legend_colors = ['black', 'black', 'red', 'green']
legend_handles = [
    plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
    if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
    for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
]
plt.legend(handles=legend_handles, loc='upper right')

# Speicherung der Datei
output_filename = "Scatterplot_NKV_2000_alleEm.png"

plt.savefig(output_filename)

# Diagramm anzeigen
plt.show()
plt.close()