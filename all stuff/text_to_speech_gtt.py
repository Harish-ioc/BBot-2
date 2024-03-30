# from gtts import gTTS
# import os

# def speak_with_customization(text, lang, rate, volume, pitch):
#     tts = gTTS(text=text, lang=lang, slow=False)
#     tts.save("output.mp3")

#     # Play the generated MP3 file
#     os.system("start output.mp3")

# # Get input from the user
# input_text = input("Enter the text you want to speak: ")

# # Get customization parameters from the user
# custom_lang = input("Enter the language code (e.g., en): ")
# custom_rate = float(input("Enter the rate (e.g., 1.0): "))
# custom_volume = float(input("Enter the volume (e.g., 1.0): "))
# custom_pitch = float(input("Enter the pitch (e.g., 1.0): "))

# # Call the function to speak the input text with customization
# speak_with_customization(input_text, custom_lang, custom_rate, custom_volume, custom_pitch)
#-----------------------------------------------------------------------------------------------------------------------
# (   generating audio in multiple languages but unable to play it )

# from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play
# import os

# def speak_with_customization(text, lang, rate, volume, pitch):
#     tts = gTTS(text=text, lang=lang, slow=False)
    
#     # Save the gTTS audio to a temporary file
#     audio_path = "temp.mp3"
#     tts.save(audio_path)

#     # Convert the gTTS audio to Pydub AudioSegment
#     audio = AudioSegment.from_mp3(audio_path)

#     # Adjust volume (optional)
#     audio = audio - 20 * (1 - volume)

#     # Play the audio
#     play(audio)

#     # Clean up: Remove the temporary file
#     os.remove(audio_path)

# # Get input from the user
# input_text = "attractive"
# # input("Enter the text you want to speak: ")

# # Get customization parameters from the user
# custom_lang = input("Enter the language code (e.g., en): ")
# custom_rate = 1
# # float(input("Enter the rate (e.g., 1.0): "))
# custom_volume = 1
# # float(input("Enter the volume (e.g., 1.0): "))
# custom_pitch = 1
# # float(input("Enter the pitch (e.g., 1.0): "))

# # Call the function to speak the input text with customization
# speak_with_customization(input_text, custom_lang, custom_rate, custom_volume, custom_pitch)

#----------------------------------------------------------------------


# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = '無理をしないで、君はどうせ素晴らしいんだから！'
  
# Language in which you want to convert 
language = 'ja'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("welcome.mp3") 