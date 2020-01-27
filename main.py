import json
import generater
from flask import Flask
from flask import jsonify, make_response, request, Response
from flask import make_response
from flask import request
from flask import Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

vimrcs = []

@app.route("/generate", methods = ['POST'])
def get_generate_req():
    json = request.get_json()
    UUID = json['uuid']
    INDENT = json['indent']
    COLOR = json['colorscheme']
    USER_NAME = json['user']

    if json['langSettings'] != None:
        LANGU_SETTINGS = json['langSettings']
        vimrc = {
                "name": USER_NAME,
                "uuid": UUID,
                "body": generater.generater(INDENT, COLOR, LANGU_SETTINGS)
                }
    else:
        vimrc = {
                "name":USER_NAME,
                "uuid": UUID,
                "body": generater.generater(INDENT, COLOR, None)
                }

    vimrcs.append({UUID: vimrc})

    return jsonify(vimrc)

if __name__ == "__main__":
    app.run()
