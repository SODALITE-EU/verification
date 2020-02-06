import os
from pathlib import Path

from flask import Flask, json, request, Response
from werkzeug.utils import secure_filename

from pnmlpy import WorkflowVerifier

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/errors/workflow/file', methods=['POST'])
def detect_errors():
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
        res = verify(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("The file does not exist to be removed")
        return res


def verify(file):
    errors = WorkflowVerifier.run_verifier(file)
    js = json.dumps(errors, sort_keys=False, indent=4)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST'
    resp.headers['Access-Control-Max-Age'] = '1000'
    return resp


app.run(host='0.0.0.0')
