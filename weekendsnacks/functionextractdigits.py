def extract_digits(number: int)->list:
    extracted = []
    for digit in str(number):
        extracted.append(int(digit))
    return extracted
