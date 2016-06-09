bank_schema = {
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

DEFAULT_SETTINGS = {
    'MONGO_DBNAME' : 'api-python-exam',
    'RESOURCE_METHODS' : ['GET'],
    'DOMAIN': {
        'bank': bank_schema
    }
}
