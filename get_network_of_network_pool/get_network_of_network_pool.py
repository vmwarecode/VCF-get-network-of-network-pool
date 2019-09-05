#Get Network of Network Pool
#Get details of a network in a givel network pool
import requests
import json
import sys

def get_help():
    help_description = '''\n\t\t----Get network of netwok pool----
    Usage:
    python get_network_of_network_pools.py <hostname> <username> <password> <network pool ID> <network ID> \n Refer to documentation for more detais\n'''
    print help_description

def get_network_of_network_pool():
    arguments = sys.argv
    if(len(arguments) < 6):
        get_help()
        return
    hostname = 'https://'+arguments[1]
    username = arguments[2]
    password = arguments[3]
    headers = {'Content-Type': 'application/json'}
    url = hostname+'/v1/network-pools/'+arguments[4]+'/networks/'+arguments[5]
    response = requests.get(url, headers=headers,auth=(username, password))
    if(response.status_code == 200):
        response = json.loads(response.text)
        print json.dumps(response,indent=4, sort_keys=True)
    else:
        print "Error reaching the server."
        exit(1)

get_network_of_network_pool()
