from reportlab.pdfgen import canvas

def generate_pdf(city):

    file="SmartCityReport.pdf"

    c=canvas.Canvas(file)

    c.drawString(100,800,"AI SMART CITY REPORT")

    y=760

    for key,value in city.items():

        c.drawString(100,y,f"{key} : {value}")

        y-=20

    c.save()

    return file