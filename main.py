from pdf_to_md import *
from equation_extractor import *

input_pdf_path = 'example1.pdf'
file_type = 'md'

# Convert *.pdf file to *.md file using Mathpix API
# md_file_name = pdf_to_md(input_pdf_path, file_type)

md_file_name = 'example1.md'
# Extract LaTex string of equation in *.md file
equations = extract_latex_equations(md_file_name)

for i, eq in enumerate(equations, 1):
    print(f"Equation {i}: {eq.strip()}")