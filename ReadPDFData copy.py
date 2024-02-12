import PyPDF2

file = open("demo.pdf", "rb")
reader = PyPDF2.PdfReader(file)
num_pages = len(reader.pages)
page3 = reader.pages[2] 
data = page3.extract_text()
print(num_pages)
print(data)
file.close() 
