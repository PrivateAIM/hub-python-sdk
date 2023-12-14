
def nullify_empty_object_properties(data: dict) -> dict:
    for key in data.keys():
        if data[key] == '':
            data[key] = None
    return data
