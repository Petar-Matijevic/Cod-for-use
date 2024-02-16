import pyttsx3
import PyPDF2

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    return wrapper

@handle_errors
def read_pdf_and_save_audio(pdf_path, output_mp3_path):
    pdfreader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    speaker = pyttsx3.init()

    # Enhanced voice adjustments for naturalness:
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)  # Experiment with different voice indices
    speaker.setProperty('rate', 150)  # Slightly slower pace for better clarity
    speaker.setProperty('volume', 1.0)  # Adjust volume as needed
    speaker.setProperty('pitch', 0.95)  # Slightly lower pitch for a less robotic tone
    speaker.setProperty('word_gap', 0.15)  # Add slight pauses between words
    all_text = ""  # Initialize variable to hold all text from the PDF

    for page_num in range(len(pdfreader.pages)):
        text = pdfreader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')  # Basic cleaning
        all_text += clean_text + " "  # Concatenate the text from each page

    print("Text extracted from PDF:")
    print(all_text)  # Print the extracted text

    try:
        speaker.save_to_file(all_text, output_mp3_path)  # Save all text to MP3
        print("Audio file saved successfully.")

    except Exception as e:
        print(f"Error saving audio: {e}")

    speaker.runAndWait()
    speaker.stop()

if __name__ == '__main__':
    pdf_path = 'Nier.pdf'  # Adjust path
    output_mp3_path = 'Nier.mp3'  # Adjust output filename
    read_pdf_and_save_audio(pdf_path, output_mp3_path)
