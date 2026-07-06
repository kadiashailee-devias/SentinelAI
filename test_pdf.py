from tools.pdf_tool import generate_pdf

path = generate_pdf(
    "This is a PDF generation test."
)

print(path)