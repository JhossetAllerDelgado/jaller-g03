"""Importando los modulos"""
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reporlab.lib import colors

"""Inicializando las variables con valores"""
filename = "reporte.pdf"
documentTitle = "Reporte"
title = "Python"
subtitle = "lo primordial"
textLine = [
    'La tecnologia nos hace concientes'
    'El mundo alrededor de nosotros'
]
image = 'image.pdf'
"""creando un objeto pdf"""
pdf = canvas.Canvas(filename)
"""Estableciendo el titulo del documento pdf"""
pdf.setTitle(documentTitle)

"""agregamos una fuente externa de python"""
pdfmetrics.registerFont(
    TTFont('abc', "SakBunderan.ttf")
)





