from gtts import gTTS
from PyPDF2 import PdfReader

# Open the PDF file using context manager to ensure proper closure
with open('name.pdf', 'rb') as pdf_file:
    # Create PDF reader object
    pdf_reader = PdfReader(pdf_file)
    count = len(pdf_reader.pages)  # Counts the number of pages in the PDF

    textList = []

    # Extracting text data from each page of the PDF file
    for i in range(count):
        try:
            page = pdf_reader.pages[i]
            textList.append(page.extract_text())  # Append extracted text from each page
        except Exception as e:
            print(f"Error extracting text from page {i}: {e}")
            pass

    # Joining all page texts into a single string (this happens after the loop)
    textString = " ".join(textList)

# Print the text for debugging
print(textString)

# Set language to English (en)
language = 'en'

# Call gTTS to convert text to speech
myAudio = gTTS(text=textString, lang=language, slow=False)

# Save the audio as an MP3 file
myAudio.save("Audio.mp3")

