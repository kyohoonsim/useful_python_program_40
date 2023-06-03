from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

kings = {
    1: "태조", 2: "정종", 3: "태종", 4: "세종", 5: "문종", 6: "단종",
    7: "세조", 8: "예종", 9: "성종", 10: "연산군", 11: "중종", 12: "인종",
    13: "명종", 14: "선조", 15: "광해군", 16: "인조", 17: "효종", 18: "현종",
    19: "숙종", 20: "경종", 21: "영조", 22: "정조", 23: "순조", 24: "헌종",
    25: "철종", 26: "고종",
}

@app.route("/")
def hello_world():
    return "<p>조선시대 왕 이름 API 서비스</p>"

@app.route("/kings", methods=["GET"])
def get_kings():
    res = make_response(jsonify(kings), 200)
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)