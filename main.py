from core.pdf_to_text import convert_pdf, to_txt
from core.text_to_speech import to_speech


pdf_name = input(
    "What is the name of the pdf you would like to convert to speech? (exclude '.pdf'): "
)

# Call the pdf to text function within the text to speech function
to_speech(convert_pdf(pdf=f"pdf/{pdf_name}.pdf"))

# Call the pdf to text function within the text file creation function
to_txt(
    txt_name=f"pdf/{pdf_name}.txt", convert_pdf=convert_pdf(pdf=f"pdf/{pdf_name}.pdf")
)
