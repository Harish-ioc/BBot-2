# import sys
# import pyttsx3

# def speak(text):
#     rate = 150
#     volume = 0.7
#     pitch = 150
#     language = 'en'
#     # Initialize the text-to-speech engine
#     engine = pyttsx3.init()

#     engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

#     # Customize voice properties
#     # engine.setProperty('rate', rate)  # Speed of speech
#     # engine.setProperty('volume', volume)  # Volume level (0.0 to 1.0)
#     # engine.setProperty('pitch', pitch)  # Pitch level (50 to 200)
#     # engine.setProperty('language', language)  # Language code

#     # Speak the provided text
#     engine.say(text)

#     # Wait for the speech to finish
#     engine.runAndWait()

# # speak("hello")

# # if len(sys.argv) > 1:
    
# #     received_data = sys.argv[1]
# #     received_data=str(received_data)
# #     print(f"Received data: {received_data}")

# #     speak(received_data)
# speak('the quick brown fox jumped over the lazy dog ')

from gtts import gTTS
import os

def text_to_speech(text, language='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    os.system("start " + filename)  # for Windows

if __name__ == "__main__":
    text = "Enter the text to convert to speech"
    text_to_speech(text)
