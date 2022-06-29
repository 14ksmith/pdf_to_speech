# python text to speech
import pyttsx3


def text_to_speech(converted_pdf_to_text):
    """Converts the final_string returned from convert_pdf function into speech."""
    # Initialize the text to speech engine
    engine = pyttsx3.init()
    # Convert text to speech
    engine.say(converted_pdf_to_text)
    # Play the speech
    engine.runAndWait()
