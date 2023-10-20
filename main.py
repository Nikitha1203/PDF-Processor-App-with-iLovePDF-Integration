import streamlit as st
from pdf_processor import PDFProcessor
import os
import tempfile

def main():
    st.sidebar.subheader("Choose an option:")
    selected_option = st.sidebar.selectbox("", ["Combine PDF files", "Separate PDF pages", "Remove PDF password",
                                               "Extract text from PDF", "Convert images to PDF", "Exit"])

    if selected_option != "Exit":
        pdf_file = st.file_uploader("Upload a PDF file:", type=["pdf"])

        if pdf_file is not None:
            output_path = f"output_{selected_option}.pdf"  # Set the output path based on the selected operation

            pdf_processor = PDFProcessor( "project_public_ba423eea39447cf6c01e2b78eb45b80a_Q5HvLf46816bfa2c7c9a83709904dce7c19f1"
,"secret_key_55ebf94acdc58f8b15436ccec96c816e_Zk2yc05165438f0de1e6f836494d202f60984"
)  # Initialize PDFProcessor with your API keys

            if selected_option == "Combine PDF files":
                st.text("Combining PDF files...")
                pdf_processor.combine_pdfs([pdf_file], output_path)

            elif selected_option == "Separate PDF pages":
                st.text("Separating PDF pages...")
                output_folder = f"output_{selected_option}"
                os.makedirs(output_folder, exist_ok=True)
                pdf_processor.separate_pdf_pages(pdf_file, output_folder)

            elif selected_option == "Remove PDF password":
                st.text("Removing PDF password...")
                password = st.text_input("Enter the PDF password:")
                pdf_processor.remove_pdf_password(pdf_file, output_path, password)

            elif selected_option == "Extract text from PDF":
                st.text("Extracting text from PDF...")
                output_text_path = f"output_{selected_option}.txt"
                pdf_processor.extract_text(pdf_file, output_text_path)

            elif selected_option == "Convert images to PDF":
                st.text("Converting images to PDF...")
                output_pdf_path = f"output_{selected_option}.pdf"
                pdf_processor.convert_images_to_pdf([pdf_file], output_pdf_path)

            download_link = f"[Download the result](./{output_path})"
            st.success(f"{selected_option} completed. Click the link below to download the result automatically.")
            st.markdown(download_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
