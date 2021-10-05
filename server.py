from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)


@app.route('/randomWord', methods=['GET'])
def getRandomWord():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    WORDS = list(map(lambda word: word.decode('UTF-8'), WORDS))
    # alternatively WORDS = [x.decode('utf-8') for x in WORDS]

    args = request.args
    if "contains" in args:
        contains = args["contains"]
        WORDS = list(filter(lambda word: contains in word, WORDS))
        if not WORDS:
            WORDS = ["error"]
        # alternatively WORDS = [word for word in WORDS if contains in word]

    randomWord = random.choice(WORDS)

    return jsonify({"word": randomWord})


if __name__ == "__main__":
    app.run(debug=True)
