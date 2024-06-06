import requests
import os
from dotenv import load_dotenv
load_dotenv()

pdf_id = "output"
APP_KEY = os.getenv("APP_KEY")
APP_ID = os.getenv("APP_ID")

# get pdf response
json = {
    "url": "input.pdf",
    "conversion_formats": {
        "docx": True,
        "tex.zip": True
    }
}

headers = {
  "app_key": APP_KEY,
  "app_id": APP_ID
}

# get docx response
url = "https://api.mathpix.com/v3/pdf/" + pdf_id + ".docx"
response = requests.get(url, json=json, headers=headers)
with open(pdf_id + ".docx", "wb") as f:
    f.write(response.content)