from .bank.domain import bank, admin_banks

DEFAULT_SETTINGS = {
    'MONGO_DBNAME' : 'api-python-exam',
    'RESOURCE_METHODS' : ['GET'],
    'DOMAIN': {
        'bank': bank,
        'admin_banks': admin_banks
    }
}
