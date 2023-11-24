"""
import pyttsx3
 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# engine.setProperty('language', 'zh')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

engine.setProperty("rate", 150)      #(  SPEED INCRESES WITH INCRESE IN NUMBER   )
engine.setProperty("volume", 1)      #(  MAX:1 , MIN:0   )
# engine.setProperty("pitch", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

audio=("the text is this ? for sure ?")
speak(audio)

"""

import pyttsx3

def speak(text, rate, volume, pitch, language):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Customize voice properties
    engine.setProperty('rate', rate)  # Speed of speech
    engine.setProperty('volume', volume)  # Volume level (0.0 to 1.0)
    engine.setProperty('pitch', pitch)  # Pitch level (50 to 200)
    engine.setProperty('language', language)  # Language code

    # Speak the provided text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# Get input from the user
# input_text = input("Enter the text you want to speak: ")
input_text="somethin"
# Set customization parameters
custom_rate = 150  # Adjust as needed
custom_volume = 0.7  # Adjust as needed
custom_pitch = 150 # Adjust as needed # NOT WORKING
custom_language = 'en'  # Adjust as needed #NOT WORKING

# Call the function to speak the input text with customization
speak(input_text, custom_rate, custom_volume, custom_pitch, custom_language)

#----------------------------------
# import pyttsx3

# engine = pyttsx3.init()

# voices = engine.getProperty("voices")

# for voice in voices:
#     print(voice)

#------------------------------------------
