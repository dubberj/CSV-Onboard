import requests
import json

def polarisProjects(url,configId,apiToken,serverUrl,accessToken,projectName):
    url = url+"/codedx/api/tool-connector-config/values/"+configId+"/populate/project"

    payload = json.dumps({
    "api_token": apiToken,
    "auth_type": "api_token",
    "server_url": serverUrl
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        result = json.loads(response.text)
        for each in result:
            if each["display"] == projectName :
                return each["value"]
    else:
        return False
    
def blackduckProjects(url,configId,apiKey,serverUrl,accessToken,projectName):
    url = url+"/codedx/api/tool-connector-config/values/"+configId+"/populate/project"

    payload = json.dumps({
    "api_key": apiKey,
    "auth_type": "api_token",
    "server_url": serverUrl
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        result = json.loads(response.text)
        for each in result:
            if each["display"] == projectName :
                return each["value"]
    else:
        return False