# ----- Text to Speech ------- #


from gtts import gTTS
from PyPDF2 import PdfReader
import os

f  =open('Demo.pdf','rb')
pdf = PdfReader(f)
text = ''
for pages in pdf.pages:
  text += pages.extract_text()

language = 'en'

audio = gTTS(text=text, lang=language,slow=False)
audio.save('audio.wav')
os.system('audio.wav')
