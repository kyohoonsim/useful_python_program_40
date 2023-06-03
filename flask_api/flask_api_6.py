from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

kings = {
    "1": "태조", "2": "정종", "3": "태종", "4": "세종", "5": "문종", "6": "단종",
    "7": "세조", "8": "예종", "9": "성종", "10": "연산군", "11": "중종", "12": "인종",
    "13": "명종", "14": "선조", "15": "광해군", "16": "인조", "17": "효종", "18": "현종",
    "19": "숙종", "20": "경종", "21": "영조", "22": "정조", "23": "순조", "24": "헌종",
    "25": "철종", "26": "고종",
}

@app.route("/")
def hello_world():
    return "<p>조선시대 왕 이름 API 서비스</p>"

@app.route("/kings", methods=["GET"])
def get_kings():
    res = make_response(jsonify(kings), 200)
    return res

@app.route("/kings/<nth>", methods=["POST"])
def add_king(nth):
    req = request.get_json()

    if nth not in list(kings.keys()):
        kings[nth] = req['name']
        res = make_response(jsonify({"message": "왕이 생성되었습니다."}), 200)
    else:
        res = make_response(jsonify({"error": "이미 존재하는 왕의 번호가 전달되었습니다."}), 400)
    return res

@app.route("/kings/<nth>", methods=["PUT"])
def update_king(nth):
    req = request.get_json()
    print(req)

    if nth in list(kings.keys()):
        kings[nth] = req['name']
        res = make_response(jsonify({"message": "왕이 수정되었습니다."}), 200)
    else:
        res = make_response(jsonify({"error": "없는 번호의 왕입니다."}), 400)
    return res 

@app.route("/kings/<nth>", methods=["DELETE"])
def delete_king(nth):
    if nth in list(kings.keys()):
        del kings[nth]
        res = make_response(jsonify({"message": "왕이 삭제되었습니다."}), 200)
    else:
        res = make_response(jsonify({"error": "없는 번호의 왕입니다."}), 400)
    return res 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)