# importing libraries
from fpdf import FPDF 
import pandas as pd
# importing modules
from table import * # calls functions by their names `tableValues()`
# import table      # calls functions with module name `table.tableValues()`
from makepretty import fit_word
# importing variables
from data import data, european_countries
from config import font_type_table_header, font_type_table_body, black, green, yellow

# PyFPDF documentation
# https://pyfpdf.readthedocs.io/en/latest/index.html

#################################################################
# First Page - Trying out the methods                           #
#################################################################

# Generate FPDF object and add page
# FPDF(orientation, unit, format)
pdf = FPDF("P","mm","A4")
pdf.add_page()

# fpdf.set_font(family, style = '', size = 0)
# Before writing text
pdf.set_font("Arial", "B", 16)

# fpdf.text(x: float, y: float, txt: str)
# Must specify `x,y`
"""
pdf.text(10,10,"Hello, World")
wi = pdf.get_string_width("Hello, World ")
pdf.text(10+wi,10,"Goodbye, World")
"""

# fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
# Rely on cursor for `x,y`
pdf.cell(0,10,"Hello, World",1,1,"C")

pdf.set_font("Courier", "", 14)
pdf.cell(95,10,"print('Hello, World')",1,0,"C")

# fpdf.set_text_color(r,g=-1,b=-1)
pdf.set_text_color(153,15,103)
pdf.cell(95,10,"console.log('Hello, World')",1,1,"C")

# fpdf.set_draw_color(r,g,b)
pdf.set_text_color(0)
pdf.cell(95,10,"Python 3",1,0,"C")
pdf.set_draw_color(153,15,103)

# fpdf.set_line_width(size)
pdf.set_line_width(1)
pdf.cell(95,10,"JavaScript",1,1,"C")

# Print color gradient of lines
# fpdf.rect(x: float, y: float, w: float, h: float, style = '')
for i in range(20):
    pdf.set_draw_color(153-5*i,15,103+5*i)
    pdf.set_fill_color(153-5*i,15,103+5*i)
    pdf.rect(10,50+i*2.5,190,2.5,"DF")
pdf.set_fill_color(255)

# Adding image of Guybrush Threepwood 
# fpdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
pdf.set_xy(10,110)
pdf.image("guy.jpeg", x = None, y = None, w = 0, h = 0)



#################################################################
# Second Page - Getting Serious                                 #
#################################################################
 
pdf.add_page()

# Load Data
df = pd.DataFrame(data)

# Define our cols and num_cols so cell width is calculated relatively
# You can change the number of columns and it will adapt to fit
# the whole page (190 mm = 210mm - 2 * 10mm)
# 10mm is the default left and right margins
cols = list(tableColumns(df))
num_cols = len(cols)
A4_width = 210
l_margin = 10
r_margin = 10
useful_page_width = A4_width-l_margin-r_margin

# Use font_type_table_header and font_type_table_body
# to get font configuration from other file `config.py`
# so it can be changed without going through code.
# The same can be applied to color, etc.
pdf.set_font(**font_type_table_header)
pdf.set_draw_color(0)
pdf.set_text_color(0)

cell_width = useful_page_width/num_cols

# Printing Header
for col in cols:
    pdf.cell(cell_width,10,col.upper(),1,0,"C")
# Add line break after printing whole line
pdf.ln()

# Printing Body
# Set border width
pdf.set_line_width(0.1)
pdf.set_font(**font_type_table_body)
for row in tableValues(df): 
    for val in row:
        # fit_word(string,cell_w,font_type)
        # Checks if string fits cell and adapts it if not
        # EXTRA - NOT SEEN ON CLASS - CONDITIONALS
        # Add condition to change color if country is european
        # and update font_type_table_body to have bold underline
        # Uncomment to check result
        """
        if val in european_countries:
            pdf.set_text_color(*green)
            pdf.set_fill_color(*yellow)
            font_type_table_body["style"] = "BU"
            pdf.set_font(**font_type_table_body)
        else:
            pdf.set_text_color(*black)
            pdf.set_fill_color(255)
            font_type_table_body["style"] = ""
            pdf.set_font(**font_type_table_body)
        """
        pdf.cell(cell_width,10,fit_word(val,cell_width,font_type_table_body),1,0,"C",1)
    pdf.ln()

# There are unlimited posibilities
# Be creative!!!

# Save File
pdf.output("sample_pdf.pdf","F")