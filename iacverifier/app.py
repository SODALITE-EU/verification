import os
from pathlib import Path

import requests
from flask import Flask, json, request, Response
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/verifier/{iactype}/file', methods=['POST'])
def detect_errors(iactype):
    home = str(Path.home())
    soda_home = os.path.join(home, ".sodalite")
    if not os.path.exists(soda_home):
        os.makedirs(soda_home)

    if 'file' not in request.files:
        return json.dumps({'message': 'No file part in the request'}, sort_keys=False, indent=4), 400

    file = request.files['file']

    if file.filename == '':
        return json.dumps({'message': 'No file selected for uploading'}, sort_keys=False, indent=4), 400
    else:
        filename = secure_filename(file.filename)
        file_path = os.path.join(soda_home, filename)
        file.save(file_path)
        res = verify(file_path, iactype)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("The file does not exist to be removed")
        return res


def verify(file_path, iactype):
    if iactype == 'tosca':
        url = 'http1://tosca-syntax:5001/errors/tosca/file'
    else:
        url = 'http1://ansible-workflow:5002/errors/workflow/file'
    files = {'file': open(file_path, 'rb')}
    r = requests.post(url, files=files)
    js = json.dumps(r.json(), sort_keys=False, indent=4)

    resp = Response(js, status=200, mimetype='application/json')
    return resp


app.run(host='0.0.0.0', port=5000)
