from flask import Flask, jsonify
import requests
import random

app = Flask(__name__)


@app.route('/randomWord', methods=['GET'])
def getRandomWord():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    randomWord = random.choice(WORDS).decode('UTF-8')

    return jsonify({"word": randomWord})


if __name__ == "__main__":
    app.run(debug=True)
