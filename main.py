import pdfplumber as pp
from gtts import gTTS

pdf_text = ''

with pp.open('a_purpose_driven_life.pdf') as file:
    for page in file.pages:
        pdf_text += page.extract_text()


tts = gTTS(text=pdf_text, lang='en')
tts.save('audio_book.mp3')
