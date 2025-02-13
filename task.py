import fitz  # PyMuPDF
import os

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
            doc.embfile_add("invoice.xml", xml_data) # xml file embaded with pdf
            doc.save(self.pdf_path)

if __name__ == '__main__':
    pdf_path = "invoice_with_embedded_xml.pdf"

    temp_pdf_path= "PDF/invoice.pdf"
    xml_path = "Data/invoice_gcp5.xml"  

    pdf_with_xml = PDFWithEmbeddedXML(pdf_path, temp_pdf_path, xml_path)
    pdf_with_xml.embed_xml_in_pdf()
