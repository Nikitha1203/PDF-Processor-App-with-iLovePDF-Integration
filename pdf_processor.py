import requests
import os
import tempfile
from PyPDF2 import PdfFileReader, PdfReader
from creds import api_public_key, api_secret_key

class PDFProcessor:
    def __init__(self, api_public_key, api_secret_key):
        self.api_public_key = api_public_key
        self.api_secret_key = api_secret_key
        self.api_url = "https://api.ilovepdf.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_secret_key}"
        }

    def combine_pdfs(self, pdf_urls, output_path):
        task_id = self.create_task("merge")

        for pdf_url in pdf_urls:
            self.add_file_to_task(task_id, pdf_url)

        self.execute_task(task_id)
        self.download_merged_pdf(task_id, output_path)

    def separate_pdf_pages(self, pdf_file, output_folder):
        task_id = self.create_task("split")

        self.add_file_to_task(task_id, pdf_file)
        self.set_ranges(task_id, "2-4,6-8")

        self.execute_task(task_id)
        self.download_split_pdfs(task_id, output_folder)

    def remove_pdf_password(self, pdf_file, output_path, password):
        task_id = self.create_task("unlock")

        self.add_file_to_task(task_id, pdf_file)
        self.set_password(task_id, password)

        self.execute_task(task_id)
        self.download_unlocked_pdf(task_id, output_path)

    def extract_text(self, pdf_file, output_text_path):
        task_id = self.create_task("text")

        self.add_file_to_task(task_id, pdf_file)

        self.execute_task(task_id)
        self.download_extracted_text(task_id, output_text_path)

    def convert_images_to_pdf(self, image_urls, output_pdf_path):
        task_id = self.create_task("imagepdf")

        for image_url in image_urls:
            self.add_file_to_task(task_id, image_url)

        self.execute_task(task_id)
        self.download_image_to_pdf(task_id, output_pdf_path)

    def create_task(self, tool):
        response = requests.post(
            f"{self.api_url}/{tool}",
            headers=self.headers
        )
        task_id = response.json().get("task")
        return task_id

    def add_file_to_task(self, task_id, file_url):
        requests.post(
            f"{self.api_url}/task/{task_id}/add",
            headers=self.headers,
            data={"url": file_url}
        )

    def set_ranges(self, task_id, page_ranges):
        requests.post(
            f"{self.api_url}/task/{task_id}/setrange",
            data={"pages": page_ranges}
        )

    def set_password(self, task_id, password):
        requests.post(
            f"{self.api_url}/task/{task_id}/password",
            data={"password": password}
        )

    def execute_task(self, task_id):
        requests.get(
            f"{self.api_url}/task/{task_id}/execute",
            headers=self.headers
        )

    def download_merged_pdf(self, task_id, output_path):
        response = requests.get(
            f"{self.api_url}/task/{task_id}/download",
            headers=self.headers
        )
        with open(output_path, "wb") as output_file:
            output_file.write(response.content)

    def download_split_pdfs(self, task_id, output_folder):
        response = requests.get(f"{self.api_url}/task/{task_id}/download", headers=self.headers)
        response.raise_for_status()  # Check for request success

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(response.content)
            tmp_file_path = tmp_file.name

        # Extract individual PDFs from the zip
        with PdfFileReader(open(tmp_file_path, 'rb')) as pdf_reader:
            num_pages = pdf_reader.numPages

            for page_num in range(num_pages):
                output_file_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
                with PdfReader(tmp_file_path) as pdf:
                    pdf_writer = PdfFileReader()
                    pdf_writer.appendPagesFromReader(pdf.pages[page_num])
                    with open(output_file_path, 'wb') as output_file:
                        pdf_writer.write(output_file)

        os.remove(tmp_file_path)

    def download_unlocked_pdf(self, task_id, output_path):
        response = requests.get(
            f"{self.api_url}/task/{task_id}/download",
            headers=self.headers
        )
        with open(output_path, "wb") as output_file:
            output_file.write(response.content)

    def download_extracted_text(self, task_id, output_text_path):
        response = requests.get(
            f"{self.api_url}/task/{task_id}/download",
            headers=self.headers
        )
        with open(output_text_path, "w", encoding="utf-8") as output_file:
            output_file.write(response.text)

    def download_image_to_pdf(self, task_id, output_pdf_path):
        response = requests.get(
            f"{self.api_url}/task/{task_id}/download",
            headers=self.headers
        )
        with open(output_pdf_path, "wb") as output_file:
            output_file.write(response.content)
