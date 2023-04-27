from PyPDF2 import PdfReader as pdf_reader

pdf_file_obj = open('meetingminutes.pdf', 'rb') # 'rb': read binary, 'wb': write binary
pdf = pdf_reader(pdf_file_obj)

print(len(pdf.pages))

text = pdf.pages[0].extract_text()
print(text)
