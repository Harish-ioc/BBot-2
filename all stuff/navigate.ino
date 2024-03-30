/*
  GY-511 Compass
  modified on 05 Sep 2020
  by Mohammad Reza Akbari @ Electropeak
  Home

  Library: https://github.com/pololu/lsm303-arduino
*/

// I2C Library
#include <Wire.h>
// LSM303 Compass Library
#include <LSM303.h>

LSM303 cmps;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  cmps.init();
  cmps.enableDefault();

  Serial.println("Setup complete...");
  
  /*
  Calibration values; the default values of +/-32767 for each axis
  lead to an assumed magnetometer bias of 0. Use the Calibrate example
  program to determine appropriate values for your particular unit.
  */
  cmps.m_min = (LSM303::vector<int16_t>){-32767, -32767, -32767};
  cmps.m_max = (LSM303::vector<int16_t>){+32767, +32767, +32767};
}

void loop() {
  cmps.read();
  
  float heading = cmps.heading();

  Serial.print("Heading:  ");
  Serial.println(heading);
  delay(200);
}