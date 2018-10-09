import pprint
from utils import *
x = NestedDict()

# example of benefit using NestedDict class is
# assigning nested key value with out initializing it.
x['a']['b']['c'] = 45

a = {'B': {'fc': {'fc5.1': {'port': 'fc1/35', 'switch': 'SJC-H7-FC1'}}}}
b = {'B': {'fc': {'fc6.1': {'port': 'fc1/33', 'switch': 'SJC-H7-FC1'}}}}
c = {'B': {'data': {'eth3':{'port': 'Eth104/1/3', 'switch': 'SJC-H9-N5k', 'port_status':'up'}}}}

ab = dict_merge(a,b)
abc = dict_merge(ab,c)
pprint.pprint(abc)

sw_data = {'B': {
             'fc': {'fc5.1': {'port': 'fc1/35', 'switch': 'SJC-H7-FC1'}, 'fc6.1': {'port': 'fc1/33', 'switch': 'SJC-H7-FC1'}},
             'data': {'eth3':{'port': 'Eth104/1/3', 'switch': 'SJC-H9-N5k', 'port_status':'up'},
             'eth4': {'port': 'Eth104/1/21', 'switch': 'SJC-H9-N5k'}},
             'mgmt': {'eth1': {'port': 'Eth102/1/47', 'switch': 'SJC-H9-N5k'}, 'eth2': {'port': None, 'switch': None}}},
           'A': {
             'fc': {'fc5.1': {'port': 'fc1/36', 'switch': 'SJC-H7-FC1'}, 'fc6.1': {'port': 'fc1/34', 'switch': 'SJC-H7-FC1'}},
             'data': {'eth3': {'port': 'Eth104/1/11', 'switch': 'SJC-H9-N5k'}, 'eth4': {'port': 'Eth104/1/18', 'switch': 'SJC-H9-N5k'}},
             'mgmt': {'eth1': {'port': 'Eth102/1/1', 'switch': 'SJC-H9-N5k'}, 'eth2': {'port': None, 'switch': None}}}}

e = get_switch_list(sw_data)
pprint.pprint(e)

