'''
# pdf to docx
from pdf2docx import parse
parse("a1.pdf", "a1.docx", start=0, end=3)

'''

# from pdf2md import parse

# parse("a1.pdf", "a2.md")

import pdftotree 
pdftotree.parse(pdf_file = "a1.pdf", html_path = "a1.html", model_type=None, model_path=None, favor_figures=True, visualize=False)