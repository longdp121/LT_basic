from flask import Flask, render_template, Response, request
import cv2 as cv
from cameraCV import cam, save_photo

app = Flask(__name__)
camera = cv.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(cam(camera), mimetype = 'multipart/x-mixed-replace; boundary=transfer_frame')

@app.route('/request', methods = ['POST', 'GET'])
def control():
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            save_photo(camera)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)