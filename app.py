from flask import Flask, request, render_template
from flask_mail import Mail, Message
import os

mail = Mail()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/educacion', methods=['GET', 'POST'])
def educacion():
    return render_template('educacion.html')

@app.route('/experiencia', methods=['GET', 'POST'])
def experiencia():
    return render_template('experiencia.html')

@app.route('/proyectos', methods=['GET', 'POST'])
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    return render_template('contacto.html')        

#Metodo para enviar correos


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME']='programacionbluehat@gmail.com'
app.config['MAIL_PASSWORD']= 'wbxhbkhtrwdlawwh'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app) 

def send_email(to, subject, message, email):
    msg = Message(subject, recipients=[to, email], sender=to)
    msg.body = message
    mail.send(msg)

@app.route('/send', methods=['POST'])
def send():
    # obtener los datos del formulario
    to = "programacionbluehat@gmail.com"
    subject = "Solicitud_ProgramacionBlueHat"
    name = request.form["name"]
    tel = request.form["tel"]
    email = request.form["email"]
    message_r = request.form['message']
   
    message = "Nombre: "+name+"\nTel: "+ tel + "\nCorreo: " + email + "\n" + message_r


    # enviar el correo electrónico
    send_email(to, subject, message, email)

    return render_template('contacto.html') 



if __name__ == '__main__':
    app.run(debug=True)
       