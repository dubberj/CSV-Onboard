import requests;
import json

def createBlankPolarisConfiguration(url,projectId,accessToken):

    url = url+"/codedx/api/tool-connector-config//entries/"+projectId

    payload = json.dumps({
    "tool": "Coverity on Polaris",
    "name": "Polaris Connector"
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)

def createBlankBlackDuckConfiguration(url,projectId,accessToken):

    url = url+"/codedx/api/tool-connector-config//entries/"+projectId

    payload = json.dumps({
    "tool": "Black Duck Hub",
    "name": "Black Duck Connector"
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)

def editPolarisConfig(url,configId,accessToken,serverUrl,apiToken,projectValue,projectBranchValue):
    url = url+"/codedx/api/tool-connector-config//values/"+str(configId)

    payload = json.dumps({
    "server_url": serverUrl,
    "auth_type": "api_token",
    "api_token": apiToken,
    "project": projectValue,
    "connector_mode": "project",
    "branch": projectBranchValue,
    "available-during-analysis": True
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.status_code

def editBlackDuckConfig(url,configId,accessToken,serverUrl,apiKey,projectValue,projectVersion):
    url = url+"/codedx/api/tool-connector-config//values/"+str(configId)

    payload = json.dumps({
    "server_url": serverUrl,
    "auth_type": "api_token",
    "api_key": apiKey,
    "project": projectValue,
    "version": projectVersion,
    "available-during-analysis": True
    })

    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.text
