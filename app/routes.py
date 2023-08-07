from flask import render_template, request
from .file_handlers import load_video
from .processors import build_palette
from app import app, STATIC_DIR

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    try: 
        video = load_video(request.files)
        video.save(STATIC_DIR + '/' + video.filename)
        build_palette(STATIC_DIR + '/' + video.filename, 400)
        return render_template('preview.html', video_name = 'final.png')
    
    except Exception as e: 
        return str(e)
