# pdfminer import
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


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
