import csv;
from CodeDX import projects,toolConfig,analysis,gitConfig,populate,issueTracker;

# Property of Synopsys Inc, Designed and Built by Synopsys.

# codeDx Constant Details
url="<Your-codeDx-url-detail>"
accessToken="CodeDx Private Access Token"

#polaris Constant Details
polarisUrl = "Polaris Url"
polarisAccessToken = "Polaris Access Token"


#blackDuck Constant Details
blackduckUrl = "BlackDuck Url"
blackduckApiToken = "BlackDuck API Token"

#Jira (issue tracker configuration)
jiraToken = "Jira Token"
jiraUrl = "Jira Url"

with open('Dataset.csv') as csv_file:

    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            #codeDx Project Name
            projectName = row[0]
            #Checking for project status
            if len(row[9]) != 0:
                parentId = projects.isAvailable(url,accessToken,row[9])
            else:
                parentId = None

            id = projects.isAvailable(url,accessToken,row[0])

            if id != None:
                if parentId != None:
                    parentCheck = projects.checkParent(url,accessToken,id)
                    if  parentId != parentCheck:
                        updateParentStatus = projects.updateParent(url,accessToken,id,parentId)
                        if updateParentStatus == 200:
                            print('Parent Updated Successfully')
                if row[6] == '0':
                    deleteStatus = projects.delete(url,id,accessToken)
                    if deleteStatus == 204:
                        print("project "+row[0]+" deleted succesfully")
                        continue
                    else:
                        print("project deletion failed for "+row[0])
                        continue
                else:
                    continue
            elif row[6] != '0':
                # Creation of Project in CodeDx
                createdProject=projects.create(url,accessToken,projectName)
                projectId=createdProject["id"]

                #updating parent
                if not row[9]:
                    print("Updating parent skipped for "+projectName)
                else:
                    updateParentStatus = projects.updateParent(url,accessToken,projectId,parentId)
                    if updateParentStatus == 200:
                        print('Parent Updated Successfully for '+projectName)
                # add git Configuration
                if gitConfig.validateRemote(url,accessToken,row[3],row[4]) == True or gitConfig.validateRemote(url,accessToken,row[3],row[4]) == 'REQUIRES_AUTH':
                    gitConfig.updateGit(url,str(projectId),row[3],row[4],accessToken,row[7],row[8])
                else:
                    print("git Configuration failed")
                    exit()
                if not row[1]:
                    print("Polaris Skipped for "+projectName)
                else:
                    # Creation of blank polaris tool configuration.
                    blankPolarisConfiguration=toolConfig.createBlankPolarisConfiguration(url,str(projectId),accessToken)
                    print(blankPolarisConfiguration)
                    configId=blankPolarisConfiguration["id"]

                    # Getting polaris project value from codeDx
                    populatedPolarisProjectValue=populate.polarisProjects(url,str(configId),polarisAccessToken,polarisUrl,accessToken,row[1])

                    # Editing Polaris tool Configuration
                    editedConfig=toolConfig.editPolarisConfig(url,configId,accessToken,polarisUrl,polarisAccessToken,populatedPolarisProjectValue,"cdx_default_branch")

                    # Check for analysis readyness.
                    ready=analysis.ready(url,projectId,configId,accessToken)

                    if str(ready == 'true'):
                        # Running Analysis for Polaris
                        analysis.begin(url,projectId,configId,accessToken)        
                        print("Polaris Analysis Started for "+projectName)
                    
                    else:
                        print("Polaris Analysis for "+projectName+" Failed")
                    
                if not row[2]:
                    print("BlackDuck Skipped for "+projectName)
                else:    
                    # Creation of black duck blank configuration
                    blankBlackDuckConfiguration=toolConfig.createBlankBlackDuckConfiguration(url,str(projectId),accessToken)
                    bdconfigId=blankBlackDuckConfiguration["id"]

                    # Getting blackduck project value from codeDx
                    populatedBlackduckProjectValue=populate.blackduckProjects(url,str(bdconfigId),blackduckApiToken,blackduckUrl,accessToken,row[2])

                    # Editing BlackDuck tool configuration
                    editedBDConfig=toolConfig.editBlackDuckConfig(url,bdconfigId,accessToken,blackduckUrl,blackduckApiToken,populatedBlackduckProjectValue,"cdx_use_latest_ver")

                    # Check for analysis readyness.
                    bdready=analysis.ready(url,projectId,bdconfigId,accessToken)
                    
                    #Running Analysis for BlackDuck
                    if str(bdready == 'true'):
                        analysis.begin(url,projectId,bdconfigId,accessToken)        
                        print("BlackDuck Analysis Running")
                    else:
                        print("BlackDuck Analysis for "+projectName+" Failed")
                
                #Jira Configuration
                if not row[5]:
                    print("Jira Configuration Skipped for "+projectName)
                else:
                    projectKey = issueTracker.getProjectKey(url,jiraUrl,jiraToken,projectId,accessToken,row[5])
                    print("project Key is "+projectKey)
                    jiraCreationStatus = issueTracker.createJiraConfig(url,projectId,jiraToken,jiraUrl,projectKey,accessToken)
                    if jiraCreationStatus == 200:
                        print('Jira Creation Success')
                    else:
                        print("JiraCreation Failed!!!")
    exit()