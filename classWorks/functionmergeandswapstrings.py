def merge_and_swap(string_one, string_two):
    new_string_one = string_one.replace(string_one[: 2], string_two[: 2])
    string_two = string_two.replace(string_two[: 2], string_one[: 2])

    return " ".join(new_string_one.split() + string_two.split())