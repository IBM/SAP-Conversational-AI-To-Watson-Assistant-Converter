# SAP-Conversational-AI-To-Watson-Assistant-Converter

This project includes a convertor which is basically a python script that can convert SAP CAI project to Watson Assistant project.

Writing an entire chatbot on a new system needs lot of efforts, hence this convertor is implemented with the purpose of making this process semi-automated.

# Prerequisite

- A latest version of python needs to be installed.
(Version used for creating this tutorial was Python 3.10.8)

At present the convertor supports converting
1.	Intents
2.	Entities
3.	Basic Skill structure (Dialog in Watson Assistant)
4.	Main webhook

# SAP CAI Project Structure:

This tutorial focuses on a simple chatbot and the images shown below can be used as a reference for actual CAI chatbot.
Login to SAP CAI and select the chatbot project which needs to be migrated.
Website: https://cai.tools.sap

Intents:

![intentSAP](example/images/intentssap.png)

Entities:

![entitySAP](example/images/entitiessap.png)

Skills:

![skillSAP](example/images/skillssap.png)

# Export and download Project.

- Click on the export button as shown in the image below to export the CAI chatbot

![projectexportSAP](example/images/projectexportsap.png)

- Once the export process is completed we can download the project to our system

![projectdownloadsap](example/images/projectdownloadsap.png)

# Edits to be done in convertor script:

Step 1: Open the File convertor.py

Step 2: In mainFun(), replace inputFileLoc with the absolute path of the root directory for SAP CAI project which was downloaded previously.

Ex. inputFileLoc = “/users/Downloads/SAPCAI-project”

Similarly mention the outputFileLoc with the absolute path where the converted watson assistant project needs to be saved.

Ex. outputFileLoc = “/users/Downloads”

![pythonfilechange](example/images/pythonfilechange.png)

Step 3: On the terminal(or the preferred IDE) execute the python script.

$ python3 convertor.py

Output file for Watson Assistant project is now generated.

![outputfile](example/images/outputfile.png)

# Watson Assistant:

Step 1: Login to IBM cloud and create a Watson Assistant instance.

Step 2: Launch the Watson assistant.

Since this is an empty project there won’t be any intent, entity or dialog available.

Intent:

![emptyintentWA](example/images/emptyintentWA.png)

Entity:

![emptyentityWA](example/images/emptyentityWA.png)

Dialog:

![emptydialogsWA](example/images/emptydialogsWA.png)

- Click on upload/download and select the file which was created as an output by convertor.

![selectgeneratedfileWA](example/images/selectgeneratedfileWA.png)

- Press upload button, then press upload and replace.

![pressuploadWA](example/images/pressuploadWA.png)

![uploadandreplaceWA](example/images/uploadandreplaceWA.png)

- If successfully uploaded, we will get status as shown in the image below.

![successfullyuploaded](example/images/successfullyuploaded.png)

# Let us check if data is migrated successfully.

Intents:

![intentmigratedWA](example/images/intentmigratedWA.png)

Entities:

![entitiesmigratedWA](example/images/entitiesmigratedWA.png)

Dialog:

![dialogmigratedWA](example/images/dialogmigratedWA.png)

Webhook:

![webhooksmigratedWA](example/images/webhooksmigratedWA.png)

# Summary

This completes the tutorial on how to use the convertor script provided in this repo to migrate some of the components directly to Watson Assistant.

# Next Steps

As next steps this project can now be used as a base to build and add more features on top of it to create chatbots of different use case.

Watson Assistant Documentation:

https://cloud.ibm.com/docs/assistant?topic=assistant-getting-started


