from core.pdf_to_text import convert_pdf_to_text, write_to_text_file
from core.text_to_speech import text_to_speech
import sys


def get_command_line_args():
    """Get the second arg passed into the command line when starting application, and set to 'text_arg'.
    If there is no second arg, set 'text_arg' to None.
    Return 'text_arg'. (First arg is always the script name)"""
    if len(sys.argv) > 1:
        text_arg = sys.argv[1]
    else:
        text_arg = None
    return text_arg


def start_pdf_to_text_file(pdf_name):
    # Call the pdf to text function within the text file creation function using the file name input
    write_to_text_file(
        txt_name=f"pdf/{pdf_name}.txt",
        converted_pdf_to_text=convert_pdf_to_text(pdf=f"pdf/{pdf_name}.pdf"),
    )
    # exit the program after creating the new text file so it does not start pdf to speech
    exit()


def start_pdf_to_speech(pdf_name):
    # Call the pdf to text function within the text to speech function using the file name input
    text_to_speech(convert_pdf_to_text(pdf=f"pdf/{pdf_name}.pdf"))


if __name__ == "__main__":

    # Retrieve second arg if there is one
    command_line_arg = get_command_line_args()

    pdf_name = input(
        "What is the name of the pdf you would like to convert to speech? (exclude '.pdf'): "
    )

    # if the arg '--text' is included in the command line, then call the function to convert pdf to text file
    if command_line_arg == "--text":
        start_pdf_to_text_file(pdf_name=pdf_name)

    # Start the pdf to speech function
    start_pdf_to_speech(pdf_name=pdf_name)
