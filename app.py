from flask import Flask
from flask import render_template
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

app = Flask(__name__,template_folder='src/templates',static_folder='src/static')


@app.route('/')
def hello():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)