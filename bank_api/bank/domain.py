bank = {
    'schema':{
        'approvalfy': {
            'type': 'integer'
        },
        'lendprojectcost': {
            'type': 'integer'
        },
        'board_approval_month': {
            'type': 'string'
        },
        'countryname': {
            'type': 'string'
        },
        'docty': {
            'type': 'string'
        },
        'impagency': {
            'type': 'string'
        },
    }
}

# Version of the endpoint for admins
from copy import deepcopy
banks_schema = deepcopy(bank['schema'])
# Make sure every fields are writable by admins
for key in banks_schema.keys():
    banks_schema[key]['readonly'] = False

admin_banks = {
    'url': '_admin/artist',
    'datasource': {
        'source': 'accounts',
    },
    'schema': banks_schema,
    'allowed_roles': ['super'],
    'allowed_item_roles': ['super'],
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
}
