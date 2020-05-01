import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Konuşun:')
    audio=r.listen(source)

    try:
        text= r.recognize_google(audio,language='tr')
        print('Söyledikleriniz:{}'.format(text))
    except:
        print('Sesiniz tam alınamamıştır')