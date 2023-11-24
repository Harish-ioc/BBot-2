import serial
import time

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.wrsate(x.encode())  # Encoding the string and sending it
    time.sleep(0.03)
    data = arduino.readline().decode()  # Decoding the received bytes to string
    return data

def write(x):
    arduino.write(x.encode())
    time.sleep(0.05)

def read():
    data=arduino.readline().decode()
    return data

while True:
    text = input("Enter a string: ")
    value = write_read(text) 
    
    
"""
1=happy
2=wink
3=anger
"""


"""
# Associated Arduino Code

String message;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  message = Serial.readStringUntil('\n'); // Read string until newline character
  message.trim(); // Remove potential whitespace

  // Perform some operation on the received string (example: convert to uppercase)
  message.toUpperCase();

  Serial.println(message); // Send back the modified string
}

"""
