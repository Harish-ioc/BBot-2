import speech_recognition as sr

def listen():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture microphone input
    with sr.Microphone() as source:
        print("Please speak:")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)  # Listen for audio input

    # Try to recognize speech using Google Speech Recognition
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Sorry, could not request results; {0}".format(e))

if __name__ == "__main__":
    print("")
