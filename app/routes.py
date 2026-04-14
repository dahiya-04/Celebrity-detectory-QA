from flask import Blueprint, render_template,request, redirect
from app.utils.image_handlers import process_image
from app.utils.qa_engine import QAEngine
from app.utils.celebrity_detector import CelebrityDetector

import base64

main = Blueprint('main', __name__)

celebrity_detector = CelebrityDetector()
qa_engine = QAEngine()
@main.route('/', methods=['GET', 'POST'])

def index():
    player_info = " "
    result_img_data = ""
    user_question = ""
    answer = ""

    if request.method == 'POST':
        if 'image' in request.files:
            image_file = request.files['image']
            
            if image_file:
                image_bytes, face_coords = process_image(image_file)

                if face_coords is not None:
                    result_img_data = base64.b64encode(image_bytes).decode('utf-8')
                    player_info = celebrity_detector.identify(image_bytes)
                else:
                    player_info = "No face detected. Please try another image."
            elif 'question' in request.form:
                user_question = request.form['question']
                player_name = request.form['player_name']
                answer = qa_engine.ask_about_celebrities(player_name, user_question)
    return render_template(
        'index.html',
        player_info=player_info,
        result_img_data=result_img_data,
        user_question=user_question,
        answer=answer
    )
            
        