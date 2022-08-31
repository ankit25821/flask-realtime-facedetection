from flask import Flask, render_template
from flask_socketio import SocketIO, emit


from utils import (
    base64_to_np_array,
    np_array_to_base64_image
)

from detection import detect_face


app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins='*')


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on('image')
def get_image(request):
    image = base64_to_np_array(request)
    detected_face = detect_face(image)
    imageData = np_array_to_base64_image(detected_face).decode('utf-8')
    b64_src = 'data:image/jpeg;base64,'
    stringData = b64_src + imageData
    emit("response_back", {'image_data': stringData})


if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)
