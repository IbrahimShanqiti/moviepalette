import os
from flask import Flask

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

app = Flask(
    __name__, 
    template_folder=os.path.join(ROOT_DIR, 'templates'), 
    static_folder=STATIC_DIR, 
    static_url_path='/static/'
)

import app.routes

if __name__ == '__main__':
    app.run(debug=True)