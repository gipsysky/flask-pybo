from flask import Blueprint, request, jsonify, render_template
import easyocr
import os

bp = Blueprint('ocr', __name__, url_prefix='/ocr')

reader = easyocr.Reader(['en', 'ko'])  # 한국어/영어 지원

@bp.route('', methods=['POST'])
def ocr_capture():
    file = request.files['file']
    if not file:
        return jsonify({"error": "no file"}), 400

    temp_path = os.path.join("uploads", file.filename)
    file.save(temp_path)

    results = reader.readtext(temp_path)
    text = " ".join([res[1] for res in results])

    return jsonify({"text": text})



@bp.route('/scan')
def scan():
    return render_template('ocr/scan.html')