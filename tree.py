# nested dictionary defined as function and dynamic class creation.
def dict_fill(obj, key):
    obj[key] = type(obj)()
    return obj[key]


# Dynamic class obj creation with name tree, inherited from dict class
tree = type('_obj', (dict,), dict(__missing__=lambda self, key: dict_fill(self, key)))
# OR
tree1 = type('_obj', (dict,), dict(__missing__=dict_fill))

