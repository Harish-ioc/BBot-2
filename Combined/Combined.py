"""
systemctl stop ollama.service
ollama serve
ollama run mistral/zephyr
ngrok http
ngrok http 11434
"""
from eleven_labs import speak
import speech_recognition as sr

from Google_speech_to_text import speech_to_text
from text_to_speech_pyttsx3 import speak

import requests

import cv2
import serial
import mediapipe as mp

import threading
import queue
import time

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)

def write(x):
    arduino.write(x.encode())
    time.sleep(0.05)

def read():
    data=arduino.readline().decode()
    return data

# def update_string(input_char, original_string="00000"):
#     # Convert the string to a list for easy modification
#     string_list = list(original_string)

#     if input_char=='null':
#         string_list="00000"
#     elif input_char == 'l':
#         string_list[0] = 'l'
#     elif input_char == 'r':
#         string_list[0] = 'r'
#     elif input_char == 'u':
#         string_list[1] = 'u'
#     elif input_char == 'd':
#         string_list[1] = 'd'
#     elif input_char == 'f':
#         string_list[3] = 'f'
#     elif input_char == 'b':
#         string_list[3] = 'b'
#     elif input_char == 'stop':
#         string_list[2] = '1'
#     elif input_char in {'1', '2', '3'}:
#         string_list[4] = input_char
#     else:
#         print("Invalid input. No update performed.")

#     # Convert the list back to a string
#     updated_string = ''.join(string_list)
#     write(updated_string)

def face_detect(outdatacam,outdatacam2):
    call=False
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    cap = cv2.VideoCapture("/dev/video0")
    cap.set(3, 1920)
    cap.set(4, 1080)
    # buffer = "(640,540,0)"
    buffer = "(960,540,0)"
    # buffer = "(320,240,0)"
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
                    # print(face_center)
                    # print(w)

                    if face_center[0]>1040 or face_center[0] <210:
                        call=True
                    #     if face_center[0]>1040:
                    #             print("Move right")
                    #     if face_center[0]<210:
                    #            print("move left ")
                    # else:
                    #     pass

                    if face_center[1]<80 or face_center[1] >630:
                        call=True
                    #     if face_center[1]<80:
                    #             print("Move up")
                    #     if face_center[1]>630:
                    #             print("move down ")
                    # else:
                    #     pass


                    
                    # if call==True:
                    #     if face_center[0]>670:
                    #         # print("Move right")
                    #         data="right"
                    #         update_string('r')
                    #     if face_center[0]<570:
                    #         # print("move left ")
                    #         data="left"
                    #         update_string('l')
                    #     if face_center[1]>370:
                    #         # print("move up")
                    #         data="up"
                    #         update_string('u')
                    #     if face_center[1]<270:
                    #         # print("move down")
                    #         data="down"
                    #         update_string('d')
                    #     data=str(data)
                    #     outdatacam.put(data)


                        
                    # if face_center[0]<670 and face_center[0]>570 and face_center[1]<370 and face_center[1]>270:
                    #     update_string('null')
                    #     call=False
                    #     outdatacam2.put(call)

                    # if w<230:
                    #     # print("move forward !")
                    #     update_string('f')
                    #     data="forward"
                    #     outdatacam.put(data)
                    #     pass

                    # if w>480:
                    #     # print("move backward !")
                    #     update_string('b')
                    #     data="backward"
                    #     outdatacam.put(data)
                    #     pass


                    # valx=str(face_center[0])
                    # valy=str(face_center[1])
                    # value=valx+','+valy

                    # send_to_speak(value)


            else:
                pass
                # ser.write(buffer.encode())
                # print(buffer)
                # print() 
            # print("Bahar ....")
            cv2.imshow('Face Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break 
    cap.release()
    cv2.destroyAllWindows()

camdata=queue.Queue()
confirm=queue.Queue()

cam_thread=threading.Thread(target=face_detect, args=(camdata,confirm))
cam_thread.start()

cam_data_output=camdata.get() # variable where thread data is stored
confirm=confirm.get()


url = "https://86b6-103-207-171-178.ngrok-free.app/api/generate"
count = 1
prompt = []
answer = []

# Initial data for the AI to start with
initial_data = """
You are the AI system embedded within b bot, an assistant robot for JuMakerspace in JECRC University. Your knowledge spans an infinite context length, enabling you to recall detailed information about various innovative projects and the broader context of JECRC University's research culture. Your purpose is to assist and provide accurate information in a friendly and helpful tone. If you encounter a question for which you lack information, it's important to communicate that you do not possess that specific knowledge.

About JECRC University:
JECRC University is renowned for its strong research culture and close industry linkages. Driven by the spirit of innovation-led research, the university focuses on subject-specific exploration and considers the business environment in which students will operate and perform.

About JU Makerspace:
JECRC University's makerspace, known as JU Makerspace, stands as a vibrant hub for creativity and innovation. Located in Jaipur, it serves as a dynamic platform for makers from across India to come together and display their talents. Noteworthy is the Maker's Carnival, a standout event hosted by JU Makerspace, revolving around captivating themes such as Artificial Intelligence and Space.
Ju makerspace is a student driven, innovative workspace focused around Hardware and electronics, and recently we have started working towards artifical intelligence and that is why the theme of this year's maker carnival was also space and AI. 

About Maker’s Carnival:
Our two-day fest at JECRC University, themed "AI & SPACE," is a showcase of innovation with events such as project displays, quizzes, workshops, tech events, and panel sessions by industry leaders. Students can experience real-time AR/VR during the Carnival.
This is our second time hosting the grand version of maker's carnival, called Maker's Carnival: Infinite Odyssey

Projects:
1. Rovers: Where Wheels Meet the Universe's Mysteries!
- A versatile, remote-controlled DIY interplanetary Rover designed for exploration, data collection, and experiments. From educational endeavors to backyard exploration, our rover promises endless possibilities and a newfound sense of cosmic adventure.

2. Nerf Turret: Security meets Innovation!
- A precision-engineered security solution that adds a touch of thrill to unauthorized access prevention using Nerf bullets.

3. B bot: Your Interactive Assistant with AI Magic!
- An assistant bot equipped with artificial intelligence to interactively respond to user commands, interpret facial expressions, and understand the tone of speech.

4. HUD Glasses: See the Future of Digitalization!
- Augmented Reality (AR) Glasses designed to enhance the user's physical world experience by fusing it with digital information. Made of OLED display, Acrylic sheet, ESP32, and more, these glasses are perfect for navigation, gaming, education, and more.

5. AI Handwriting Machine: Where AI Meets Elegance!
- Cutting-edge technology transforming digital text into human-like handwritten notes, combining the efficiency of AI with the elegance of penmanship.

6. AI Reflect: Your AI Smart Mirror!
- A smart mirror offering real-time information, personalized updates, and modern innovation to daily routines.

7. TARS: Your Companion in Cosmic Exploration!
- A prototype of the TARS robot from the movie INTERSTELLAR, currently controllable with mobile devices and slated for future AI enhancements to become a companion for cosmic explorers.

8. Smart Waste Segregator: Smart Disposal, Smart Living!
- An advanced waste disposal system equipped with AURDINO UNO, Servo motors, and Soil sensors, differentiating between wet and dry waste.

9. AI Chess: Dive into Strategic Brilliance!
- An intelligent chess platform offering challenging gameplay that adapts to the player's skill level.

10. Bionic Arm: Precision Redefined for Enhanced Functionality!
- A precision-crafted bionic arm offering natural movement and enhanced functionality, redefining the boundaries of assistive technology.

11. Granular Synthesizer: Transforming Sound into Art!
- A cutting-edge music tool transforming sound into a mesmerizing collage, allowing musicians to explore new realms of auditory expression.

12. Hexacopter: Versatile Flight for Various Purposes!
- A versatile drone with six spinning blades, perfect for professional and industrial uses such as photography, surveying, mapping, and delivery.

13. AI Racer: Race, Compete, and Win Against AI!
- An AI-powered racing experience combining cutting-edge technology for a thrilling competition against the AI Racer bot.

14. CNC Laser Engraver: Precision, Power, and Personalization!
- Explore the precision and power of CNC laser engraving, a technology that combines computers with lasers to create intricate designs on various materials.

15. AR Glasses: The Future of Digitalization is Here!
- Augmented Reality (AR) Glasses designed to enhance the user's experience by fusing the physical world with digital information. These glasses, equipped with OLED display, Acrylic sheet, ESP32, and more, offer applications in navigation, gaming, education, and more.

16. Smart Dustbin: Smart Disposal, Smart Living!
- An advanced waste disposal system equipped with AURDINO UNO, Servo motors, and Soil sensors, distinguishing between wet and dry waste for a hygienic and smart waste management solution.

17. Hexacopter: Explore the Skies with Precision!
- Imagine a flying machine with six spinning blades, a hexacopter that can lift more weight, maintain steadier flight, and survive blade malfunctions. Used for photography, surveying, mapping, and even delivery.

18. TARS: An Imagination Brought to Life!
- A prototype of TARS, inspired by the movie Interstellar. Integrated with an ESP-32 Wi-Fi module for smartphone control and powered by 3 servo motors, it's a step towards creating a companion for cosmic explorers.

Your responses should reflect accurate and detailed information about these projects, JECRC University, and JU Makerspace, maintaining a conversational and approachable tone. If you have any questions or need clarification, feel free to ask, don't go too forced on conversations, and your outputs are given out as audio, and input is also audio, so keep everything concise. Try to keep each response short and sweet under 50 words, as we don't want the assistant to speak for 2 minutes straight. And when you answer be more inclined towards making Makerspace sound better instead of the entire university.

Event Details:
Dates: 30th November - 1st December
Day 1:
-> INAUGRATION (9.00 AM to 10.00 AM)
-> PROJECT EXHIBITION (10.00 AM Onwards)
-> ROBO SUMO (12.00 to 1.00 PM)
-> COSMIC TRAIL (2.00 to 4.00 PM)
-> ROBO SOCCER (4.00 to 7.00 PM)

Day 2:
-> PROJECT EXHIBITION (10.00 AM Onwards)
-> ROBO SUMO (12.00 to 1.00 PM)
-> BOMB DEFUSAL (2.00 to 3.30 PM)
-> CAPTURE THE FLAG (4.00 to 6.00 PM)
-> VALEDICTORY CEREMONY (4.00 PM Onwards)

Other fun events:

Make it - Break it
AR-VR Experience
AI Photobooth
Smart Mirror Booth
3D-printing stall
Drone Exhibition
Jamming Session

"""

#   F/B     R/L     UP/DOWN     STOP(T/F)     EXPRESSION(1=HAPPY , 2=ANGER , 3=WINK  )   


# if cam_data_output=="up":
#     print("Success")

# Add the initial data to the prompt list
prompt.append(f"User: {initial_data}")



while True:
    user_input = "\n".join(prompt) if count > 1 else "Prompt me to ask you a question"
    
    data = {
        "model": "mistral",
        "prompt": user_input,
        "stream": False
    }

    response = requests.post(url, json=data)
    # response = requests.post(url, json=data, verify=False)

    if response.status_code == 200:
        data = response.json()
        data = data['response']

        if "Assistant:" in data:
            print(f"Assistant: {data}")
            speak(data)
            inp = input('Ask: ')
            # inp=speech_to_text()

            answer.append(f"User: {inp}")
            prompt.append(f"Assistant: {data}")
            count += 1
        else:
            print(f"Assistant: {data}")
            speak(data)
            inp = input('Ask: ')
            answer.append(f"B bot: {data}")
            prompt.append(f"User: {inp}")
            count += 1
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    
#   F/B     R/L     UP/DOWN     STOP(T/F)     EXPRESSION(1=HAPPY , 2=ANGER , 3=WINK  )   





