class NestedDict(dict):
    """
    Nested Dictionary with Auto-initialize if the key is missing
    """
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


# merge two nested dictionaries Dict and dict2, merged_dict is the merged dictionary and no return value.
def dict_merge(dict1, dict2, merged_dict):
    for k in dict1.keys() | dict2.keys():
        if k in dict1.keys() and k in dict2.keys():
            if isinstance(dict1[k], dict):
                if k not in merged_dict : merged_dict[k] = {}
                dict_merge(dict1[k], dict2[k], merged_dict[k])
            else : merged_dict[k] = dict1[k]
        elif k in dict1 : merged_dict[k] = dict1[k]
        elif k in dict2 : merged_dict[k] = dict2[k]
