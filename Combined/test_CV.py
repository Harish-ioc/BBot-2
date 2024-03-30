import cv2
import serial
import mediapipe as mp

def face_detect():
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
                    print(face_center)
                    print(w)

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


                    
                    if call==True:
                        if face_center[0]>670:
                            print("Move right")
                        if face_center[0]<570:
                            print("move left ")
                        if face_center[1]>370:
                            print("move up")
                        if face_center[1]<270:
                            print("move down")
                        
                    if face_center[0]<670 and face_center[0]>570 and face_center[1]<370 and face_center[1]>270:
                        call=False

                    # if w<230:
                    #     print("move forward !")
                    if w>480:
                        print("move backward !")



                    # valx=str(face_center[0])
                    # valy=str(face_center[1])
                    # value=valx+','+valy

                    # send_to_speak(value)


            else:
                # ser.write(buffer.encode())
                print(buffer)  
            # print("Bahar ....")
            cv2.imshow('Face Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break 
    cap.release()
    cv2.destroyAllWindows()

"""
import cv2
import serial
import mediapipe as mp
# import subprocess
# import test_recive

# def send_to_speak(data_in):
#     test_recive.speak(data_in)


# arduino_port = 'COM7'
# face_cascade = cv2.CascadeClassifier('opencv_practice\haarcascade_frontalface_default.xml')
# ser = serial.Serial(arduino_port, 9600)
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
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
                print(face_center)

                # valx=str(face_center[0])
                # valy=str(face_center[1])
                # value=valx+','+valy

                # send_to_speak(value)


        else:
            # ser.write(buffer.encode())
            print(buffer)  
        print("Bahar ....")
        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break 
cap.release()
cv2.destroyAllWindows()


"""