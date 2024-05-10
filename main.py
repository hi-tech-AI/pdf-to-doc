# import pdfplumber

# # Convert PDF to DOC
# pdfplumber.converter.convert_from_path("input.pdf", "output.doc")

# # Extract text from PDF
# with pdfplumber.open("input.pdf") as pdf:
#     text = ""
#     for page in pdf.pages:
#         text += page.text

# # Extract tables from PDF
# table_data = []
# with pdfplumber.open("input.pdf") as pdf:
#     for page in pdf.pages:
#         for rect in page.rects:
#             if rect.type == "table":
#                 data = []
#                 for cell in rect.cells:
#                     data.append(cell.text)
#                 table_data.append(data)

# # Extract images from PDF
# image_data = []
# with pdfplumber.open("input.pdf") as pdf:
#     for page in pdf.pages:
#         for image in page.images:
#             image_data.append(image.getvalue())

# # Extract mathematical formulas from PDF
# formula_data = []
# with pdfplumber.open("input.pdf") as pdf:
#     for page in pdf.pages:
#         for curve in page.curves:
#             if curve.type == "formula":
#                 formula_data.append(curve.get_data())



# import convertapi

# convertapi.api_secret = 'o4VDPH5JjpJVfcsz'
# convertapi.convert('docx', {
#     'File': 'sample.pdf',
#     'Wysiwyg': 'true'
# }, from_format = 'pdf').save_files('output.docx')


import os
import win32com.client
import pythoncom

def pdf_to_doc(pdf_file, doc_file):
    """
    Converts a PDF file to a DOC file using the win32com library.
    
    Args:
        pdf_file (str): The path to the input PDF file.
        doc_file (str): The path to the output DOC file.
    """
    try:
        # Initialize the Word COM object
        pythoncom.CoInitialize()
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False  # Set to True if you want to see the Word application
        
        # Create a new document
        doc = word.Documents.Add()
        
        # Open the PDF file
        doc.GoTo(0)
        selection = word.Selection
        selection.PasteSpecial(Link=False, DataType=-4104, DisplayAsIcon=False)
        
        # Save the document as a DOC file
        doc.SaveAs(doc_file, FileFormat=0)  # FileFormat=0 for DOC
        
        # Close the document and the Word application
        doc.Close(SaveChanges=True)
        word.Quit()
        
        print(f"PDF file '{pdf_file}' converted to DOC file '{doc_file}'.")
    except Exception as e:
        print(f"Error converting PDF to DOC: {e}")
    finally:
        # Ensure that the Word application is properly closed
        pythoncom.CoUninitialize()

# Example usage
pdf_file = "input.pdf"
doc_file = "output.doc"
pdf_to_doc(pdf_file, doc_file)