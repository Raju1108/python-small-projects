# Importing Libraries
from gtts import gTTS  # Corrected import
from PyPDF2 import PdfReader  # Correct import for PyPDF2

# Open the PDF file
pdf_file = open('name.pdf', 'rb')


# Create PDF reader object
pdf_reader = PdfReader(pdf_file)
count = len(pdf_reader.pages)  # Counts the number of pages in the PDF

textList = []

# Extracting text data from each page of the PDF file
for i in range(count):
    try:
        page = pdf_reader.pages[i]
        textList.append(page.extract_text())  # Append extracted text from each page
    except:
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

# Close the PDF file after processing
pdf_file.close()
