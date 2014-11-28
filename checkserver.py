import requests
import json
from StringIO import StringIO

print("1. Check that the server gives a list of all candidates.")
d = requests.get('http://qainterview.cogniance.com/candidates')
code = d.status_code
obj = json.loads(d.text)
if code != 200:
    print ('FAIL. Return ' + str(code) + ' code in response')

size = len(obj['candidates'])
if size > 0:
    print ('OK. Return ' + str(size) + ' candidates')
else:
    print ('FAIL. Return' + str(size) + ' candidates')

print("2. Check that the server add new candidate.")
load = {'name': 'Masha', 'position': 'QA intern'}
json_params = json.dumps(load)
headers = {'content-type': 'application/json'}
r = requests.post('http://qainterview.cogniance.com/candidates', data=json_params, headers=headers)
code = r.status_code
print (r.text)
obj = json.loads(r.text)
size = len(['id'])
if size != 1:
    print ('FAIL. Return ' + str(size) + ' new candidates')

new_candidate = obj['candidate']
new_candidat_id = new_candidate['id']

if code != 201:
    print ('FAIL. Return ' + str(code) + ' code in response')


print("3. Check negative verifications.")
incload = {'dogName': 'Bill', 'catName': 'Sarah', 'parrotName': 'Kluv'}
json_incparams = json.dumps(incload)
headerstwo = {'content-type': 'application/json'}
b = requests.post('http://qainterview.cogniance.com/candidates', data=json_incparams, headers=headerstwo)
code = b.status_code
if code != 201:
    print ('OK. Return ' + str(code) + ' code in response with negative verifications')

print("4. Delete the candidat.")
url = ('http://qainterview.cogniance.com/candidates/'+str(new_candidat_id))
response = requests.delete(url, data=json.dumps(load), headers=headers)
k = requests.get('http://qainterview.cogniance.com/candidates')
code = k.status_code
if code != 200:
    print ('FAIL. Return ' + str(code) + ' code in response')

