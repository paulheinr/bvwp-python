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
