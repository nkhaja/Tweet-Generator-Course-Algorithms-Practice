from flask import Flask, request, jsonify, json, render_template
import generator
import os

app = Flask(__name__)

@app.route('/')
def hello():
    tweet_text = generator.main()
    if len(tweet_text) > 140:
        tweet_text = tweet_text[0:139]
    return render_template('tweet.html',tweet_text=tweet_text)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    print(status)
    return redirect('/')

@app.route('/generate', methods=['GET'])
def generate():
    tweet_text = generator.main()
    if len(tweet_text) > 140:
        tweet_text = tweet_text[0:139]
    return render_template('tweet.html',tweet_text=tweet_text)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port=port)
