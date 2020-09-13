from gtts import gTTS

import os

f=open('text.txt')
x=f.read()

language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save("text.wav")
os.system("text.wav")
