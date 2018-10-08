class NestedDict(dict):
    """
    Nested Dictionary with Auto-initialize if the key is missing
    """
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


# merge two nested dictionaries Dict and dict2
def dict_merge(dict1, dict2):
    merged_dict = {}
    for k in dict1.keys() | dict2.keys():
        if k in dict1.keys() and k in dict2.keys():
            if isinstance(dict1[k], dict) : merged_dict[k] = dict_merge(dict1[k], dict2[k])
            else : merged_dict[k] = dict1[k]
        elif k in dict1 : merged_dict[k] = dict1[k]
        elif k in dict2 : merged_dict[k] = dict2[k]
    return merged_dict

# returns list with values matching a key in a nested dictionary. - here the key is 'switch'
def get_switch_list(switchport_dict):
    switch_list = []
    for key, value in switchport_dict.items():
        if isinstance(value, dict):
            switch_list += get_switch_list(value)
        elif key == 'switch':
            if value:
                switch_list.append(value)
    return list(set(switch_list))

