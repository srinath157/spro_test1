class Tree(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value


def dict_fill(obj, key):
    obj[key] = type(obj)()
    return obj[key]


tree = type('_obj', (dict,), dict(__missing__=lambda self, key: dict_fill(self, key)))