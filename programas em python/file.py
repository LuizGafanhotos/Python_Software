import fitz
import os

pasta = r"C:\\Users\\renata\\Downloads"
pdflist = os.listdir(pasta)

pagel = 9

for pdf in pdflist:
    if pdf.endswith(".pdf"):
        document = fitz.open(pdf)
        page = document.loadPage(pagel-1)
        matriz = fitz.Matrix(8,8)
        pix = page.getPixmap(matrix=matriz)
        output = str(pdf)+" - outfile.png"
        pix.writePNG(output)