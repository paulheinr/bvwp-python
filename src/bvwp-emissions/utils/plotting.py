import numpy as np
from matplotlib import pyplot as plt

from utils import string_to_float


def create_rail_plots(values_of_project):
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
    # Speicherung der Datei
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


def create_all_emissions_plots(values_of_project):
    #### Balkendiagramm zu rausgefallen Projekten für CO2-Preis für Autobahn
    # sum of saved building costs --> determined with excel

    summe_baukosten_670 = 8115.5
    summe_baukosten_1000 = 12566.25
    summe_baukosten_1500 = 20397.9
    summe_baukosten_2000 = 22327.65

    # number of cancelled projects differentiated according to "Autobahnen" and "Bundesstraßen" --> determined with excel

    anz_nkv_unter1_670_a = 52
    anz_nkv_unter1_670_b = 65
    anz_nkv_unter1_1000_a = 84
    anz_nkv_unter1_1000_b = 93
    anz_nkv_unter1_1500_a = 118
    anz_nkv_unter1_1500_b = 135
    anz_nkv_unter1_2000_a = 134
    anz_nkv_unter1_2000_b = 186

    # sum of saved building costs differentiated

    summe_baukosten_670_a = 6.12
    summe_baukosten_670_b = 2.00
    summe_baukosten_1000_a = 9.10
    summe_baukosten_1000_b = 3.46
    summe_baukosten_1500_a = 15.39
    summe_baukosten_1500_b = 5.01
    summe_baukosten_2000_a = 16.04
    summe_baukosten_2000_b = 6.28

    # sum of saved CO2-emissions --> determined with excel

    summe_co2_670_a = 0.37
    summe_co2_670_b = 0.09
    summe_co2_1000_a = 0.69
    summe_co2_1000_b = 0.16
    summe_co2_1500_a = 1.04
    summe_co2_1500_b = 0.26
    summe_co2_2000_a = 1.18
    summe_co2_2000_b = 0.32
    summe_co2_100_a = 1.55
    summe_co2_100_b = 0.49
    summe_co2_100 = 2.04

    x = np.array([670, 1000, 1500, 2000])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([anz_nkv_unter1_670_a, anz_nkv_unter1_1000_a, anz_nkv_unter1_1500_a, anz_nkv_unter1_2000_a])
    y2 = np.array([195, 195, 195, 195])  # Gesamtanzahl der Projekte mit NKV < 1

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_670_a, summe_co2_1000_a, summe_co2_1500_a, summe_co2_2000_a])
    y4 = np.array([summe_co2_100_a, summe_co2_100_a, summe_co2_100_a, summe_co2_100_a])
    y5 = np.array([summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b])

    # Anzahl der Balken
    num_bars = len(x)

    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='A mit NKV > 1', color='royalblue')
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='A mit NKV < 1', color='lightblue')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Anzahl Autobahnprojekte', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (Anzahl der Projekte mit NKV < 1)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.0f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Erstellung der Legende
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    plt.xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t' for val in x])

    # Diagramm anzeigen
    plt.show()

    #### Balkendiagramm zu rausgefallen Projekten für CO2-Preis für Bundesstraßen
    x = np.array([670, 1000, 1500, 2000])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([anz_nkv_unter1_670_b, anz_nkv_unter1_1000_b, anz_nkv_unter1_1500_b, anz_nkv_unter1_2000_b])
    y2 = np.array([833, 833, 833, 833])  # Gesamtanzahl der Projekte mit NKV < 1

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_670_b, summe_co2_1000_b, summe_co2_1500_b, summe_co2_2000_b])
    y4 = np.array([summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b])

    # Anzahl der Balken
    num_bars = len(x)

    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Bundesstraßen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='B mit NKV > 1', color='orange')
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='B mit NKV < 1', color='wheat')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Anzahl Bundesstraßenprojekte', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Bundesstraßen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (Anzahl der Projekte mit NKV < 1)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.0f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Erstellung der Legende
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    plt.xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t' for val in x])

    # Diagramm anzeigen
    plt.show()

    ############# Balkendiagramm zu Baukosten ########################################################################################
    x = np.array([670, 1000, 1500, 2000])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([summe_baukosten_670_a, summe_baukosten_1000_a, summe_baukosten_1500_a, summe_baukosten_2000_a])
    y2 = np.array([23.67, 23.67, 23.67, 23.67])

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_670_a, summe_co2_1000_a, summe_co2_1500_a, summe_co2_2000_a])
    y4 = np.array([summe_co2_100_a, summe_co2_100_a, summe_co2_100_a, summe_co2_100_a])

    # Anzahl der Balken
    num_bars = len(x)

    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='Baukosten A', color='royalblue',
                    zorder=1)
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='Einsparung A', color='lightblue')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Baukostensumme in Mrd. €', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (vebleibende Baukosten A)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-12, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    plt.xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t' for val in x])

    # Diagramm anzeigen
    plt.show()

    ############# Balkendiagramm zu Baukosten ########################################################################################
    x = np.array([670, 1000, 1500, 2000])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1

    y5 = np.array([summe_baukosten_670_b, summe_baukosten_1000_b, summe_baukosten_1500_b, summe_baukosten_2000_b])
    y7 = np.array([25.59, 25.59, 25.59, 25.59])

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_670_b, summe_co2_1000_b, summe_co2_1500_b, summe_co2_2000_b])
    y4 = np.array((summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b))

    # Anzahl der Balken
    num_bars = len(x)

    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y7 - y5, width, label='Baukosten B', color='orange', zorder=1)
    ax1.bar(np.arange(num_bars) * equal_spacing, y5, width, bottom=y7 - y5, label='Einsparung B', color='wheat')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Baukostensumme in Mrd. €', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (vebleibende Baukosten A)
    for bar, y_val in zip(bars1, y7 - y5):
        height = bar.get_height()
        ax1.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-12, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    plt.xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t' for val in x])

    # Diagramm anzeigen
    plt.show()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für Ausgangswerte
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in t/a')
    plt.title('Zusammenhang zwischen Projektgröße und CO2-Emissionen für Ausgangswerte')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_base.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für 670 €
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv_670']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in t/a')
    plt.title('670 €/t')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_670.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für 1000 €
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv_1000']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in t/a')
    plt.title('1000 €/t')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_1000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für 1500 €
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv_1500']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in t/a')
    plt.title('1500 €/t')

    # Erstelung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_1500.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für 2000
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv_2000']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in Mio. t/a')
    plt.title('2000 €/t')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_2000.png"

    # Diagramm als Datei speichern (zum Beispiel im PNG-Format)
    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu NKV für Ausgangsgrößen
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['nkv']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in y_sorted]
    markers = ['v' if name.startswith('A') else 'o' if name.startswith('B') else 'o' for name in p_sorted]

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')
    plt.text(max(x_sorted) + 5, 1, '1', ha='left', va='center', color='red', fontsize=10,
             bbox=dict(facecolor='white', edgecolor='white', pad=5))

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('NKV')
    plt.title('Zusammenhang zwischen Projektgröße und NKV für Ausgangsgrößen')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='upper right')

    # Speicherung der Datei
    output_filename = "Scatterplot_NKV_base.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu NKV mit CO2 = 670 €/t
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['nkv_670']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sprtierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in y_sorted]
    markers = ['v' if name.startswith('A') else 'o' if name.startswith('B') else 'o' for name in p_sorted]

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')
    plt.text(max(x_sorted) + 5, 1, '1', ha='left', va='center', color='red', fontsize=10,
             bbox=dict(facecolor='white', edgecolor='white', pad=5))

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('NKV')
    plt.title('Zusammenhang zwischen Projektgröße und NKV für CO2 = 670 €/t')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='upper right')

    # Speicherung der Datei
    output_filename = "Scatterplot_NKV_670.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    plt.close()

    #### Scatterplot für Projektgröße zu NKV für CO2-Preis von 1000€ je t
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['nkv_1000']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in y_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')
    plt.text(max(x_sorted) + 5, 1, '1', ha='left', va='center', color='red', fontsize=10,
             bbox=dict(facecolor='white', edgecolor='white', pad=5))

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('NKV')
    plt.title('Zusammenhang zwischen Projektgröße und NKV für CO2 = 1000 €/t')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='upper right')

    # Speicherung der Datei
    output_filename = "Scatterplot_NKV_1000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu NKV mit CO2 = 1500 €/t
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['nkv_1500']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in y_sorted]
    markers = ['v' if name.startswith('A') else 'o' if name.startswith('B') else 'o' for name in p_sorted]

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')
    plt.text(max(x_sorted) + 5, 1, '1', ha='left', va='center', color='red', fontsize=10,
             bbox=dict(facecolor='white', edgecolor='white', pad=5))

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('NKV')
    plt.title('Zusammenhang zwischen Projektgröße und NKV für CO2 = 1500 €/t')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='upper right')

    # Speicherung der Datei
    output_filename = "Scatterplot_NKV_1500.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    #### Scatterplot für Projektgröße zu NKV mit CO2 = 2000 €/t
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['nkv_2000']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in y_sorted]
    markers = ['v' if name.startswith('A') else 'o' if name.startswith('B') else 'o' for name in p_sorted]

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')
    plt.text(max(x_sorted) + 5, 1, '1', ha='left', va='center', color='red', fontsize=10,
             bbox=dict(facecolor='white', edgecolor='white', pad=5))

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('NKV')
    plt.title('Zusammenhang zwischen Projektgröße und NKV für CO2 = 2000 €/t')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='upper right')

    # Speicherung der Datei
    output_filename = "Scatterplot_NKV_2000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()
    ################ --> Boxplot und Violinplot

    x_values = np.array([145])
    y_values = np.array([string_to_float(project_values['nkv']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert für Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 145 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Soeicherung der Datei
    output_filename = "Box_Violinplot_base.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Violinplot für CO2-Preis von 670€ je t
    x_values = np.array([670])
    y_values = np.array([string_to_float(project_values['nkv_670']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert für Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert für Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 670 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Datei
    output_filename = "Box_Violinplot_670.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Violinplot für CO2-Preis von 1000€ je t
    x_values = np.array([1000])
    y_values = np.array([string_to_float(project_values['nkv_1000']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 1000 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Daten
    output_filename = "Box_Violinplot_1000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Violinplot für CO2-Preis von 1500€ je t
    x_values = np.array([1500])
    y_values = np.array([string_to_float(project_values['nkv_1500']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert für Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert für Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 1500 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Datei
    output_filename = "Box_Violinplot_1500.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Violinplot für CO2-Preis von 2000€ je t
    x_values = np.array([2000])
    y_values = np.array([string_to_float(project_values['nkv_2000']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert für Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert für Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 2000 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Datei
    output_filename = "Box_Violinplot_2000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()


def create_co2_plots(values_of_project):
    #### Balkendiagramm zu rausgefallen Projekten für CO2-Preis für Autobahn
    # number of cancelled projects differentiated according to "Autobahnen" and "Bundesstraßen" --> determined with excel

    anz_nkv_unter1_670_a = 46
    anz_nkv_unter1_670_b = 63
    anz_nkv_unter1_1000_a = 67
    anz_nkv_unter1_1000_b = 93
    anz_nkv_unter1_1500_a = 100
    anz_nkv_unter1_1500_b = 137
    anz_nkv_unter1_2000_a = 124
    anz_nkv_unter1_2000_b = 189
    anz_nkv_unter1_90_a = 163
    anz_nkv_unter1_90_b = 324
    anz_nkv_unter1_95_a = 170
    anz_nkv_unter1_95_b = 361
    anz_nkv_unter1_975_a = 172
    anz_nkv_unter1_975_b = 371
    anz_nkv_unter1_995_a = 174
    anz_nkv_unter1_995_b = 411

    # sum of saved building costs --> determined with excel

    summe_baukosten_670 = 7817.122
    summe_baukosten_1000 = 10830.636
    summe_baukosten_1500 = 19377.919
    summe_baukosten_2000 = 22157.229
    summe_baukosten_90 = 28933.83
    summe_baukosten_95 = 31658.877
    summe_baukosten_975 = 33001.874
    summe_baukosten_995 = 34259.086

    # sum of saved building costs differentiated

    summe_baukosten_670_a = 4.35
    summe_baukosten_670_b = 1.74
    summe_baukosten_1000_a = 6.66
    summe_baukosten_1000_b = 2.74
    summe_baukosten_1500_a = 12.21
    summe_baukosten_1500_b = 4.78
    summe_baukosten_2000_a = 15.69
    summe_baukosten_2000_b = 6.03
    summe_baukosten_90_a = 19.29
    summe_baukosten_90_b = 9.75
    summe_baukosten_95_a = 20.94
    summe_baukosten_95_b = 11.18
    summe_baukosten_975_a = 21.06
    summe_baukosten_975_b = 11.94
    summe_baukosten_995_a = 21.25
    summe_baukosten_995_b = 13.04

    # sum of saved CO2-emissions --> determined with excel

    summe_co2_670_a = 0.33
    summe_co2_670_b = 0.06
    summe_co2_1000_a = 0.58
    summe_co2_1000_b = 0.14
    summe_co2_1500_a = 0.88
    summe_co2_1500_b = 0.25
    summe_co2_2000_a = 1.15
    summe_co2_2000_b = 0.32
    summe_co2_90_a = 1.39
    summe_co2_90_b = 0.46
    summe_co2_95_a = 1.45
    summe_co2_95_b = 0.45
    summe_co2_975_a = 1.46
    summe_co2_975_b = 0.53
    summe_co2_995_a = 1.48
    summe_co2_995_b = 0.54
    summe_co2_100_a = 1.55
    summe_co2_100_b = 0.49

    x = np.array([670, 1000, 1500, 2000])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([anz_nkv_unter1_670_a, anz_nkv_unter1_1000_a, anz_nkv_unter1_1500_a, anz_nkv_unter1_2000_a])
    y2 = np.array([195, 195, 195, 195])  # Gesamtanzahl der Projekte mit NKV < 1

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_670_a, summe_co2_1000_a, summe_co2_1500_a, summe_co2_2000_a])
    y4 = np.array([summe_co2_100_a, summe_co2_100_a, summe_co2_100_a, summe_co2_100_a])
    y5 = np.array([summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b])

    # Anzahl der Balken
    num_bars = len(x)

    # Gleichmäßiger Abstand zwischen den Balken
    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='A mit NKV > 1', color='royalblue')
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='A mit NKV < 1', color='lightblue')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Anzahl Autobahnprojekte', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (Anzahl der Projekte mit NKV < 1)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.0f}'.format(y_val),  # Auf ganze Zahlen runden
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    plt.xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t' for val in x])

    # Diagramm anzeigen
    plt.show()

    #### Balkendiagramm zu rausgefallen Projekten für CO2-Preis für Bundesstraßen
    x = np.array([670, 1000, 1500, 2000])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([anz_nkv_unter1_670_b, anz_nkv_unter1_1000_b, anz_nkv_unter1_1500_b, anz_nkv_unter1_2000_b])
    y2 = np.array([833, 833, 833, 833])  # Gesamtanzahl der Projekte mit NKV < 1

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_670_b, summe_co2_1000_b, summe_co2_1500_b, summe_co2_2000_b])
    y4 = np.array([summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b])

    # Anzahl der Balken
    num_bars = len(x)

    # Gleichmäßiger Abstand zwischen den Balken
    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='B mit NKV > 1', color='orange')
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='B mit NKV < 1', color='wheat')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Anzahl Bundesstraßenprojekte', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (Anzahl der Projekte mit NKV < 1)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.0f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    plt.xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t' for val in x])

    # Diagramm anzeigen
    plt.show()

    ################ Balkendiagramm für die Emissionseinsparungen ####################################################################
    x = np.array([4273, 5330, 5630, 7267])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([anz_nkv_unter1_90_a, anz_nkv_unter1_95_a, anz_nkv_unter1_975_a, anz_nkv_unter1_995_a])
    y2 = np.array([195, 195, 195, 195])  # Gesamtanzahl der Projekte mit NKV < 1

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_90_a, summe_co2_95_a, summe_co2_975_a, summe_co2_995_a])
    y4 = np.array([summe_co2_100_a, summe_co2_100_a, summe_co2_100_a, summe_co2_100_a])
    y5 = np.array([summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b])

    # Anzahl der Balken
    num_bars = len(x)

    # Gleichmäßiger Abstand zwischen den Balken
    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='A mit NKV > 1', color='royalblue')
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='A mit NKV < 1', color='lightblue')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Anzahl Autobahnprojekte', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (Anzahl der Projekte mit NKV < 1)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.0f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    ax1.set_xticks(np.arange(num_bars) * equal_spacing)
    ax1.set_xticklabels([f'{val} €/t ≈ {prozent}%' for val, prozent in zip(x, [90, 95, 97.5, 99.5])])

    # Diagramm anzeigen
    plt.show()

    ################ Balkendiagramm für die Emissionseinsparungen ####################################################################
    x = np.array([4273, 5330, 5630, 7267])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([anz_nkv_unter1_90_b, anz_nkv_unter1_95_b, anz_nkv_unter1_975_b, anz_nkv_unter1_995_b])
    y2 = np.array([833, 833, 833, 833])  # Gesamtanzahl der Projekte mit NKV < 1

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_90_b, summe_co2_95_b, summe_co2_975_b, summe_co2_995_b])
    y4 = np.array([summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b])

    # Anzahl der Balken
    num_bars = len(x)

    # Gleichmäßiger Abstand zwischen den Balken
    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='B mit NKV > 1', color='orange')
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='B mit NKV < 1', color='wheat')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Anzahl Bundesstrassenprojekte', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (Anzahl der Projekte mit NKV < 1)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.0f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    ax1.set_xticks(np.arange(num_bars) * equal_spacing)
    ax1.set_xticklabels([f'{val} €/t ≈ {prozent}%' for val, prozent in zip(x, [90, 95, 97.5, 99.5])])

    # Diagramm anzeigen
    plt.show()

    ############# Balkendiagramm zu Baukosten ########################################################################################
    x = np.array([670, 1000, 1500, 2000])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([summe_baukosten_670_a, summe_baukosten_1000_a, summe_baukosten_1500_a, summe_baukosten_2000_a])
    y2 = np.array([23.67, 23.67, 23.67, 23.67])

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_670_a, summe_co2_1000_a, summe_co2_1500_a, summe_co2_2000_a])
    y4 = np.array([summe_co2_100_a, summe_co2_100_a, summe_co2_100_a, summe_co2_100_a])

    # Anzahl der Balken
    num_bars = len(x)

    # Gleichmäßiger Abstand zwischen den Balken
    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='Baukosten A', color='royalblue',
                    zorder=1)
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='Einsparung A', color='lightblue')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Baukostensumme in Mrd. €', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (vebleibende Baukosten A)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-12, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    plt.xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t' for val in x])

    # Diagramm anzeigen
    plt.show()

    ############# Balkendiagramm zu Baukosten ########################################################################################
    x = np.array([670, 1000, 1500, 2000])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    y5 = np.array([summe_baukosten_670_b, summe_baukosten_1000_b, summe_baukosten_1500_b, summe_baukosten_2000_b])
    y7 = np.array([25.59, 25.59, 25.59, 25.59])

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_670_b, summe_co2_1000_b, summe_co2_1500_b, summe_co2_2000_b])
    y4 = np.array((summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b))
    # Anzahl der Balken
    num_bars = len(x)

    # Gleichmäßiger Abstand zwischen den Balken
    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y7 - y5, width, label='Baukosten B', color='orange', zorder=1)
    ax1.bar(np.arange(num_bars) * equal_spacing, y5, width, bottom=y7 - y5, label='Einsparung B', color='wheat')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Baukostensumme in Mrd. €', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (vebleibende Baukosten A)
    for bar, y_val in zip(bars1, y7 - y5):
        height = bar.get_height()
        ax1.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-12, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    plt.xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t' for val in x])

    # Diagramm anzeigen
    plt.show()

    ################ Balkendiagramm zu Baukosten fpr Einsparszenarien ########################################################################
    x = np.array([4273, 5330, 5630, 7267])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y1 = np.array([summe_baukosten_90_a, summe_baukosten_95_a, summe_baukosten_975_a, summe_baukosten_995_a])
    y2 = np.array([23.67, 23.67, 23.67, 23.67])  # Gesamtanzahl der Projekte mit NKV < 1

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y3 = np.array([summe_co2_90_a, summe_co2_95_a, summe_co2_975_a, summe_co2_995_a])
    y4 = np.array([summe_co2_100_a, summe_co2_100_a, summe_co2_100_a, summe_co2_100_a])

    # Anzahl der Balken
    num_bars = len(x)

    # Gleichmäßiger Abstand zwischen den Balken
    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Autobahnen (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y2 - y1, width, label='Baukosten A', color='royalblue')
    ax1.bar(np.arange(num_bars) * equal_spacing, y1, width, bottom=y2 - y1, label='Einsparung A', color='lightblue')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Baukostensumme in Mrd. €', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y3, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y3, width, bottom=y4 - y3, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (verbleibende Baukostensumme A)
    for bar, y_val in zip(bars1, y2 - y1):
        height = bar.get_height()
        ax1.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-12, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung A)
    for bar, y_val in zip(bars2, y4 - y3):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    ax1.set_xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t ≈ {prozent}%' for val, prozent in zip(x, [90, 95, 97.5, 99.5])])

    # Diagramm anzeigen
    plt.show()

    ################ Balkendiagramm zu Baukosten fpr Einsparszenarien ########################################################################
    x = np.array([4273, 5330, 5630, 7267])  # x-Positionen für die Balken
    width = 10  # Breite der Balken

    # Anzahl der Projekte mit NKV < 1
    y5 = np.array([summe_baukosten_90_b, summe_baukosten_95_b, summe_baukosten_975_b, summe_baukosten_995_b])
    y7 = np.array([25.59, 25.59, 25.59, 25.59])

    # Einsparung von CO2 bei jeweiligem CO2-Preis
    y4 = np.array([summe_co2_100_b, summe_co2_100_b, summe_co2_100_b, summe_co2_100_b])
    y6 = np.array([summe_co2_90_b, summe_co2_95_b, summe_co2_975_b, summe_co2_995_b])

    # Anzahl der Balken
    num_bars = len(x)

    # Gleichmäßiger Abstand zwischen den Balken
    equal_spacing = 50

    # Erstes gestapeltes Balkendiagramm für Bundesstraße (linke y-Achse)
    fig, ax1 = plt.subplots()
    bars1 = ax1.bar(np.arange(num_bars) * equal_spacing, y7 - y5, width, label='Baukosten B', color='orange')
    ax1.bar(np.arange(num_bars) * equal_spacing, y5, width, bottom=y7 - y5, label='Einsparung B', color='wheat')
    ax1.set_xlabel('CO2-Preis')
    ax1.set_ylabel('Baukostensumme in Mrd. €', color='black')

    # Zweites gestapeltes Balkendiagramm C02-Ausstoss für Autobahnen (rechte y-Achse)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(np.arange(num_bars) * equal_spacing + width, y4 - y6, width, label='CO2-Emissionen',
                    color='limegreen')
    ax2.bar(np.arange(num_bars) * equal_spacing + width, y6, width, bottom=y4 - y6, label='CO2-Einsparung',
            color='lightgreen')
    ax2.set_ylabel('CO2-Emissionen in Mio. t/a', color='black')

    # Beschriftung der Balken mit y1-Werten (verbleibende Baukostensumme B)
    for bar, y_val in zip(bars1, y7 - y5):
        height = bar.get_height()
        ax1.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(-12, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Beschriftung der Balken mit y3-Werten (CO2-Einsparung B)
    for bar, y_val in zip(bars2, y4 - y6):
        height = bar.get_height()
        ax2.annotate('{:.2f}'.format(y_val),
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(5, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', color='black', zorder=10)

    # Gemeinsame Legende erstellen
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    all_handles = handles1 + handles2
    all_labels = labels1 + labels2

    plt.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.18), ncol=4)

    # X-Achse anpassen
    ax1.set_xticks(np.arange(num_bars) * equal_spacing, x)
    ax1.set_xticklabels([f'{val} €/t ≈ {prozent}%' for val, prozent in zip(x, [90, 95, 97.5, 99.5])])

    # Diagramm anzeigen
    plt.show()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für Ausgangswerte
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in t/a')
    plt.title('Zusammenhang zwischen Projektgröße und CO2-Emissionen für Ausgangswerte')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_base.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für 670 €
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv_670']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Liste der Farben für die Punkte
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in t/a')
    plt.title('Zusammenhang zwischen Projektgröße und CO2-Emissionen für 670 €/t')

    # Erstellung der Legende
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_670.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für 1000 €
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv_1000']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sprtierung der Daten
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in t/a')
    plt.title('Zusammenhang zwischen Projektgröße und CO2-Emissionen für 1000 €/t')

    # Legende erstellen
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_1000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für 1500 €
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv_1500']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten nach
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in t/a')
    plt.title('Zusammenhang zwischen Projektgröße und CO2-Emissionen für 1500 €/t')

    # Legende erstellen
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_1500.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Scatterplot für Projektgröße zu CO2-Emissionen für 2000
    x = np.array([string_to_float(project_values['kosten']) for project_values in values_of_project.values()])
    y = np.array([string_to_float(project_values['lifec_em']) for project_values in values_of_project.values()])
    z = np.array([string_to_float(project_values['nkv_2000']) for project_values in values_of_project.values()])
    p = np.array([project_values['project-name'] for project_values in values_of_project.values()])

    # Sortierung der Daten nach
    sorted_indices = np.argsort(x)
    x_sorted = x[sorted_indices]
    y_sorted = y[sorted_indices]
    z_sorted = z[sorted_indices]
    p_sorted = p[sorted_indices]

    # Definition der Farben und Symbole
    colors = ['red' if val < 1 else 'green' for val in z_sorted]
    markers = ['v' if p.startswith('A') else 'o' if p.startswith('B') else 'o' for p in p_sorted]

    # Neue Skalierung der y-Achse für bessere Übersicht
    new_y_min = -12000
    new_y_max = 100000
    plt.ylim(new_y_min, new_y_max)

    # Punktplot erstellen
    plt.scatter(x_sorted, y_sorted, c=colors, marker='None')

    # Markierungen für Punkte mit Dreieck (A)
    for x_val, y_val, marker, color in zip(x_sorted, y_sorted, markers, colors):
        if marker == 'v':
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Autobahnen')
        else:
            plt.scatter(x_val, y_val, marker=marker, color=color, edgecolor='black', s=80, label='Bundesstraßen')

    # Achsentitel und Diagrammtitel
    plt.xlabel('Projektgröße in Mio. €')
    plt.ylabel('CO2-Emissionen in Mio. t/a')
    plt.title('Zusammenhang zwischen Projektgröße und CO2-Emissionen für 2000 €/t')

    # Legende erstellen
    legend_labels = ['Autobahnen', 'Bundesstraßen', 'NKV < 1', 'NKV >= 1']
    legend_markers = ['v', 'o', '', '']
    legend_colors = ['black', 'black', 'red', 'green']
    legend_handles = [
        plt.Line2D([0], [0], marker=marker, color=color, label=label, markersize=10, markerfacecolor='black')
        if marker != '' else plt.Line2D([0], [0], color=color, label=label, markersize=10)
        for marker, color, label in zip(legend_markers, legend_colors, legend_labels)
    ]
    plt.legend(handles=legend_handles, loc='lower right')

    # Speicherung der Datei
    output_filename = "Scatterplot_CO2_2000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.show()

    # Diagramm schließen
    plt.close()

    ################ --> Boxplot und Violinplot

    x_values = np.array([145])
    y_values = np.array([string_to_float(project_values['nkv']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    # Y-Achsenbeschriftungen
    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert für Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert für Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 145 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Datei
    output_filename = "Box_Violinplot_base.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Violinplot für CO2-Preis von 670€ je t
    x_values = np.array([670])
    y_values = np.array([string_to_float(project_values['nkv_670']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 670 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Datei
    output_filename = "Box_Violinplot_670.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Violinplot für CO2-Preis von 1000€ je t
    x_values = np.array([1000])
    y_values = np.array([string_to_float(project_values['nkv_1000']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert für Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert für Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 1000 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Datei
    output_filename = "Box_Violinplot_1000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Violinplot für CO2-Preis von 1500€ je t
    x_values = np.array([670])
    y_values = np.array([string_to_float(project_values['nkv_1500']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert für Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert für Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 1500 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Datei
    output_filename = "Box_Violinplot_1500.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()

    #### Violinplot für CO2-Preis von 2000€ je t
    x_values = np.array([670])
    y_values = np.array([string_to_float(project_values['nkv_2000']) for project_values in values_of_project.values()])
    p_values = [project_values['project-name'] for project_values in values_of_project.values()]

    # Unterscheidung von Autobahn und Bundesstraße
    y_values_a = [y for y, p in zip(y_values, p_values) if p.startswith('A')]
    y_values_b = [y for y, p in zip(y_values, p_values) if p.startswith('B')]

    # Plot erstellen
    fig, ax = plt.subplots(figsize=(8, 6))

    # Violinplot erstellen und über Boxplot legen
    violin_parts_a = ax.violinplot(dataset=[y_values_a], positions=[0.2], showmeans=False, showmedians=False,
                                   widths=0.5)
    violin_parts_b = ax.violinplot(dataset=[y_values_b], positions=[0.8], showmeans=False, showmedians=False,
                                   widths=0.5)

    box_parts_a = ax.boxplot([y_values_a], positions=[0.2], widths=0.15, patch_artist=True)
    box_parts_b = ax.boxplot([y_values_b], positions=[0.8], widths=0.15, patch_artist=True)

    # Farben für Violinplot und Boxplot für A und B
    for pc in violin_parts_a['bodies']:
        pc.set_facecolor('royalblue')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for pc in violin_parts_b['bodies']:
        pc.set_facecolor('orange')
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)

    for box in box_parts_a['boxes']:
        box.set(facecolor='royalblue', edgecolor='black', alpha=0.6)

    for box in box_parts_b['boxes']:
        box.set(facecolor='orange', edgecolor='black', alpha=0.6)

    # Gerade Baseline bei y = 1 zeichnen
    plt.axhline(y=1, color='red', linestyle='--')

    current_yticks = list(plt.yticks()[0])

    current_yticks.append(1)

    ytick_colors = ['red' if tick == 1 else 'black' for tick in current_yticks]

    plt.yticks(current_yticks)
    for label, color in zip(plt.gca().get_yticklabels(), ytick_colors):
        label.set_color(color)

    # Medianwert Boxplot A
    median_a = np.median(y_values_a)
    ax.text(0.2, median_a, f'Median A: {median_a:.2f}', ha='center', va='bottom', color='yellow')

    # Medianwert für Boxplot B
    median_b = np.median(y_values_b)
    ax.text(0.8, median_b, f'Median B: {median_b:.2f}', ha='center', va='bottom', color='green')

    # Achsenbeschriftungen und Titel
    ax.set_title('NKV-Verteilung für CO2 = 2000 €/t')
    ax.set_xlabel('Projektgruppe')
    ax.set_ylabel('NKV')
    ax.set_xticks([0.2, 0.8])
    ax.set_xticklabels(['Autobahn', 'Bundesstraße'])

    # Speicherung der Datei
    output_filename = "Box_Violinplot_2000.png"

    plt.savefig(output_filename)

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

    # Diagramm schließen
    plt.close()
