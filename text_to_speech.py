from gtts import gTTS
import pyttsx3
import os


myText=input("Okunacak metni yazınız: ")


print('pyttsx3 çıktısı')
engine = pyttsx3.init()
engine.say(myText)
engine.runAndWait()


language=input("Okunacak metnin dilini yazınız(Örn. tr): ")
if(language == ''):
    language='en'
print('Google output')
output= gTTS(text=myText, lang=language,slow=False)
output.save("output.mp3")
os.system("output.mp3")