from flask import Flask, render_template, request
from Persistence import *
from ProcessRequest import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        if request.form['buttonType'] == 'submit':
            return processSaveForm(request)

        elif request.form['buttonType'] == 'clearAll':
            return processDeleteAllData()

        elif request.form['buttonType'] == 'delete':
            return processDeleteOneRecord(request)

        elif request.form['buttonType'] == 'retrieveName':
            return processRetrieveName(request)

        elif request.form['buttonType'] == 'retrieveEmail':
            return processRetrieveEmail(request)

    listOfAllData = retrieveAllDataFromShelve()
    return render_template('home.html', listOfAllData=listOfAllData)


if __name__ == '__main__':
    app.run(port='80')
