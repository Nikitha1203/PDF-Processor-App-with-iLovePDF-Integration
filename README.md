# PDF-Processor-App-with-iLovePDF-Integration
This Python application provides a user-friendly interface to process PDF files with a variety of operations, such as merging, splitting, removing password protection, text extraction, and image-to-PDF conversion. It integrates with the iLovePDF API to perform these tasks seamlessly.

## Features

1. **Combine PDF Files:** Merge two or more PDF files into a single PDF document.

2. **Separate PDF Pages:** Split a PDF document into individual pages saved as separate PDF files.

3. **Remove PDF Password:** Remove password security from a PDF document, enabling reading and editing.

4. **Extract Text from PDF:** Extract all text content from a PDF file and save it to a text file.

5. **Convert Images to PDF:** Convert JPG, TIFF, and PNG images into a single PDF document.

## Usage

1. Clone this repository to your local machine.

2. Install the required Python packages by running `pip install -r requirements.txt`.

3. Set up your iLovePDF API credentials in the `creds.py` file. Obtain your API keys by signing up at [iLovePDF Developer](https://developer.ilovepdf.com/tools) and follow the API documentation.

4. Run the app using Streamlit by executing `streamlit run main.py`.

5. Choose one of the available PDF processing options and upload your PDF file. Follow the on-screen instructions to complete the selected operation.

6. After processing, you can download the result directly from the app.

7. To exit the app, select the "Exit" option.

## Dependencies

- Python 3.x
- Streamlit
- Requests

## Configuration

Make sure to configure your API keys in the `creds.py` file:

python
api_public_key = "your_project_public_key"
api_secret_key = "your_secret_key"
