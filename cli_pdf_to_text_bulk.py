import os
import PyPDF2

# Prompt the user for directory paths
pdf_dir = input("Enter the path to your PDF directory: ")
text_dir = input("Enter the path for output text files: ")

# Create the text directory if it doesn't exist
if not os.path.exists(text_dir):
    os.makedirs(text_dir)


def clean_text(text):
    # Implement any cleaning logic here
    # For example, removing headers, footers, page numbers, etc.
    return text


for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith('.pdf'):
        # Construct full file paths
        pdf_path = os.path.join(pdf_dir, pdf_file)
        text_path = os.path.join(text_dir, pdf_file.replace('.pdf', '.txt'))

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            with open(text_path, 'w', encoding='utf-8') as text_file:
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    cleaned_text = clean_text(text)
                    text_file.write(cleaned_text)

print("PDF conversion completed!")
