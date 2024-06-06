import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def doc_to_pdf(doc_path):
    if '.docx' in doc_path:
        pdf_path = doc_path.replace('.docx', '.pdf')
    elif '.doc' in doc_path:
        pdf_path = doc_path.replace('.doc', '.pdf')
    elif '.rtf' in doc_path:
        pdf_path = doc_path.replace('.rtf', '.pdf')
    else:
        print('Invalid type of file')
        return "Invalid type of file"

    pythoncom.CoInitialize()
    
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        # Open the document
        doc = word.Documents.Open(doc_path)
        doc.Activate()

        # Save as PDF
        doc.SaveAs(pdf_path, FileFormat=17)  # 17 represents the wdFormatPDF constant

    except Exception as e:
        print("An error occurred:", e)
        return "Conversion failed"
    finally:
        # Ensure Word is closed
        if 'doc' in locals():
            doc.Close()
        if 'word' in locals():
            word.Quit()

    # Check if the PDF was created successfully
    if os.path.exists(pdf_path):
        print("Doc to PDF Conversion successful.")
        return pdf_path
    else:
        print("Conversion failed. PDF not found.")
        return "Conversion failed"

def send_md_to_mathpix(file_path, output_format, purpose='pdf'):
    url = f'https://api.mathpix.com/v3/{purpose}'
    headers = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
        'Content-Type': 'application/json'
    }

    with open(file_path, 'r', encoding='utf-8') as file:
        options = json.dumps({
            "mmd": file.read(),
            "formats": {
                output_format: True,
            }
            })
        print(f"Sending {os.path.getsize(file_path) / 1000} kb to Mathpix for convert")
        response = requests.post(url, headers=headers, data=options)
        response_data = response.json()

        if 'conversion_id' in response_data:
            conversion_id = response_data['conversion_id']
            print(f"Conversion ID: {conversion_id}")
            return conversion_id
        else:
            print("Error: Unable to send file to Mathpix===>", response_data['error'])
            return None

import re

def extract_latex_equations(file_path):
    # Read the content of the .md file
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    # Regular expression to find all instances of $$ ... $$
    pattern = r'\$\$(.*?)\$\$'
    matches = re.findall(pattern, content, re.DOTALL)

    return matches
