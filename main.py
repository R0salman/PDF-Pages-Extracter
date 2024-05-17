import os
import shutil
import time
import PyPDF2
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


#defining a function
def extract_pages(input_file, pages, output_file):
    with open(input_file, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        writer = PyPDF2.PdfWriter()

        for page_num in pages:
            if page_num > len(reader.pages) or page_num < 1:
                print(f"Page number {page_num} is out of range. Skipping.")
                continue
            writer.add_page(reader.pages[page_num - 1])

        with open(output_file, 'wb') as output:
            writer.write(output)

if __name__ == "__main__":
    #create "EditedPDFs" folder on the desktop if it doesn't exist
    desktop_path = Path.home() / "Desktop"
    edited_pdfs_folder_path = desktop_path / "EditedPDFs"
    edited_pdfs_folder_path.mkdir(parents=True, exist_ok=True)

    #making a window so the user select the input_file
    root = tk.Tk()
    root.withdraw()
    input_pdf = filedialog.askopenfilename()

    #read the list of page numbers
    pages = input("Enter the page numbers you want to extract [No comma, Only use space]: ")
    pages = pages.split()
    pages = [int(page) for page in pages]

    #get the output_file name from the user
    output_name = input("Enter the name of the output file: ")
    output_file = edited_pdfs_folder_path / f"{output_name}.pdf"

    #call the function
    extract_pages(input_pdf, pages, output_file)

    #move or overwrite the output file to the "EditedPDFs" folder
    try:
        shutil.move(output_file, edited_pdfs_folder_path)
    except shutil.Error as e:
        print(f"Something happend! {e}, check the folder...")
        os.replace(output_file, edited_pdfs_folder_path / f"{output_name}.pdf")
        print("wait...")
    time.sleep(3)
    print(f"Extraction of the pages was successful! It was saved as {output_name} and stored inside {edited_pdfs_folder_path} folder!")