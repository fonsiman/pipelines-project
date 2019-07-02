# Función para enviar un correo con un pdf adjunto

import smtplib
import email
import email.mime
import email.mime.application
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

if not "GMAIL_MAIL" in os.environ:
    raise ValueError("Hay un fallo con la cuenta del correo.")

if not "GMAIL_KEY" in os.environ:
    raise ValueError("Hay un fallo con el password del correo.")

gmail_user = os.environ["GMAIL_MAIL"]
gmail_password = os.environ["GMAIL_KEY"]

def sendMail(FileName):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    msg = MIMEMultipart()
    msg['Subject'] = "Informe" + FileName
    msg['From'] = gmail_user
    msg['To'] = input("¿Dónde enviamos el correo? ")

    html = """\
        <html>
        <head></head>
        <body>
            <p>Buenas tardes,</p>
            <p>Adjunto a este correo encontrarás un informe de la empresa seleccionada.</p>
            <p><em>Alfonso ROMÁN</em></p>
        </body>
        </html>
        """
    text = MIMEText(html, 'html')
    msg.attach(text)
    filename1 = dir_path+"/outputs/"+FileName
    fp = open(filename1 , 'rb')
    attach_part = email.mime.application.MIMEApplication(fp.read(),"pdf")
    fp.close()

    attach_part.add_header('Content-Disposition','attachment',filename = FileName)
    msg.attach(attach_part)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        print("Conectado al servidor de gmail")
    except:  
        print("Opps! Algo falló...")

    # Send the mail to SMTP gmail server
    if server.sendmail(msg['From'], msg['To'], msg.as_string()) == {}:
        print("Mensaje enviado correctamente")

    server.close()