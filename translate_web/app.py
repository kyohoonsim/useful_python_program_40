from flask import Flask, render_template, request, jsonify, make_response
from googletrans import Translator

app = Flask(__name__)
simpago = Translator()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/translate", methods=['POST'])
def translate():
    req = request.get_json()
    trans_src = req['trans_src']
    print(trans_src)

    trans_dest = simpago.translate(trans_src, dest='en', src='ko')
    print(trans_dest.text)

    res = make_response(jsonify({'result': trans_dest.text}), 200)
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)