from flask import Flask, request, jsonify, json
import corpus_processing

app = Flask(__name__)

@app.route('/')
def hello():
    return corpus_processing.generateSentence()

if __name__ == "__main__":
    app.run()
