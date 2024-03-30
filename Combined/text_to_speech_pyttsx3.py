# """
# import pyttsx3
 

# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty('voices')
# # engine.setProperty('language', 'zh')
# #print(voices[1].id)
# engine.setProperty('voice',voices[1].id)

# engine.setProperty("rate", 150)      #(  SPEED INCRESES WITH INCRESE IN NUMBER   )
# engine.setProperty("volume", 1)      #(  MAX:1 , MIN:0   )
# # engine.setProperty("pitch", 150)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
    

# audio=("the text is this ? for sure ?")
# speak(audio)

# """

# import pyttsx3

# def speak(text):
#     # Initialize the text-to-speech engine
#     # engine = pyttsx3.init('sapi5')
#     engine = pyttsx3.init('sapi5')

#     rate = 100  # Adjust as needed
#     volume = 1 # Adjust as needed


#     # Customize voice properties
#     engine.getProperty('rate')
#     engine.getProperty('volume')

#     voices = engine.getProperty('voices')
#     engine.setProperty('voice',voices[1].id)


#     engine.setProperty('rate', rate)  # Speed of speech
#     engine.setProperty('volume', volume)  # Volume level (0.0 to 1.0)

#     # Speak the provided text
#     engine.say(text)

#     # Wait for the speech to finish
#     engine.runAndWait()


# speak(" this is my shity voice ! ")
# # speak("testing the audio output !")

# # Get input from the user
# # input_text = input("Enter the text you want to speak: ")
# # Set customization parameters

# # Call the function to speak the input text with customization

# #----------------------------------
# # import pyttsx3

# # engine = pyttsx3.init()

# # voices = engine.getProperty("voices")

# # for voice in voices:
# #     print(voice)

# #------------------------------------------
# # speak("resting")


import pyttsx3

def speak(text):
    # Initialize the text-to-speech engine with SAPI5
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# Example usage
