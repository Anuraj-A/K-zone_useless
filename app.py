from flask import Flask, render_template, request
import os
from utils import classify_pothole

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    filename = None

    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            result = classify_pothole(filepath)
            filename = file.filename

    return render_template('index.html', result=result, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
