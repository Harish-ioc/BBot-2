from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="af42a0a96978450565a933e63163af62", # Defaults to ELEVEN_API_KEY
)

def speak(line):
    # text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
    audio = client.generate(text=line,voice="Adam",model="eleven_multilingual_v1")
    play(audio)

if __name__=="__main__":
    # speak("hbhjk")
    print("")

