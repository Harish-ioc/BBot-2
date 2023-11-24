import json
import random
import serial
import time
import speech_recognition as sr
import smtplib
import pyttsx3
import cv2
import serial
import mediapipe as mp




server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
# buffer = "(640,540,0)"
buffer = "(960,540,0)"
# buffer = "(320,240,0)"

#-- -- ( BBot login ) -- --
Bbot_email="junk90yard@gmail.com"
Bbot_pass="tesu tkfd pikb qlza"
server.login(Bbot_email,Bbot_pass)


# -- unable when COMPORT is available --
# arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
# def write_read(x):
#     arduino.wrsate(x.encode())  # Encoding the string and sending it
#     time.sleep(0.03)
#     data = arduino.readline().decode()  # Decoding the received bytes to string
#     return data

# def write(x):
#     arduino.write(x.encode())
#     time.sleep(0.05)

# def read():
#     data=arduino.readline().decode()
#     return data
# -- --- -- -- -- -- -- -- -- -- 


def speak(text):
    # Initialize the text-to-speech engine

    rate=150
    volume=0.7
    pitch=150
    language='en'
    
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

def listen():
    try:    
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Speak...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text = text.lower()
        text=str(text)
        print("You : ",text)

        return text
    except sr.UnknownValueError:
        print("No speech detected ! ")

def load_json_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def respond_to_user_input(user_input, json_context):
    user_input=str(user_input)
    user_words = user_input.lower().split()

    best_match_key = None
    max_matching_words = 0

    for context_dict in json_context:
        for key, value_list in context_dict.items():
            matching_words = len(set(user_words) & set(key.split()))
            if matching_words > max_matching_words:
                max_matching_words = matching_words
                best_match_key = key

    if best_match_key is not None:
        response_list = next(item[best_match_key] for item in json_context if best_match_key in item)
        return random.choice(response_list)
    else:
        return "I'm sorry, I didn't understand that. Please try again."


#--- ( Functions for notes  v ) ----

def add_note(note):
    with open('notes.txt', 'a') as file:
        file.write(note + '\n')

def list_notes():
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
        if notes:
            print("List of Notes:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note}")
        else:
            print("No notes found.")

def latest_note():
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
        if notes:
            latest = notes[-1]
            print("Latest Note:")
            print(latest)
        else:
            print("No notes found.")

def oldest_note():
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
        if notes:
            oldest = notes[0]
            print("Oldest Note:")
            print(oldest)
        else:
            print("No notes found.")

def delete_note_by_number(note_number):
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
    
    if 0 < note_number <= len(notes):
        del notes[note_number - 1]
        with open('notes.txt', 'w') as file:
            file.writelines(notes)
        print("Note deleted successfully.")
    else:
        print("Note number out of range. No note deleted.")

def delete_note_by_content(content):
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
    
    filtered_notes = [note for note in notes if content not in note]
    with open('notes.txt', 'w') as file:
        file.writelines(filtered_notes)
    print("Notes containing the specified content are deleted.")

def clear_notes():
    open('notes.txt', 'w').close()
    print("All notes cleared.")

#----------         --          -------

file_path = 'data.json'
json_context = load_json_from_file(file_path)

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)
        if results.detections:
            for detection in results.detections[0:1]:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # Green
                cv2.rectangle(frame, (210,80), (1040, 630), (255,0 , 0), 2)  # Blue
                cv2.rectangle(frame,(570,270),(670,370),(0,0,255),2)   # Red
                
                face_center=(x+(w//2),y+(h//2))
                cv2.circle(frame,center=face_center,radius=2,color=(0,0,0))
                str_cord = f"(x={x},y={y},width={w},height={h})"
                buffer = f"(960,{y},0)"
                # ser.write(str_cord.encode())
                print(face_center)
        else:
            # ser.write(buffer.encode())
            print(buffer)  
        # print("Bahar ....")
        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break 

    # user_input = listen()
        user_input=input("You : ")
        if user_input=="exit":
            print("Exiting...")
            break
        if "send" and "mail" in user_input:
            print("ok !")
            print("on which email address ? ")
            receiver_email= listen().replace(" ","")

            print("what do you wanna say ?")
            content=listen()
            print("Understood !")
            print("Now, let me see !")

            try:
                server.sendmail(Bbot_email,receiver_email,content)
                print("Ok. Its gone !")
            except:
                print("oops ! something went wrong.")

        # Notes ---
        if "add" and "note" in user_input:
            new_note = input("Enter your note: ")
            add_note(new_note)
        elif "what" and "notes" in user_input:
            list_notes()
        elif "what" and "latest" and "notes" in user_input:
            latest_note()
        elif "what" and "oldest" and "notes" in user_input:
            oldest_note()
        elif "delete" and "note" and "number" in user_input:
            note_num = int(input("Enter the note number to delete: "))
            delete_note_by_number(note_num)
        elif "delete" and "note" and "content" in user_input:
            content_to_delete = input("Enter the content to delete: ")
            delete_note_by_content(content_to_delete)
        elif "clear" and "all" and "notes" in user_input:
            clear_notes()
                

        response = respond_to_user_input(user_input, json_context)
        print("Bot : ",response)
            
cap.release()
cv2.destroyAllWindows()

