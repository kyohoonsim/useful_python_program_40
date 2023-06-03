from gtts import gTTS

text = "We are studying Python right now."
tts = gTTS(text, lang='en')
tts.save('result1.mp3')