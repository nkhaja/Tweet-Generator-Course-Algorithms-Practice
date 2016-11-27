from flask import Flask, request, jsonify, json


app = Flask(__name__)

### MARK: functions for operations on lists alone ###

# returns array of every list name
#allLists is an array of all Lists stored
def getListNames(allLists):
    listNames = []
    for someList in allLists:
        listNames.append(someList["title"])
    return listNames




#Checks allList array for lists' existence
# @ id the id of the list
# @ allLists an array of all lists stored
def listExists(id, allLists):
    for someList in allLists:
        if someList["id"] == id:
            return someList
        else:
            return None

# checks the post has all properly formatted parameters
# @ dict -- a dictionary representing the post request
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


### MARK: Functions for working on tasks ###

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

    # Get all Tasks
    if request.method == 'GET' and id == None:
        return jsonify(allTasks)

    # Get task with a specific id
    if request.method == 'GET' and id !=None:
        return getTask(allTasks, id)

    # Delete a specific task
    if request.method == 'DELETE' and id != None:
        return deleteTask(id, allTasks)

    # Need to specify id to delete tasks
    if request.method == 'DELETE' and id == None:
        return jsonify({"error": "404, Please specify a task to delete"})

    # Make a post if properly formatted, else return error
    # Also ensures that post with same id doesn't already exist
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


    if POST:
        checkValidListPost(dic) # program stops here if not valid
        allLists.append(dic)
        return jsonResponse

    if PUT:
        return updateListWithId(allLists, id, dic)

    if DELETE:
        return deleteList(allLists, id)

@app.route('/lists/<list_id>/tasks', methods = ['GET','POST', 'PUT'])
def allTasksFromList(list_id):
    dic = request.form.to_dict()
    result = request.form
    jsonResponse = jsonify(result)
    GET = request.method == 'GET'
    POST = request.method == 'POST'
    PUT = request.method == 'PUT'

    if GET:
        requestedList = listExists(list_id, allLists)













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
