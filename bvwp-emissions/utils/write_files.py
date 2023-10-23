import csv


def write_to_csv(values_of_project, header, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=header)
        writer.writeheader()
        writer.writerows(list(values_of_project.values()))
