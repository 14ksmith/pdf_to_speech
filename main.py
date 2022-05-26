# plays the sound for the text to speech
from black import out
from playsound import playsound

# python text to speech
import pyttsx3

# pdfminer import
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# For the formatting of the sentence spaces
import re

# ----------------------------- CONVERT PDF TO TEXT FILE --------------------------------#


def convert_pdf(pdf):
    """Converts a given pdf to text. Returns the converted text."""
    output_string = StringIO()
    with open(pdf, "rb") as file:
        parser = PDFParser(file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    final_string = " ".join(output_string.getvalue().split())
    return final_string


def to_txt(txt_name, convert_pdf):
    """Creates a txt file with final_string returned from convert_pdf function."""
    # save extracted data from pdf to a text file
    black_cat_text = open(txt_name, "a")
    black_cat_text.writelines(convert_pdf)


# ----------------------------------------------------------------------------------------#

# ----------------------------- CONVERT TEXT TO SPEECH -----------------------------------#


def to_speech(convert_pdf):
    """Converts the final_string returned from convert_pdf function into speech."""
    # Initialize the text to speech engine
    engine = pyttsx3.init()
    # Convert text to speech
    engine.say(convert_pdf)
    # Play the speech
    engine.runAndWait()


# ----------------------------------------------------------------------------------------#

pdf_path = input(
    "What is the file path of the pdf you would like to convert to speech? (exclude '.pdf'): "
)

# Call the pdf to text function within the text to speech function
to_speech(convert_pdf(pdf=f"{pdf_path}.pdf"))

# # Call the pdf to text function within the text file creation function
# to_txt(txt_name=f"{pdf_path}.txt", convert_pdf=convert_pdf(pdf=f"{pdf_path}.pdf"))
