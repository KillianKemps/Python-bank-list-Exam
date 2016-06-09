import requests

banks_resp = requests.get('http://localhost:5000/bank', auth=('admin', ''))

banks = banks_resp.json()

for bank in banks['_items']:
    print('Country: ', bank['countryname'])
