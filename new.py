from Google_speech_to_text import listen
from eleven_labs import speak
from calling import ask

while True:
    que = listen()
    ans = ask(str(que))
    speak(str(ans))

    