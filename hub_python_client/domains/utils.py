from enum import Enum


def nullify_empty_object_properties(data: dict) -> dict:
    for key in data.keys():
        if data[key] == '':
            data[key] = None
    return data


def enum_encoder(obj):
    if isinstance(obj, Enum):
        return obj.value
    else:
        raise TypeError(f"{obj} is not Enum")
    raise TypeError(f"{obj} is not serializable")
