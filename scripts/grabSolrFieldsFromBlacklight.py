import requests
import json

sets = ['bol']
baseURL = 'https://digital-stg.library.cornell.edu/catalog/'
output = {"output": []}

for n in range(len(sets)):
    for i in range(9999):
        if len(str(i+1)) == 1:
            resp = requests.get(baseURL + sets[n] + ':000' + str(i+1) +
                                '.json')
            if resp.status_code == 200:
                output['output'].append(resp.json()['response'])
                print(requests.get(baseURL + sets[n] + ':000' + str(i+1) +
                      '.json'))
        elif len(str(i+1)) == 2:
            resp = requests.get(baseURL + sets[n] + ':00' + str(i+1) + '.json')
            if resp.status_code == 200:
                output['output'].append(resp.json()['response'])
                print(requests.get(baseURL + sets[n] + ':00' + str(i+1) +
                      '.json'))
        elif len(str(i+1)) == 3:
            resp = requests.get(baseURL + sets[n] + ':0' + str(i+1) + '.json')
            if resp.status_code == 200:
                output['output'].append(resp.json()['response'])
                print(requests.get(baseURL + sets[n] + ':0' + str(i+1) +
                      '.json'))
        elif len(str(i+1)) == 4:
            resp = requests.get(baseURL + sets[n] + ':' + str(i+1) + '.json')
            if resp.status_code == 200:
                output['output'].append(resp.json()['response'])
                print(requests.get(baseURL + sets[n] + ':' + str(i+1) +
                      '.json'))

with open('../ActiveHydraMetadata/data.json', 'w') as f:
    json.dump(output, f)
