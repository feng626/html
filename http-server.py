import os
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/usr/share/nginx/logs/'


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        path = app.config['UPLOAD_FOLDER'] + request.form['file_path']
        file = request.files['file_name']
        if not os.path.exists(path):
            os.mkdir(path)
        if file:
            file.save(os.path.join(path, file.filename))
    return jsonify({'code': 200, 'message': 'success'})


if __name__ == '__main__':
    app.run()
