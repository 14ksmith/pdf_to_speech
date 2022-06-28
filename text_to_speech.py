# python text to speech
import pyttsx3


def to_speech(convert_pdf):
    """Converts the final_string returned from convert_pdf function into speech."""
    # Initialize the text to speech engine
    engine = pyttsx3.init()
    # Convert text to speech
    engine.say(convert_pdf)
    # Play the speech
    engine.runAndWait()
