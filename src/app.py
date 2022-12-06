import onnxruntime as ort
from flask import Flask, jsonify, request
from common import detect

app = Flask(__name__)

MODEL_FILE_PATH = "src/model/yolov7.onnx"

CUDA_MODE = False

IMG_SIZE = 640

providers = ['CUDAExecutionProvider',
             'CPUExecutionProvider'] if CUDA_MODE else ['CPUExecutionProvider']
model = ort.InferenceSession(MODEL_FILE_PATH, providers=providers)


@app.route('/api/detectImage', methods=['POST'])
def detectImage():
    if(request.files):
        binary_file = request.files.get("image_file").read()
        result = detect(model=model, img=binary_file, img_size=IMG_SIZE)
    return jsonify(result)


if __name__ == '__main__':
    settings = {
        "host": '0.0.0.0',
        "port": 9999,
        "debug": False,
        "use_reloader": False
    }
    app.run(**settings)
