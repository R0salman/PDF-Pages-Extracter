# PDF-Pages-Extracter

This is a Python script that extracts specific pages from a PDF file 
and saves the extracted pages as a new PDF file.

## Requirements

-  Python3
- PyPDF2
- tkinter (usually included with Python)
- shutil (usually included with Python)

## Usage

1. **Run the script:**

   ```sh
   python script_name.py
   ```

2. **Select the input PDF file:**

   A file dialog will appear allowing you to select the PDF file
    from which you want to extract pages.

3. **Enter the page numbers:**

   In the terminal, enter the page numbers you want to extract, separated by spaces.
    For example, to extract pages 1, 3, and 5, you would enter:

   ```
   1 3 5
   ```

4. **Enter the name of the output file:**

   In the terminal, enter the desired name for the output PDF file (without the `.pdf` extension).

5. **Check the `EditedPDFs` folder:**

   The script will create a folder named `EditedPDFs` on your Desktop (if it doesn't already exist) and save the extracted pages as a new PDF file inside this folder.

