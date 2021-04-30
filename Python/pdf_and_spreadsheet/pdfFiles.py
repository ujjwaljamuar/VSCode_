import PyPDF2
f=open('Working_Business_Proposal.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

page_one=pdf_reader.getPage(0)
print(page_one)

page_one_text=page_one.extractText()
print(page_one_text)
f.close()


# add pages
f2=open('Working_Business_Proposal.pdf','rb')
pdf_reader1=PyPDF2.PdfFileReader(f2)
firstPage=pdf_reader1.getPage(0)
pdf_Writer=PyPDF2.PdfFileWriter()
pdf_Writer.addPage(firstPage)
pdf_output=open('someNewFile.pdf','wb')
pdf_Writer.write(pdf_output)
f2.close()
pdf_output.close()