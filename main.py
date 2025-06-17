import time
import svgwrite
import json
from fpdf import FPDF

before_json = time.time()
with open("resources/merged.json", 'r') as file:
    dictionary = json.load(file)
after_json = time.time()
time_json = (after_json - before_json)

array = dictionary['我'].get('strokes')
dwg = svgwrite.Drawing('output.svg', size=(1024, 1024), profile='tiny')
dwg.viewbox(0, 0, 1024, 1024)
for stroke in array:
    dwg.add(dwg.path(stroke, stroke='black', fill='black', transform="scale(1, -1) translate(0, -1024)"))
dwg.save()

pdf = FPDF()
pdf.add_page()
pdf.image("output.svg")
pdf.output("output.pdf")

