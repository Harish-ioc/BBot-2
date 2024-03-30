import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as mic:
                print("Say...")
                recognizer.adjust_for_ambient_noise(mic, duration=0.1)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                print(f"Recognized: {text}")
                return text

        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
            continue

