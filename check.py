import fitz  # PyMuPDF

def check_pdf_attachments(pdf_path):
    doc = fitz.open(pdf_path)

    if doc.embfile_count() > 0:
        print("Embedded files found:")
        for i in range(doc.embfile_count()):
            embedded_file_info = doc.embfile_get(i)
            filename = str(embedded_file_info[0]) 

            print(f"File: {filename}")
            
            if filename.lower() == "info.xml".lower():
                print("XML file is attached successfully.")
                
                file_data = embedded_file_info[1]  
                
                with open(filename, "wb") as f:
                    f.write(file_data)
                print(f"{filename} has been extracted successfully.")
    else:
        print("No embedded files found.")

# Example usage
pdf_path = "invoice_with_embedded_xml.pdf"

## For Testing _________________________________
# pdf_path = "without_xml.pdf"
# pdf_path = "with_xml.pdf"
check_pdf_attachments(pdf_path)
