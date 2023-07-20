import requests;
import json;

def ready(url,projectId,configId,accessToken):
    url = url+"/codedx/x/tool-connector-config/entries/"+str(projectId)+"/"+str(configId)+"/analysis-ready"
    payload={}
    headers = {
    'Authorization': 'Bearer '+accessToken,
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

def begin(url,projectId,configId,accessToken):
    url = url+"/codedx/x/tool-connector-config/entries/"+str(projectId)+"/"+str(configId)+"/analysis"
    payload = json.dumps({
    "branch": "main"
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return print(response.status_code)
