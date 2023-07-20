import requests
import json


def validateRemote(url,accessToken,gitUrl,branch):
    payload = json.dumps({
        "url": gitUrl,
        "branch": branch
    })

    url = url+"/codedx/x/gitconf/3/validate-remote"

    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }   

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    if  json.loads(response.text)["valid"] == True :
        return True
    elif json.loads(response.text)["valid"] == False and json.loads(response.text)["code"] == "REQUIRES_AUTH":
        return "REQUIRES_AUTH"
    else:
        return False
    
def updateGit(url,projectId,gitUrl,branch,accessToken,username,githubToken):
    print("im here"+username)
    print(githubToken)
    url = url+"/codedx/x/gitconf/"+projectId
    payload = json.dumps({
    "url": gitUrl,
    "branch": branch
    })
    headers = {
    'Authorization': 'Bearer '+accessToken,
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text,response.status_code)
    if len(username) != 0:
        print("im here")
        url1 = url+"/auth/http"
        payload1 = json.dumps({"username":username,"password":githubToken})
        print(payload1)
        response = requests.request("POST", url1, headers=headers, data=payload1)
        print(response.text,response.status_code)

    return response.status_code