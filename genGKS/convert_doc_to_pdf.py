'''Convert docx to pdf'''


from docx2pdf import convert
import os 


files = os.listdir("GEN1000/")

# convert("input.docx")
# convert("input.docx", "output.pdf")
# convert("my_docx_folder/")

for f in files:
    convert("GEN1000/" + f, "PDF1000/" + f[:-4] + "pdf")