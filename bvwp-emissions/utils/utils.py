import logging
import pathlib
import sys


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


def get_output_file_path(fallback_name):
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        logging.info(f"Called rail analysis with argument: {file_path}")
    else:
        file_path = f"./output/{fallback_name}.csv"
        logging.info(f"Called rail analysis without argument. Writing to default file: {file_path}")

    pathlib.Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    return file_path
