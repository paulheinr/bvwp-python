import csv
import unittest

import pandas as pd

ORIGINAL_OUTPUT_FILE_RAIL = "resources/original_result_files/tables/BVWP-_Schiene.csv"
ORIGINAL_OUTPUT_FILE_CO2 = "resources/original_result_files/tables/BVWP_CO2.csv"
ORIGINAL_OUTPUT_FILE_ALL_EMISSIONS = "resources/original_result_files/tables/BVWP_alleEm.csv"


def read_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


class MyTestCase(unittest.TestCase):
    def test_rail_output_csv(self):
        self.check_file_diff_empty_by_csv(ORIGINAL_OUTPUT_FILE_RAIL, "../bvwp-emissions/output/rail.csv")

    def test_co2_output_csv(self):
        self.check_file_diff_empty_by_pd(ORIGINAL_OUTPUT_FILE_CO2, "")

    def test_all_emissions_output_csv(self):
        self.check_file_diff_empty_by_csv(ORIGINAL_OUTPUT_FILE_ALL_EMISSIONS,
                                          "../bvwp-emissions/output/all_emissions.csv")

    def check_file_diff_empty_by_pd(self, original_file, current_file):
        df_original = pd.read_csv(original_file)
        df_current = pd.read_csv(current_file)

        self.assertEqual(df_original, df_current)

    def check_file_diff_empty_by_csv(self, original_file, current_file):
        data_original = read_csv(original_file)
        data_current = read_csv(current_file)

        self.assertEqual(data_original, data_current)


if __name__ == '__main__':
    unittest.main()
