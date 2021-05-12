import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en'
output_lang = 'es'

try:
    with sr.Microphone() as source:
        print("Speak Now...")
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice)
        print(text)

except:
    pass

translated = translator.translate(text, dest=input_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('Language.mp3')
playsound.playsound('Language.mp3')
