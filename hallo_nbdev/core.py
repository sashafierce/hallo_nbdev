# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['roman_to_int', 'int_to_roman']

# Cell
def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(s) == 1:
        return roman_dict[s[0]]

    # atleast 2 len
    converted_int = 0
    prev_item = -1
    for idx, item in enumerate(s):
        if prev_item == -1:
            prev_item = item
            if idx == len(s) - 1:
                converted_int += roman_dict[item]
            continue
        if roman_dict[prev_item] < roman_dict[item]:
            converted_int += (roman_dict[item] - roman_dict[prev_item])
            prev_item = -1
        else:
            converted_int += roman_dict[prev_item]
            if idx == len(s) - 1:
                converted_int += roman_dict[item]
            prev_item = item


        return converted_int

# Cell
def int_to_roman(i):
    """
    :type i: int
    :rtype: str
    """
    return "Not Implemented"