from flask import request, render_template
from Persistence import *

def processSaveForm(request):
    email = request.form['email']
    name = request.form['name']

    listOfAllData = retrieveAllDataFromShelve()

    if len(email) == 0 or len(name) == 0:
        return render_template('home.html', returnMsg="Email and/or Name missing")

    result = saveToShelve(email, name)
    if result:
        listOfAllData = retrieveAllDataFromShelve()
        return render_template('home.html', returnMsgForSave="Saved successfully", listOfAllData=listOfAllData)
    else:
        return render_template('home.html', returnMsgForSave="Email already exists", listOfAllData=listOfAllData)

def processDeleteAllData():
    deleteAll()
    return render_template('home.html', returnMsgForDeleteAll="Deleted successfully")

def processDeleteOneRecord(request):
    if deleteOneRecord(request.form['email']):
        returnMsgForDelete="Record Deleted"
    else:
        returnMsgForDelete = "Record not Deleted"
    listOfAllData = retrieveAllDataFromShelve()
    return render_template('home.html', returnMsgForDelete=returnMsgForDelete, listOfAllData=listOfAllData)


def processRetrieveName(request):
    listOfAllData = retrieveAllDataFromShelve()
    retrieveName = retrieveDataUsingEmail(request.form['email'])

    returnMsg = None
    if retrieveName == None:
        returnMsg = "Email not found"
        return render_template('home.html', returnMsgForRetrieveName=returnMsg, listOfAllData=listOfAllData)

    return render_template('home.html', returnMsgForRetrieveName=returnMsg, listOfAllData=listOfAllData,
                           retrieveName=retrieveName)

def processRetrieveEmail(request):
    listOfAllData = retrieveAllDataFromShelve()
    retrieveEmail = retrieveDataUsingName(request.form['name'])

    returnMsg = None
    if retrieveEmail == None:
        returnMsg = "Email not found"
        return render_template('home.html', returnMsgForRetrieveEmail=returnMsg, listOfAllData=listOfAllData)

    return render_template('home.html', returnMsgForRetrieveEmail=returnMsg, listOfAllData=listOfAllData,
                           retrieveEmail=retrieveEmail)

