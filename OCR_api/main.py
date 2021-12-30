from flask import Flask, request, redirect, url_for, render_template
# from werkzeug.utils import secure_filename
import utils

UPLOAD_FOLDER = 'upload/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    if filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

@app.route('/upload')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'my_file' not in request.files:
            return redirect(request.url)
        file = request.files['my_file']
        print(f'This is file {file}')
        file_name = file.filename
        print(f'This is filename {file_name}')
        print(f'This is request.file {request.files}')
        print(f'This is {request.method}')
        if file_name == '':
            return redirect(request.url)
        if file and allowed_file(file_name):
            utils.show_img(file, file_name)
            return redirect('/upload')




if __name__ == '__main__':
    app.run(debug=True)