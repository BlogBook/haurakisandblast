from flask import Flask,request
from flask import render_template
import os,sys
from flask_mail import Mail, Message


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

app = Flask(__name__,template_folder='src/templates',static_folder='src/static')



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'support@thegeeks.co.nz'
app.config['MAIL_PASSWORD'] = 'support@thegeeks.co.nz'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/message',methods=['POST'])
def message():
    if request.method =='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        item = request.form.get('item')
        subject = request.form.get('subject')
        msg = Message('Hello', sender = 'support@thegeeks.co.nz', recipients = ['dave@haurakisandblasting.co.nz'])
        msg.body = "New message from User"
        msg.html="Name: "+name+"<br> Email: "+email+"<br> Number: "+number+"<br> Hear about us:"+item+"<br> Detail:"+subject
        mail.send(msg)
        return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
