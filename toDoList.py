from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route('')
def index():
    return "Welcome!"

storage = {}
@app.route("/tasks/<id>", methods = ['GET','POST']
def tasks(id=None):
dic = request.form.to_dict()
    ## GET a specific task if given existing id (if exists), else give all tasks
    if request.method == 'GET':
        if id != None:
            try: output = storage[id] ## CHANGE when storage method decided
            except:return jsonify({"error": "No task with that id in storage"})
        return jsonify(output)

    if request.method == 'GET' && id != None:
        try:
            output = storage[id] ## may need to change this
        except KeyError:
            return jsonify({"error": "No task with that id in storage"})
        return output
    else:
        return storage


    if request.method == 'POST':
        try:
            taskText = dic["text"]
