
import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
     try:
          
          with sr.Microphone() as mic :
               print("say...")
               recognizer.adjust_for_ambient_noise(mic, duration=0.1)
               audio = recognizer.listen(mic)
            

               text = recognizer.recognize_google(audio)
               text = text.lower()

               print(f"Recognized {text}")

     except : #sr.UnknownValueErrror()
        recognizer = sr.Recognizer()
        continue
