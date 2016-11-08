from flask import Flask, request, jsonify, json

app = Flask(__name__)

### MARK: functions for operations on lists alone ###
def getListNames(allLists):
    listNames = []
    for someList in allLists:
        listNames.append(someList["title"])
    return listNames

def listExists(id, allLists):
    for someList in allLists:
        if someList["id"] == id:
            return someList
        else:
            return None


def checkValidListPost(someDict):
    try:
        newId = someDict['id']
        newTitle = someDict['title']
    except KeyError:
        return jsonify({"error": "400, You are missing a parameter"})
    for someList in allLists:
        if someList["id"] = newId:
            return jsonify({"error": "409, A task with this id already exists"})
    return

def updateListWithId(allLists, id, dic): # allLists might be optional once hooked to Mongo
    someList = listExists
    for someList in allLists:
        if someList['id'] == id:
            someList['title'] = dic['title']
            return jsonify({"repsonse": "List with id %s successfully updated" % id})
        return jsonify({"error": "404, No list found with given id"})

def deleteList(allLists, id):
    targetIndex = 0
    for someList in allLists:
        targetIndex = targetIndex + 1
        if someList[id] == id:
            targetIndex = targetIndex - 1
            break
    if targetIndex == len(someList):
        someList.pop(targetIndex)
        return jsonify({"response": "list with id %s successfully deleted" % id})
    else:
        return jsonify({"error": "404, No list found with given id"})


### Mark Functions for working on tasks ###

def getTask(id, allTasks):
    for item in allTasks:
        if item['id'] == id:
            return jsonify(item)
    return jsonify({"error": "404, No task found with given id"})

def deleteTask(id, allTasks):
    for item in allTasks:
        if item['id'] == id:
            allTasks.remove(item)
            return jsonify({"response" : "item with id %s was successfully removed" % id})
        else:
            return jsonify({"error": "404, No task found with given id"})


### ROUTES ###

@app.route('/')
def index(item=None):
    if item == None:
        return "Welcome!"

allLists []
allTasks = []

@app.route("/tasks", methods = ['GET','POST'])
@app.route("/tasks/<id>", methods = ['GET', 'DELETE'])
def tasks(id=None):
    dic = request.form.to_dict()
    result = request.form
    jsonResponse = jsonify(result)

    if request.method == 'GET' and id == None:
        return jsonify(allTasks)

    if request.method == 'GET' and id !=None:
        return getTask(allTasks, id)

    if request.method == 'DELETE' and id != None:
        return deleteTask(id, allTasks)



    if request.method == 'DELETE' and id == None:
        return jsonify({"error": "404, No task found with given id"})


    if request.method =='POST':
        try:
            newId = dic['id']
            taskText = dic['text']
        except KeyError:
            jsonify({"error": "400, You are missing a parameter"})


        for task in allTasks:
            if newId == task['id']:
                return jsonify({"error": "409, A task with this id already exists"})
        allTasks.append(dic)
        return jsonResponse


@app.route('/lists', methods = ['GET','POST', 'PUT'])
@app.route('/lists/<list_id>', methods = ['GET','POST', 'PUT'])

def lists(list_id=None):
    dic = request.form.to_dict()
    result = request.form
    jsonResponse = jsonify(result)
    GET = request.method == 'GET'
    POST = request.method == 'POST'
    PUT = request.method == 'PUT'
    DELETE = request.method == 'DELETE'
    HAS_LIST = list_id != None

    if GET and !HAS_LIST:
        return getListNames()

    if GET and HAS_LIST:
        someList = listExists(id, allLists)
        if someList:
            return someList
        else:
            jsonify({"error": "404, No list found with given id"})


    if request.method == 'POST':
        checkValidListPost(dic) # program stops here if not valid
        allLists.append(dic) # move
        return jsonResponse

    if PUT:
        return updateListWithId(allLists, id, dic)

    if DELETE:
        return deleteList(allLists, id)

@app.route('/lists/<list_id>/tasks', methods = ['GET','POST', 'PUT'])
@app.route('/lists/<list_id>/tasks/<task_id>', methods = ['GET','POST', 'PUT'])
def tasksForList(list_id = None, task_id = None):
        dic = request.form.to_dict()
        result = request.form
        jsonResponse = jsonify(result)
        GET = request.method  == 'GET'
        POST = request.method == 'POST'
        PUT = request.method  == 'PUT'
        DELETE = request.method == 'DELETE'
        HAS_LIST = list_id != None







if __name__ == "__main__":
    app.run()
