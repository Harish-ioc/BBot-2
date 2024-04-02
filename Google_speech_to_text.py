import speech_recognition as sr
from Serial_send import *

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak:")
        write("S")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)  # Listen for audio input

    try:
        write("Q")
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        write("Q")
        print("Sorry, could not understand audio.")
        return "Did you understand the question?"
    except sr.RequestError as e:
        write("Q")
        print("Sorry, could not request results; {0}".format(e))
        return "Did you understand the question?"


if __name__ == "__main__":
    # listen()
    print("")
