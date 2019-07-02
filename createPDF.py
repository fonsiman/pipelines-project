
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import os
    
def createPDF(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    ancho, alto=A4 
    c=canvas.Canvas(dir_path+"/outputs/"+file_name+".pdf", pagesize=A4)                      

    text1=c.beginText(50, 465)           
    text1.setFont("Times-Roman", 15)     

    text2=c.beginText(50, 310)           
    text2.setFont("Times-Roman", 15)     

    text3=c.beginText(50, 160)           
    text3.setFont("Times-Roman", 15)     

    c.drawImage( dir_path+"/outputs/"+file_name+"-plot.png", 0, 495, width=600, height=350)   
    text1.textLine("Cuenta de resultados")
    c.drawImage( dir_path+"/outputs/"+file_name+"-resultados.png", 0, 295, width=600, height=225)  
    text2.textLine("Balance")
    c.drawImage( dir_path+"/outputs/"+file_name+"-balance.png", 0, 150, width=600, height=225) 
    text3.textLine("Plantilla")
    c.drawImage( dir_path+"/outputs/"+file_name+"-plantilla.png", 0, 0, width=600, height=225)

    c.drawText(text1)
    c.drawText(text2)
    c.drawText(text3) 
    c.showPage()                 
    c.save()

    return file_name+".pdf"