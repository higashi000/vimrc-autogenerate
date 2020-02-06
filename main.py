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

vimrcs = {}

@app.route("/generate", methods = ['POST'])
def get_generate_req():
    global vimrcs
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

    vimrcs.setdefault(UUID, vimrc)
    f = open('vimrc', 'a')
    f.write(vimrc["name"])
    f.write("\n")
    f.write(vimrc["uuid"])
    f.write("\n")
    f.write(vimrc["body"])
    f.write("\n")
    f.write("\n")
    f.close()

    return jsonify(vimrc)

@app.route("/list", methods = ['GET'])
def vimrc_list():
    vimrc_data = []
    print(vimrcs)
    for i in vimrcs:
        data = {"uuid": i, "name": vimrcs[i]["name"]}
        print(data)
        vimrc_data.append(data)

    data_list = {"inform": vimrc_data}

    print()
    print(data_list)
    print()

    return jsonify(data_list)

@app.route("/result/<vimrc_id>", methods = ['GET'])
def send_vimrc(vimrc_id):
    global vimrcs
    vimrc = vimrcs[vimrc_id]

    return jsonify(vimrc)

if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0')
