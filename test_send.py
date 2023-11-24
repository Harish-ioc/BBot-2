import subprocess
import test_recive
# script_path = "test_recive.py"

# def send_to_speak(data_in):
    # subprocess.run(["python", script_path, data_in])
def send_to_speak(data_in):
    test_recive.speak(data_in)

send_to_speak("hell")