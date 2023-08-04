from flask import Flask, render_template, request
from .file_handlers import load_video
from .processors import build_palette


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try: 
        video = load_video(request.files)
        video.save('static/' + video.filename)
        build_palette('static/' + video.filename, 400)
        return render_template('preview.html', video_name = 'final.png')
    
    except Exception as e: 
        return e.message()

if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True)
     