from flask import Blueprint, url_for, render_template, request
from werkzeug.utils import redirect

import easyocr
import cv2
import os

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo! (view)'


@bp.route('/')
def index(): 
    return redirect(url_for('question._list'))
    
    

# OCR Reader (한국어+영어)
reader = easyocr.Reader(['ko', 'en'], gpu=False)



@bp.route('/upload_ocr_form', methods=['GET', 'POST'])
def ocr_page():
    text_result = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join("uploads", file.filename)
            file.save(filepath)

            # 이미지 읽기
            image = cv2.imread(filepath)

            # OCR 실행
            results = reader.readtext(image)
            text_result = [text for (_, text, prob) in results]

    return render_template("ocr_result.html", results=text_result)
    
    