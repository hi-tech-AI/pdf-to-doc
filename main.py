from pdf2docx import Converter
import win32com.client

def pdf2docx_pdf(pdf_file):
    docx_file = pdf_file.replace('.pdf', '.docx')
    # Create a Converter object
    cv = Converter(pdf_file)
    
    # Convert the PDF to a DOCX file
    cv.convert(docx_file, start=0, end=None)  # start and end can be used to specify the range of pages
    
    # Close the Converter object
    cv.close()
    
    print(f'{pdf_file} has been successfully converted to {docx_file}')
  
def win32com_pdf(pdf_file):
    try:
        docx_file = pdf_file.replace('.pdf', '.docx')
        # Create an instance of Word application
        word = win32com.client.Dispatch("Word.Application")

        # Set Word to be visible (optional)
        word.Visible = False

        # print('Open PDF file')
        # Open the PDF file
        doc = word.Documents.Open(pdf_file)
        # Save the PDF as a DOCX file
        doc.SaveAs(docx_file, FileFormat=16)  # 16 corresponds to the wdFormatDocumentDefault (DOCX format)

        # Close the document and Word application
        doc.Close()
        word.Quit()

        print(f'{pdf_file} has been successfully converted to {docx_file}')
    except Exception as e:
        print(f'An error occurred : {e}')

if __name__ == "__main__":
    pdf_file = 'example1.pdf'
    pdf2docx_pdf(pdf_file)
    # win32com_pdf(pdf_file)