from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="508eb6b61b5c09fe7ec0c653a61c25d0", # Defaults to ELEVEN_API_KEY
)

def speak(line):
    # text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
    audio = client.generate(text=line,voice="Gigi",model="eleven_multilingual_v1")
    play(audio)

if __name__=="__main__":
    print("")

