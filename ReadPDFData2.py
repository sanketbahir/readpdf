import PyPDF2

file = open("demo.pdf", "rb")
reader = PyPDF2.PdfReader(file)
num_pages = len(reader.pages)
page3 = reader.pages[2] 
pdfData =  page3.extract_text()
assert "sanket" in  pdfData

file.close()
