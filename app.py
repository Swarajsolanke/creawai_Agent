import pdfplumber
pdf_path=r"C:\aptitude content\13.Permutations Combination.pdf"
print(f"pdf_path:{pdf_path}")

with pdfplumber.open(pdf_path) as pdf:
    text = []
    for page in pdf.pages:
        print(page)
        text1 = page.extract_text()
        print(text1)
        if text1:
            text.append(text1.strip())
           
        print(f"text:{text}")

print(text)


