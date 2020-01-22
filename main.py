import json
from flask import Flask, jsonify, make_response, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods = ['POST'])
def generate_vimrc():
    json = request.get_json()
    DATA = json['data']
    vimrc = {\
            "data": DATA\
            }

    return jsonify(vimrc)

if __name__ == "__main__":
    app.run()
