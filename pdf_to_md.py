import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

def send_pdf_to_mathpix(file_path, output_format):
    url = 'https://api.mathpix.com/v3/pdf'
    headers = {
        'app_id': APP_ID,
        'app_key': APP_KEY,
    }

    with open(file_path, 'rb') as file:
        files = {'file': file}
        options = {
            'options_json': json.dumps({"conversion_formats": {output_format: True}, "rm_spaces": True})
            }
        print(f"Sending {os.path.getsize(file_path) / 1000} kb to Mathpix")
        response = requests.post(url, headers=headers, data=options, files=files)
        response_data = response.json()

        if 'pdf_id' in response_data:
            pdf_id = response_data['pdf_id']
            print(f"PDF ID: {pdf_id}")
            return pdf_id
        else:
            print("Error: Unable to send PDF to Mathpix")
            return None

def wait_for_processing(file_id, purpose='pdf'):
    url = f'https://api.mathpix.com/v3/{purpose}/{file_id}'
    headers = {
        'app_id': APP_ID,
        'app_key': APP_KEY
    }

    while True:
        response = requests.get(url, headers=headers)
        response_data = response.json()
        status = response_data.get('status', None)

        if status == 'completed':
            print("Processing complete")
            return True
        elif status == 'error':
            print("Error: Unable to process PDF")
            return False
        else:
            print(f"Status: {status}, waiting for processing to complete")
            time.sleep(3)

def download_processed_file(file_id, file_format, output_path, purpose='pdf'):
    url = f'https://api.mathpix.com/v3/{purpose}/{file_id}.{file_format}'
    headers = {
        'app_id': APP_ID,
        'app_key': APP_KEY
    }

    response = requests.get(url, headers=headers)
    with open(output_path, 'wb') as output_file:
        output_file.write(response.content)
    print(f"File downloaded to {output_path}")

def pdf_to_md(input_pdf_path, file_type):
    print('start pdf convert')
    # path of the converted markdown file
    output_mmd_path = input_pdf_path.replace('.pdf', f'.{file_type}')

    # pdf to md convert
    if not os.path.exists(output_mmd_path):
        pdf_id = send_pdf_to_mathpix(input_pdf_path, file_type)
        if pdf_id and wait_for_processing(pdf_id):
            download_processed_file(pdf_id, file_type, output_mmd_path)

    return output_mmd_path            