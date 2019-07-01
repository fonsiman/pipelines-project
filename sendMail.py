import smtplib
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

def sendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = ImgFileName
    msg['From'] = gmail_user
    msg['To'] = input("Who should receive the mail? ")

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        print("Connected to gmail servers")
    except:  
        print("Something went wrong...")

    # Send the mail to SMTP gmail server
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.close()