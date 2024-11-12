import requests
import fitz  # pymupdf

# Book URL
url = "https://americanenglish.state.gov/files/ae/resource_files/the_tell-tale_heart_0.pdf"

# Downloading the PDF from the URL
resp = requests.get(url)
with open('book.pdf', 'wb') as f:
    f.write(resp.content)
    
# Opening the PDF file
pdf_document = fitz.open("book.pdf")

# Converting the PDF file into text document 'document.txt'
with open("document.txt", 'w', encoding='utf-8') as f:
    # Loop through each page in the PDF and extract text
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)  # Load each page
        text = page.get_text()  # Extract text from the page
        f.write(text)  # Write the extracted text to the document.txt file

# Close the PDF document
pdf_document.close()

print("PDF conversion completed successfully!")
