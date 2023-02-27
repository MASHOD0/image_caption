
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from Model import predict
from flask import send_from_directory


UPLOAD_FOLDER = r'C:\Users\mashh\Documents\git\listed_image_caption\uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')
        file = request.files['file']
        num_return_sequnces = request.form['num_return_sequnces']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        results = predict(os.path.join(app.config['UPLOAD_FOLDER'], filename), num_return_sequnces=num_return_sequnces)
        return render_template('answer.html', results=results, image_src = os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        return render_template('index.html')
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run()