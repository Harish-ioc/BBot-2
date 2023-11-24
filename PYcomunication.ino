
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
