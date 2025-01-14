import fitz  # PyMuPDF
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFWithEmbeddedXML:
    def __init__(self, pdf_path, temp_pdf_path, xml_path):
        self.pdf_path = pdf_path
        self.xml_path = xml_path
        self.temp_pdf_path = temp_pdf_path

    def read_xml_file(self):
        with open(self.xml_path, 'r', encoding='utf-8') as xml_file:
            xml_data = xml_file.read()
        return xml_data

    def embed_xml_in_pdf(self):
        xml_data = self.read_xml_file().encode('utf-8')
        
        # Open the temporary PDF
        with fitz.open(self.temp_pdf_path) as doc:
            doc.embfile_add("info.xml", xml_data)
            doc.save(self.pdf_path)

def browse_pdf():
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_path_var.set(pdf_file)

def browse_xml():
    xml_file = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
    xml_path_var.set(xml_file)

def create_pdf_with_xml():
    pdf_path = pdf_path_var.get()
    xml_path = xml_path_var.get()

    if not pdf_path or not xml_path:
        messagebox.showerror("Error", "Please select both a PDF and an XML file.")
        return

    output_pdf_path = "invoice_with_embedded_xml.pdf"

    # Call the function to embed XML in the PDF
    pdf_with_xml = PDFWithEmbeddedXML(output_pdf_path, pdf_path, xml_path)
    try:
        pdf_with_xml.embed_xml_in_pdf()
        messagebox.showinfo("Success", f"PDF created successfully: {output_pdf_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Initialize Tkinter root window
root = tk.Tk()
root.title("Embed XML into PDF")

# Create tkinter variables for file paths
pdf_path_var = tk.StringVar()
xml_path_var = tk.StringVar()

# Create GUI layout
tk.Label(root, text="Select PDF File").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=pdf_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_pdf).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select XML File").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=xml_path_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_xml).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Submit", command=create_pdf_with_xml).grid(row=2, column=0, columnspan=3, pady=20)

# Start the Tkinter event loop
root.mainloop()
