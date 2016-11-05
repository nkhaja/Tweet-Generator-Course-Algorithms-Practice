from flask import Flask, request, jsonify, json

app = Flask(__name__)



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
        for item in allTasks:
            if item['id'] == id:
                return jsonify(item)
        return jsonify({"error": "404, No task found with given id"})


    if request.method == 'DELETE' and id != None:
        for item in allTasks:
            if item['id'] == id:
                allTasks.remove(item)
                return jsonify({"response" : "item with id %s was successfully removed" % id})
            else:
                return jsonify({"error": "404, No task found with given id"})


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


@app.route('/lists', methods = ['GET','POST'])
@app.rooute('lists/<list_id>')
def lists(list_id=None):
    dic = request.form.to_dict()
    result = request.form
    jsonResponse = jsonify(result)
    GET = request.method == 'GET'
    POST = request.method == 'POST'
    HAS_LIST = list_id != None

    if GET and !HAS_LIST:
        return jsonify(allLists)


    if GET and :
        return jsonify(allLists)

    if request.method == 'POST':
        try:
            newId = dic['id']
            newTitle = dic['title']
        except KeyError:
            jsonify({"error": "400, You are missing a parameter"})
        for list in allLists:
            if list["id"] = newId:
                return jsonify({"error": "409, A task with this id already exists"})
        allLists.append(dic)
        return jsonResponse



if __name__ == "__main__":
    app.run()
