import requests
import json
def createJiraConfig(url,projectId,jiraToken,jiraUrl,projectKey,accessToken):
    url = url+"/codedx/x/issueTracker/jira/"+str(projectId)+"/config"

    payload = json.dumps({
    "username": "",
    "password": {
        "submitted": jiraToken
    },
    "trackerType": "jira",
    "url": jiraUrl,
    "authType": "token",
    "projectKey": projectKey,
    "refreshInterval": 60,
    "projectId": projectId
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code

def getProjectKey(url,jiraUrl,JiraToken,projectId,accessToken,jiraProjectName):
    url = url+"/codedx/x/issueTracker/jira/check-config/projects"

    payload = json.dumps({
    "trackerType": "jira",
    "url": jiraUrl,
    "username": "",
    "password": {
        "submitted": JiraToken
    },
    "authType": "token",
    "projectId": projectId
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    if response.status_code == 200:
        result = json.loads(response.text)
        for each in result:
            if each["name"] == jiraProjectName :
                return each["id"]
    else:
        return False