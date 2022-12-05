from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/api/detectImage', methods=['POST'])
def detectImage():
    if(request.files):
        binary_file = request.files.get("image_file").read()
    return "Hello"


if __name__ == '__main__':
    settings = {
        "host": '0.0.0.0',
        "port": 9999,
        "debug": True,
        "use_reloader": True
    }
    app.run(**settings)
