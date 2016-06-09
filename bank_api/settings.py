from .bank.domain import bank

DEFAULT_SETTINGS = {
    'MONGO_DBNAME' : 'api-python-exam',
    'RESOURCE_METHODS' : ['GET'],
    'DOMAIN': {
        'bank': bank
    }
}
