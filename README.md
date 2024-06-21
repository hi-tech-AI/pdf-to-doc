# PDF to DOCX Conversion Script

This project provides two methods for converting PDF files to DOCX format using Python:

1. **pdf2docx** library
2. **win32com** client (requires Microsoft Word)

## Prerequisites

- Python 3.7+
- `pdf2docx` package for conversion using the pdf2docx method.
- `pywin32` package for interacting with Microsoft Word via win32com.

## Setup

### Step 1: Install Required Packages

```bash
pip install pdf2docx pywin32
```

### Step 2: Ensure Microsoft Word is Installed

For the **win32com** method, you need to have Microsoft Word installed on your machine.

## Code Structure

### Functions

#### 1. pdf2docx_pdf(pdf_file)
This function uses the `pdf2docx` library to convert a PDF file to a DOCX file.

#### 2. win32com_pdf(pdf_file)
This function uses the `win32com` library to convert a PDF file to a DOCX file through Microsoft Word.

### Running the Script

To run the script and convert a PDF file to DOCX format, use the following block:

```python
if __name__ == "__main__":
    pdf_file = './example1.pdf'
    # Uncomment the desired method
    # pdf2docx_pdf(pdf_file)
    win32com_pdf(pdf_file)
```

## Example Usage

1. **Using pdf2docx Library**
   - Make sure to uncomment the line `pdf2docx_pdf(pdf_file)` in the `if __name__ == "__main__"` block.

2. **Using win32com Library**
   - Make sure to uncomment the line `win32com_pdf(pdf_file)` in the `if __name__ == "__main__"` block.

Then, simply run the script:

```bash
python main.py
```

### Notes

- The `pdf2docx` method is platform-independent, while the `win32com` method requires Windows OS with Microsoft Word installed.
- The `win32com` method might provide better accuracy for complex PDFs due to direct interaction with Microsoft Word's conversion capabilities.
- You may need to handle exceptions and edge cases specific to your PDF files for more robust operation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
