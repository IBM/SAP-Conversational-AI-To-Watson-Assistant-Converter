#
#
# mainFun() will be run when you execute this file
# Write absolute path of the SAP CAI Project at inputFileLoc.
# Write absolute path for saving the output Wastson Assistant project
# Output will be a JSON project file.
#
#

#IMPORTS
import json

#Common Function to read the JSON files of SAP CAI project
#
#input: fileName to read
#
#output: json dict
#
def loadJson(fileName):
    with open(fileName) as filePointer:
        jsonVariable = json.load(filePointer)
    return jsonVariable

#This Function checks for all intent and converts to 
#Watson Assistant Format
#
#input: file location for SAP CAI project
#
#output: dict with all intents
#
def createIntents(inputFileLoc):
    intentDict = {}
    fileURL = inputFileLoc + "/train/datasets-0.json"
    cai_intentJson = loadJson(fileURL)
    intentDict["intents"] = []  
    for intents in cai_intentJson["intents"]:
        inIntentDict = {}
        inIntentDict["intent"] = intents["slug"]
        inIntentDict["examples"] = []
        for example in cai_intentJson["expressions"]:
            if example["intent_id"] == intents["position"]:
                exampleDict = {}
                exampleDict["text"] = example["source"]
                inIntentDict["examples"].append(exampleDict)
        intentDict["intents"].append(inIntentDict)
    return intentDict 

#This function check for all the entities and converts 
#to Watson Assistant format
#
#input: file location for SAP CAI project
#
#output: dict with all the entities
#
def createEntity(inputFileLoc):
    entityDict = {}
    fileURL = inputFileLoc + "/train/datasets-0.json"
    cai_entityJson = loadJson(fileURL)
    entityDict["entities"] = []
    for entity in cai_entityJson["entities"]:
        inEntityDict = {}
        inEntityDict["entity"] = entity["slug"]
        inEntityDict["values"] = []
        entityDict["entities"].append(inEntityDict)
    return entityDict

#Watson Assistant supports only one main webhook
#This function fetches main webhook
#
#input: file location for SAP CAI project
#
#output: dict with main webhook
#
def webhookDict(inputFileLoc):
    webHookDict = {}
    fileURL = inputFileLoc + "/bc/bc.json"
    cai_webhookJson = loadJson(fileURL)
    webHookDict["webhooks"] = []
    for urls in  cai_webhookJson["bot_versions"][0]["web_requests"]:
        inWebHookDict = {}
        inWebHookDict["url"] = urls["url"]
        inWebHookDict["headers"] = []
        inWebHookDict["name"] = "main_webhook"
        webHookDict["webhooks"].append(inWebHookDict)
    return webHookDict

#This function creates a dialog structure only for the main skills
#available in SAP CAI. All child skills would need to be created 
#manually post the project file is uploaded.
# 
#input: file location for SAP CAI project
# 
#output: list of all the skills
#  
def createDialog(inputFileLoc):
    majorNodevalue = 1
    minorNodeValue = 1682939201807
    previousNode = "Welcome" 
    skills = []
    fileURL = inputFileLoc + "/csr/csr.json"
    cai_SkillsJson = loadJson(fileURL)
    for skill in cai_SkillsJson["bot_versions"][0]["skills"]:
        dialogJson = {}
        dialogJson["type"] = "standard"
        dialogJson["title"] = skill["name"]
        condition = skill["in_condition"]["children"][0]["children"][0]["left"][0]["value"]
        dialogJson["conditions"] = condition.replace("@","#")
        dialogJson["dialog_node"] = "node_"+str(majorNodevalue)+"_"+str(minorNodeValue)
        dialogJson["previous_sibling"] = previousNode
        skills.append(dialogJson)
        previousNode = "node_"+str(majorNodevalue)+"_"+str(minorNodeValue)
        minorNodeValue += 1   
    anythingElseNode = {"type": "standard","title": "Anything else","output": {"generic": [{"values": [{"text": "I didn't understand. You can try rephrasing."},{"text": "Can you reword your statement? I'm not understanding."},{"text": "I didn't get your meaning."}],"response_type": "text","selection_policy": "sequential"}]},"conditions": "anything_else","dialog_node": "Anything else","previous_sibling": previousNode,"disambiguation_opt_out": True}
    skills.append(anythingElseNode)
    return skills

#This function creates the entire JSON project for Watson Assistant
#All necessary information currently supported are gathered from files
#
#input: file location for SAP CAI project
#
#output: dict of entire project
#
def genericDict(inputFileLoc):
    projectDict = {}
    retIntent = createIntents(inputFileLoc)
    projectDict["intents"] = retIntent["intents"]
    retEntity = createEntity(inputFileLoc)
    projectDict["entities"] = retEntity["entities"]
    projectDict["metadata"] = {}
    projectDict["metadata"]["api_version"] = {}
    projectDict["metadata"]["api_version"]["major_version"] = "v2"
    projectDict["metadata"]["api_version"]["minor_version"] = "2018-11-08"
    retWebhook = webhookDict(inputFileLoc)
    projectDict["webhooks"] = retWebhook["webhooks"]
    projectDict["counterexamples"] = []
    projectDict["learning_opt_out"]= False
    projectDict["language"]= "en"
    projectDict["description"]= "created for assistant"
    projectDict["name"]= "get flight name import-dialog"
    projectDict["dialog_nodes"] = [{"type": "standard","title": "Welcome","output": {"generic": [{"values": [{"text": "Hello. How can I help you?"}],"response_type": "text","selection_policy": "sequential"}]},"conditions": "welcome","dialog_node": "Welcome"}]
    retDialogs = createDialog(inputFileLoc)
    for dialog in retDialogs:
        projectDict["dialog_nodes"].append(dialog)
    return projectDict

# This is the main function for this convertor
#It creates JSON project after collecting the data 
#from various SAP CAI project files and converted them to 
#watson assistant project. 
#
#input none
#
#output: Saves watson assistant project file to the respective location
def mainFun():
    inputFileLoc = "<Absolute path to the SAP CAI project root directory>"
    outputFileLoc = "<Absolute path to save the output JSON Watson Assistant Project>"
    retGen = genericDict(inputFileLoc)
    json_string = json.dumps(retGen)
    with open(outputFileLoc+"/WatsonAssistant_Project.json", "w") as outfile:
        outfile.write(json_string)
    return True

if __name__ == "__main__":
    mainFun()
