from __future__ import print_function
import re

from PyPDF2 import PdfFileReader as pdfr

grePdfReader = pdfr(open("gre-words.pdf", "rb"))

pageText = grePdfReader.getPage(0).extractText()
print(pageText)
print("/////////////////////////////////////////////////////////")
print(len(re.split("\d+",pageText)[2:-1]))
print(re.split("\d+",pageText)[2:-1])