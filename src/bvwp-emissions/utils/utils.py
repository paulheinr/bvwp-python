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
