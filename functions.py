import numpy as np
from key import Key

def remove_duplicates(values):
    output = []
    seen = []
    for value in values:
        if not np.any([np.all(value == x) for x in seen]):
            output.append(value)
            seen.append(value)
    return output

def key_proliferation(input_keys):
    dt = np.dtype(object)
    key_list = [x.array_swap() for x in input_keys]
    map_list = []
    for list in key_list:
        for key in list:
            map_list.append(key.map)
    filtered_map_list = remove_duplicates(map_list)
    filtered_key_list = [Key(x) for x in filtered_map_list]
    return filtered_key_list
