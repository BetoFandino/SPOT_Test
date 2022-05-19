

def is_valid_params(crude_json, fields_list):
    """
    It receives two lists and verifies that each field of the crude_json are in list_field.
    """
    valid = False
    for each in crude_json:
        if each in fields_list:
            valid = True
        else:
            return False
    return valid
