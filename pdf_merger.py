import os
import pypdf

location = input("Enter the path to the files: ")

print("\nEnter the name of the pdfs to be merged in the order you want them to be merged. Enter 'n' to stop.")

pdfs = []
while True:
    pdf = input("Pdf name: ")
    if pdf == "n":
        break
    elif not pdf.endswith(".pdf"):
        pdf += ".pdf"
    pdfs.append(os.path.join(location, pdf))
    
merged_file_name = input("\nEnter the name of the merged file: ")
if not merged_file_name.endswith(".pdf"):
    merged_file_name += ".pdf"
    
merger = pypdf.PdfWriter()
for pdf in pdfs:
    merger.append(pdf)
    
merger.write(os.path.join(location, merged_file_name))
