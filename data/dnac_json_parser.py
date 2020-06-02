import json
from pprint import pprint
with open("C:/Users/thsindhu/Documents/GitHub/DevNetTrainingAssignments/data/dnac_devices.json") as dnac_file:
    data = json.load(dnac_file)
    for d in data["response"]:
        t = {}
        t['id'] = d['id']
        t['family'] = d['family']
        t['softwareType'] = d['softwareType']
        t['type'] = d['type']
        t['managementIpAddress'] = d['managementIpAddress']
        pprint(t, indent=4)