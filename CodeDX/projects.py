import requests;
import json;

def list(url,accessToken):
    payload = ""
    headers = {
    'Authorization': 'Bearer '+accessToken
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return print(response.text)

def checkParent(url,accessToken,projectId):
    url =  url+"/codedx/x/projects/"+str(projectId)
    payload = ""
    headers = {
    'Authorization': 'Bearer '+accessToken
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return json.loads(response.text)["parentId"]
    else:
        return response.status_code
    
def updateParent(url,accessToken,projectId,parentId):
    url =  url+"/codedx/x/projects/"+str(projectId)
    payload = json.dumps({
        "parentId": parentId
        })
    headers = {
        'Authorization': 'Bearer '+accessToken
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.status_code
    else:
        return response.status_code

def isAvailable(url,accessToken,projectName):
    url = url+"/codedx/api/projects"
    payload = ""
    headers = {
    'Authorization': 'Bearer '+accessToken
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        result = json.loads(response.text)["projects"]
        for each in result:
            if each["name"] == projectName :
                return each["id"]
    else:
        return None

def create(url,accessToken,projectName):
    url = url+"/codedx/api/projects"

    payload = json.dumps({
    "name": projectName
    })

    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)

def delete(url,projectId,accessToken):
    url = url+"/codedx/x/projects/"+str(projectId)

    payload={}
    headers = {
        'Authorization': 'Bearer '+accessToken
        }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    return response.status_code