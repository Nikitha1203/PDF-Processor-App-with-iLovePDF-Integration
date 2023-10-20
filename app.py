# app.py
from main import PDFProcessor
import sys

def main():
    pdf_processor = PDFProcessor()
    while True:
        print("PDF Processing App Menu:")
        print("1. Combine PDFs")
        print("2. Separate PDF Pages")
        print("3. Remove PDF Password")
        print("4. Extract Text from PDF")
        print("5. Convert Images to PDF")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            pdf_processor.combine_pdfs()
        elif choice == "2":
            pdf_processor.separate_pdf_pages()
        elif choice == "3":
            pdf_processor.remove_pdf_password()
        elif choice == "4":
            pdf_processor.extract_text()
        elif choice == "5":
            pdf_processor.convert_images_to_pdf()
        elif choice == "6":
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
