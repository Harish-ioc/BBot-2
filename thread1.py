from Serial_send import *
import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define the static bounding box in the middle of the screen
static_box_center = (320, 240)  # (x, y) coordinates
static_box_size = (350, 350)     # width, height

# Start capturing video from the default camera (0)
video_capture = cv2.VideoCapture(0)

#-----------
def watch():
# while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw static bounding box
    static_box_x, static_box_y = static_box_center
    static_box_w, static_box_h = static_box_size
    cv2.rectangle(frame, (static_box_x - static_box_w//2, static_box_y - static_box_h//2),
                    (static_box_x + static_box_w//2, static_box_y + static_box_h//2), (0, 255, 0), 2)

    # Draw rectangles around the detected faces and check for movement
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Check if the face is moving out of the static box
        if x < static_box_x - static_box_w//2:
            print("Left")
            write("L")
        elif x + w > static_box_x + static_box_w//2:
            print("Right")
            write("R")
        elif y < static_box_y - static_box_h//2:
            print("Up")
            write("U")
        elif y + h > static_box_y + static_box_h//2:
            print("Down")
            write("D")
        else:
            print("Center")
            write("C")

    # Display the frame
    # cv2.imshow('Face Detection', frame)

    # # Check for the 'q' key to exit the loop
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    # Release the video capture object and close all OpenCV windows
    # video_capture.release()

if __name__=="__main__":
    # watch()
    print("")