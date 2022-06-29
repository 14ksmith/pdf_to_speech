from inspect import Arguments
from tracemalloc import start
from core.pdf_to_text import convert_pdf_to_text, write_to_text_file
from core.text_to_speech import text_to_speech


def start_pdf_to_text_file(pdf_name):
    # Call the pdf to text function within the text file creation function using the file name input
    write_to_text_file(
        txt_name=f"pdf/{pdf_name}.txt",
        converted_pdf_to_text=convert_pdf_to_text(pdf=f"pdf/{pdf_name}.pdf"),
    )


def start_pdf_to_speech(pdf_name):
    # Call the pdf to text function within the text to speech function using the file name input
    text_to_speech(convert_pdf_to_text(pdf=f"pdf/{pdf_name}.pdf"))


if __name__ == "__main__":

    # TODO: FUNCTION TO COLLECT COMMAND LINE Arguments
    #   check if the command line argument[0] == to_text

    pdf_name = input(
        "What is the name of the pdf you would like to convert to speech? (exclude '.pdf'): "
    )

    start_pdf_to_speech(pdf_name=pdf_name)
