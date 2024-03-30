#include <LedControl.h> // include led control library
#include <Wire.h>
#include <Servo.h>

//#include <Adafruit_MPU6050.h>
//#include <Adafruit_Sensor.h>
//#include <Wire.h>
//Adafruit_MPU6050 mpu;

Servo servo;



int DIN=2; // define DIN pin to digital pin 10
int CS=3; // define CS pin to digital pin 11
int CLK=4; // define CLK to digital pin 12

int din_mid=5;
int cs_mid=6;
int clk_mid=7;

int brightness=5;  // 0 to 15

//---------------------------------------------------------------------------(  MOTION   )----------------------------

int Lpin=5;
int Rpin=6;

int Lb=8;
int Lf=9;
int Rb=10;
int Rf=11;



// byte s[]=   {0xB77C,0x00,0x7C,0x60,0x7C,0x0C,0x7C,0x00}; // letter s byte arrays custom character
// byte t[]=   {0x00,0x00,0x7C,0x10,0x10,0x10,0x10,0x00}; // letter t byte arrays custom character
// byte e1[]=  {0x00,0x00,0x78,0x40,0x70,0x40,0x78,0x00}; // letter e byte arrays custom character
// byte e2[]=  {0x00,0x00,0x78,0x40,0x70,0x40,0x78,0x00};
// byte m[]=   {0x00,0x00,0x44,0x6C,0x54,0x44,0x44,0x00}; // lett er m byte arrays custom character
// byte i[]=   {0x00,0x10,0x00,0x10,0x10,0x10,0x38,0x00}; // letter i byte arrays custom character
// byte T[]=   {0x00,0x00,0x7C,0x10,0x10,0x10,0x10,0x00};

LedControl lc=LedControl(DIN,CLK,CS,0);  // chain length or the variable 0 has to be changed if Hex code is used

LedControl lc_m=LedControl(din_mid,clk_mid,cs_mid,0);

bool t=true;
bool f=false;

int speed(int& left,int& right){

  left=map(left,0,1000,0,255);
  right=map(right,0,1000,0,255);

}


int randomnumber(int min, int max) {
  // Initialize the random seed
  randomSeed(analogRead(A0)); // Use an analog pin to generate a random seed

  // Generate a random number within the given range
  int randomNumber = random(min, max + 1); // '+1' to include the 'max' value

  return randomNumber;
}

void glow(int section,int row,int Llimit,int Ulimit,bool true_false){
  for(int i=Llimit;i<=Ulimit;i++){
    lc.setLed(section,row,i,true_false);
  }
}
void glow_m(int section,int row,int Llimit,int Ulimit,bool true_false){
  for(int i=Llimit;i<=Ulimit;i++){
    lc_m.setLed(section,row,i,true_false);
  }
}

void clear(){
  lc_m.clearDisplay(0);lc_m.clearDisplay(1);lc_m.clearDisplay(2);lc_m.clearDisplay(3);
  lc.clearDisplay(0);lc.clearDisplay(1);lc.clearDisplay(2);lc.clearDisplay(3);
  lc.clearDisplay(4);lc.clearDisplay(5);lc.clearDisplay(6);lc.clearDisplay(7);

}



void blink(int blink_speed){  

int btwCO = randomnumber(10,5000);  // btwCO = delay between eye closing and opening

glow_m(1,1,2,6,t); glow_m(2,1,1,5,t); // L1
glow_m(1,2,1,7,t); glow_m(2,2,0,6,t); // L2
glow_m(1,3,1,7,t); glow_m(2,3,0,6,t); // L3
glow_m(1,4,1,7,t); glow_m(2,4,0,6,t); // L4
glow_m(1,5,1,7,t); glow_m(2,5,0,6,t); // L5  // not closed 
glow_m(1,6,1,7,t); glow_m(2,6,0,6,t); // L6
glow_m(1,7,2,6,t); glow_m(2,7,1,5,t); // L7

delay(btwCO);

// eye closing -------
glow_m(1,1,2,6,f); glow_m(2,1,1,5,f); // L1
delay(blink_speed);
glow_m(1,7,2,6,f); glow_m(2,7,1,5,f); // L7
delay(blink_speed);
glow_m(1,2,1,7,f); glow_m(2,2,0,6,f); // L2
delay(blink_speed);
glow_m(1,3,1,7,f); glow_m(2,3,0,6,f); // L3
delay(blink_speed);
glow_m(1,6,1,7,f); glow_m(2,6,0,6,f); // L6
delay(blink_speed);
glow_m(1,4,1,7,f); glow_m(2,4,0,6,f); // L4
delay(blink_speed);

// Closed 
// Eye Opening--------
glow_m(1,4,1,7,t); glow_m(2,4,0,6,t); // L4
delay(blink_speed);
glow_m(1,6,1,7,t); glow_m(2,6,0,6,t); // L6
delay(blink_speed);
glow_m(1,3,1,7,t); glow_m(2,3,0,6,t); // L3
delay(blink_speed);
glow_m(1,2,1,7,t); glow_m(2,2,0,6,t); // L2
delay(blink_speed);
glow_m(1,7,2,6,t); glow_m(2,7,1,5,t); // L7
delay(blink_speed);
glow_m(1,1,2,6,t); glow_m(2,1,1,5,t); // L1
delay(blink_speed);

}
void cry(){
  clear();
  //Right Eye
  glow_m(0, 1, 3, 7, t);glow_m(1, 1, 0, 3, t);
  glow_m(0, 2, 3, 7, t);glow_m(1, 2, 0, 3, t);
  //Left Eye
  glow_m(2, 1, 4, 7, t);glow_m(3, 1, 0, 4, t);
  glow_m(2, 2, 4, 7, t);glow_m(3, 2, 0, 4, t);
  //Tear Right Eye
  lc_m.setLed(0, 3, 6, t);lc_m.setLed(0, 3, 7, t);lc_m.setLed(1, 3, 0, t);
  lc_m.setLed(0, 4, 6, t);lc_m.setLed(0, 4, 7, t);lc_m.setLed(1, 4, 0, t);
  lc_m.setLed(0, 5, 6, t);lc_m.setLed(0, 5, 7, t);lc_m.setLed(1, 5, 0, t);
  lc_m.setLed(0, 6, 6, t);lc_m.setLed(0, 6, 7, t);lc_m.setLed(1,6, 0, t);
  lc_m.setLed(0, 7, 6, t);lc_m.setLed(0, 7, 7, t);lc_m.setLed(1, 7, 0, t);
  //Tear Left Eye
  lc_m.setLed(2,3,7,t);lc_m.setLed(3, 3, 0, t);lc_m.setLed(3, 3, 1, t);
  lc_m.setLed(2,4,7,t);lc_m.setLed(3, 4, 0, t);lc_m.setLed(3, 4, 1, t);
  lc_m.setLed(2,5,7,t);lc_m.setLed(3, 5, 0, t);lc_m.setLed(3, 5, 1, t);
  lc_m.setLed(2,6,7,t);lc_m.setLed(3, 6, 0, t);lc_m.setLed(3, 6, 1, t);
  lc_m.setLed(2,7,7,t);lc_m.setLed(3, 7, 0, t);lc_m.setLed(3, 7, 1, t);
}

void satisfied(){
  clear();
  //Right Eye
  lc_m.setLed(0, 1, 2, t);lc_m.setLed(0, 2, 3, t);
  lc_m.setLed(0, 3, 4, t);lc_m.setLed(0, 3, 5, t);lc_m.setLed(0, 3, 6, t);
  lc_m.setLed(0, 3, 7, t);
  lc_m.setLed(1, 2, 0, t);lc_m.setLed(1, 1, 1, t);
  //Left Eye
  lc_m.setLed(2, 1, 6, t);lc_m.setLed(2, 2, 7, t);
  lc_m.setLed(3, 3, 0, t);
  lc_m.setLed(3, 3, 1, t);
  lc_m.setLed(3, 3, 2, t);
  lc_m.setLed(3, 3, 3, t);
  lc_m.setLed(3, 2, 4, t);
  lc_m.setLed(3, 1, 5, t);
}

void surprised(int wait){
  clear();
  //Right Eye Suprised
  lc_m.setLed(1, 0, 7, t);lc_m.setLed(0, 0, 0, t); lc_m.setLed(0, 0, 1, t);
  lc_m.setLed(0, 1, 2, t);lc_m.setLed(0, 1, 2, t);lc_m.setLed(0, 1, 2, t);
  lc_m.setLed(1, 1, 6, t);
  lc_m.setLed(0, 2, 2, t);lc_m.setLed(0, 3, 2, t);lc_m.setLed(0, 4, 2, t);
  lc_m.setLed(0, 5, 2, t); lc_m.setLed(0, 5, 2, t); lc_m.setLed(0, 6, 2, t);
  lc_m.setLed(0, 7, 1, t);lc_m.setLed(0, 7, 0, t);lc_m.setLed(1, 7, 7, t);
  lc_m.setLed(1, 6, 6, t);lc_m.setLed(1, 5, 6, t);lc_m.setLed(1, 4, 6, t);
  lc_m.setLed(1, 3, 6, t);lc_m.setLed(1, 2, 6, t);
  //Left Eye Suprised
  lc_m.setLed(3, 0, 6, t); lc_m.setLed(3, 0, 7, t); lc_m.setLed(2, 0, 0, t);
  lc_m.setLed(2, 1, 1, t); lc_m.setLed(2, 2, 1, t); lc_m.setLed(2, 3, 1, t);
  lc_m.setLed(2, 4, 1, t); lc_m.setLed(2, 5, 1, t); lc_m.setLed(2, 6, 1, t);
  lc_m.setLed(2, 7, 0, t); lc_m.setLed(3, 7, 7, t); lc_m.setLed(3, 7, 6, t);
  lc_m.setLed(3, 6, 5, t); lc_m.setLed(3, 5, 5, t); lc_m.setLed(3, 4, 5, t);
  lc_m.setLed(3, 3, 5, t); lc_m.setLed(3, 2, 5, t);lc_m.setLed(3, 1, 5, t);
  delay(wait);

}

void bigeye(){
 clear();
  int hold=randomnumber(1000,2000);
  glow_m(2,1,1,7,t); glow_m(1,1,0,6,t); glow_m(3,1,1,0,t); //glow_m(0,1,1,7,t);// L1
  glow_m(2,0,2,6,t); glow_m(1,0,1,5,t);
  glow_m(2,2,0,7,t); glow_m(1,2,0,7,t); glow_m(3,2,0,1,t); glow_m(0,2,6,7,t); // L2
  glow_m(2,3,0,7,t); glow_m(1,3,0,7,t); glow_m(3,3,0,1,t); glow_m(0,3,6,7,t); // L3
  glow_m(2,4,0,7,t); glow_m(1,4,0,7,t); glow_m(3,4,0,1,t); glow_m(0,4,6,7,t); // L4
  glow_m(2,5,0,7,t); glow_m(1,5,0,7,t); glow_m(3,5,0,1,t); glow_m(0,5,6,7,t); // L5  
  glow_m(2,6,0,7,t); glow_m(1,6,0,7,t); glow_m(3,6,0,1,t); glow_m(0,6,6,7,t); // L6
  glow_m(2,7,0,7,t); glow_m(1,7,0,7,t); glow_m(3,7,0,1,t); glow_m(0,7,6,7,t); // L7
  glow(3,0,0,0,t); glow(2,0,1,7,t); glow(1,0,0,6,t); glow(0,0,7,7,t);
  glow(2,1,2,7,t); glow(1,1,0,5,t); glow(0,0,7,7,t);

  delay(hold);
 
}

void happy(){ // 1 or 2 or 3

  int level=randomnumber(1,3);

  int hold=randomnumber(1000,2000);
  clear();
  if(level==1){
    lc_m.setLed(2,4,5,t); lc_m.setLed(2,3,5,t); 
    lc_m.setLed(2,3,4,t); lc_m.setLed(2,2,4,t);
    lc_m.setLed(2,2,3,t); lc_m.setLed(2,1,3,t);
    lc_m.setLed(2,1,2,t); lc_m.setLed(2,0,2,t);
    lc_m.setLed(2,0,1,t); lc_m.setLed(2,0,0,t);
    lc_m.setLed(2,1,0,t); lc_m.setLed(2,1,1,t);

    // lc.setLed(7,7,0,t); lc.setLed(7,7,1,t); lc.setLed(7,6,0,t);
    // lc.setLed(6,7,7,t); lc.setLed(6,6,7,t); lc.setLed(6,7,6,t);

    lc_m.setLed(3,0,6,t); lc_m.setLed(3,0,5,t);
    lc_m.setLed(3,1,5,t); lc_m.setLed(3,1,4,t);
    lc_m.setLed(3,2,4,t); lc_m.setLed(3,2,3,t);
    lc_m.setLed(3,3,3,t); lc_m.setLed(3,3,2,t);
    lc_m.setLed(3,4,2,t); lc_m.setLed(3,0,7,t);
    lc_m.setLed(3,1,6,t); lc_m.setLed(3,1,7,t);

    lc_m.setLed(0,4,5,t); lc_m.setLed(0,3,5,t);
    lc_m.setLed(0,3,4,t); lc_m.setLed(0,2,4,t);
    lc_m.setLed(0,2,3,t); lc_m.setLed(0,1,3,t);
    lc_m.setLed(0,1,2,t); lc_m.setLed(0,0,2,t);
    lc_m.setLed(0,0,1,t); lc_m.setLed(0,0,0,t);
    lc_m.setLed(0,1,0,t); lc_m.setLed(0,1,1,t);
 
    // lc.setLed(5,7,0,t); lc.setLed(5,7,1,t); lc.setLed(5,6,0,t);
    // lc.setLed(4,7,7,t); lc.setLed(4,6,7,t); lc.setLed(4,7,6,t);

    lc_m.setLed(1,0,6,t); lc_m.setLed(1,0,5,t);
    lc_m.setLed(1,1,5,t); lc_m.setLed(1,1,4,t);
    lc_m.setLed(1,2,4,t); lc_m.setLed(1,2,3,t);
    lc_m.setLed(1,3,3,t); lc_m.setLed(1,3,2,t);
    lc_m.setLed(1,4,2,t); lc_m.setLed(1,0,7,t);
    lc_m.setLed(1,1,6,t); lc_m.setLed(1,1,7,t);
    

  }else if(level==2){

  lc_m.setLed(1,4,3,t); lc_m.setLed(1,4,4,t); lc_m.setLed(2,4,4,t); lc_m.setLed(2,4,3,t); 
  lc_m.setLed(1,3,4,t); lc_m.setLed(1,3,5,t); lc_m.setLed(2,3,2,t); lc_m.setLed(2,3,3,t);
  lc_m.setLed(1,5,4,t); lc_m.setLed(1,5,5,t); lc_m.setLed(2,5,3,t); lc_m.setLed(2,5,2,t);
  lc_m.setLed(1,2,5,t); lc_m.setLed(1,2,6,t); lc_m.setLed(2,2,2,t); lc_m.setLed(2,2,1,t);
  lc_m.setLed(1,6,5,t); lc_m.setLed(1,6,6,t); lc_m.setLed(2,6,2,t); lc_m.setLed(2,6,1,t);
  lc_m.setLed(1,1,6,t); lc_m.setLed(1,1,7,t); lc_m.setLed(2,1,1,t); lc_m.setLed(2,1,0,t);
  lc_m.setLed(1,7,6,t); lc_m.setLed(1,7,7,t); lc_m.setLed(2,7,1,t); lc_m.setLed(2,7,0,t);
  lc_m.setLed(1,0,7,t); lc_m.setLed(2,0,0,t);

  // lc.setLed(7,7,0,t); lc_m.setLed(3,0,0,t);
  lc.setLed(2,0,7,t);  // lc.setLed(3,0,0,t); lc.setLed(3,1,0,t); lc.setLed(0,1,7,t);
  // lc.setLed(4,7,7,t);
  lc.setLed(1,0,0,t); // lc.setLed(0,0,7,t); lc_m.setLed(0,0,7,t);



  }else if(level==3){
        // lc_m.setLed(3,2,5,t); lc_m.setLed(3,3,4,t);
    lc_m.setLed(2,4,3,t); 
    lc_m.setLed(2,3,2,t); lc_m.setLed(2,2,1,t); lc_m.setLed(2,3,0,t);
    // lc_m.setLed(3,4,7,t); lc_m.setLed(3,3,6,t);
    //---
    // lc_m.setLed(3,1,5,t); lc_m.setLed(3,2,4,t);
    lc_m.setLed(2,3,3,t); 
    lc_m.setLed(2,2,2,t); lc_m.setLed(2,1,1,t); lc_m.setLed(2,2,0,t);
    // lc_m.setLed(3,3,7,t); lc_m.setLed(3,2,6,t);
    //-----------------------

    lc_m.setLed(3,4,7,t); lc_m.setLed(3,3,6,t); lc_m.setLed(3,2,5,t);
    lc_m.setLed(3,3,4,t); lc_m.setLed(3,4,3,t);
    //---
    lc_m.setLed(3,3,7,t); lc_m.setLed(3,2,6,t); lc_m.setLed(3,1,5,t);
    lc_m.setLed(3,2,4,t); lc_m.setLed(3,3,3,t);
    //---

    // lc_m.setLed(0,4,0,t); lc_m.setLed(0,3,1,t); lc_m.setLed(0,2,2,t); lc_m.setLed(0,3,3,t);
    lc_m.setLed(1,4,4,t); lc_m.setLed(1,3,5,t);
    lc_m.setLed(1,2,6,t); lc_m.setLed(1,3,7,t);
    //---
    // lc_m.setLed(0,3,0,t); lc_m.setLed(0,2,1,t); lc_m.setLed(0,1,2,t); lc_m.setLed(0,2,3,t); 
    lc_m.setLed(1,3,4,t); lc_m.setLed(1,2,5,t);
    lc_m.setLed(1,1,6,t); lc_m.setLed(1,2,7,t);
    //---
    
    lc_m.setLed(0,4,4,t); lc_m.setLed(0,3,3,t); lc_m.setLed(0,2,2,t);
    lc_m.setLed(0,3,1,t); lc_m.setLed(0,4,0,t);
    //---
    lc_m.setLed(0,3,4,t); lc_m.setLed(0,2,3,t); lc_m.setLed(0,1,2,t);
    lc_m.setLed(0,2,1,t); lc_m.setLed(0,3,0,t);
    //---  
  }
  delay(hold);
 
}

void angry(){ // 1 or 2

  clear();
//  int hold=randomnumber(2000,4000);

  // glow_m(3,2,0,3,t); glow_m(2,2,2,7,t); glow_m(1,2,0,5,t); glow_m(0,2,4,7,t);
  // glow_m(3,3,0,2,t); glow_m(2,3,3,7,t); glow_m(1,3,0,4,t); glow_m(0,3,5,7,t);
  // glow_m(3,4,0,1,t); glow_m(2,4,4,7,t); glow_m(1,4,0,3,t); glow_m(0,4,6,7,t);

  glow_m(2,2,0,3,t); glow_m(3,2,2,7,t); glow_m(0,2,0,5,t); glow_m(1,2,4,7,t);
  glow_m(2,3,0,2,t); glow_m(3,3,3,7,t); glow_m(0,3,0,4,t); glow_m(1,3,5,7,t);
  glow_m(2,4,0,1,t); glow_m(3,4,4,7,t); glow_m(0,4,0,3,t); glow_m(1,4,6,7,t);


//  delay(hold);
    
  
}

void wink(){

clear();
int blink_speed=20;
int hold=randomnumber(800,2000);

glow_m(1,1,2,6,t); glow_m(2,1,1,5,t); // L1
glow_m(1,2,1,7,t); glow_m(2,2,0,6,t); // L2
glow_m(1,3,1,7,t); glow_m(2,3,0,6,t); // L3
glow_m(1,4,1,7,t); glow_m(2,4,0,6,t); // L4
glow_m(1,5,1,7,t); glow_m(2,5,0,6,t); // L5  // not closed 
glow_m(1,6,1,7,t); glow_m(2,6,0,6,t); // L6
glow_m(1,7,2,6,t); glow_m(2,7,1,5,t); // L7

lc_m.setLed(1,2,1,f); lc_m.setLed(1,2,7,f);
lc_m.setLed(1,6,1,f); lc_m.setLed(1,6,7,f);


glow_m(1,1,2,6,f); glow_m(2,1,1,5,f); // L1
delay(blink_speed);
glow_m(1,7,2,6,f); glow_m(2,7,1,5,f); // L7
delay(blink_speed);
glow_m(2,2,0,6,f); // L2
delay(blink_speed);
glow_m(2,3,0,6,f); // L3
delay(blink_speed);
glow_m(2,5,0,6,f); // L5 
delay(blink_speed);
glow_m(2,6,0,6,f); // L6
delay(blink_speed);
glow_m(2,4,0,6,f); // L4
delay(blink_speed);


// glow_m(1,7,2,6,t); glow_m(1,1,2,6,t);

lc_m.setLed(2,4,4,t); lc_m.setLed(2,4,3,t); 
lc_m.setLed(2,3,2,t); lc_m.setLed(2,3,3,t);
lc_m.setLed(2,5,3,t); lc_m.setLed(2,5,2,t);
lc_m.setLed(2,2,2,t); lc_m.setLed(2,2,1,t);
lc_m.setLed(2,6,2,t); lc_m.setLed(2,6,1,t);
// lc_m.setLed(2,1,1,t); lc_m.setLed(2,1,0,t);
// lc_m.setLed(2,7,1,t); lc_m.setLed(2,7,0,t);

delay(hold);


}

void forward(int Lspeed,int Rspeed){
  speed(Lspeed,Rspeed);
  analogWrite(Lf,Lspeed);
  analogWrite(Rf,Rspeed);
  analogWrite(Lb,0);
  analogWrite(Rb,0);
}

void backward(int Lspeed,int Rspeed){
  speed(Lspeed,Rspeed);
  analogWrite(Lb,Lspeed);
  analogWrite(Rb,Rspeed);
  analogWrite(Lf,0);
  analogWrite(Rf,0);
}

void right(int Lspeed,int Rspeed){
  speed(Lspeed,Rspeed);
  analogWrite(Lf,Lspeed);
  analogWrite(Rb,Rspeed);
  analogWrite(Rf,0);
  analogWrite(Lb,0);
}

void left(int Lspeed,int Rspeed){
  speed(Lspeed,Rspeed);
  analogWrite(Lb,Lspeed);
  analogWrite(Rf,Lspeed);
  analogWrite(Rb,0);
  analogWrite(Lf,0);
}

void stop(int Lspeed,int Rspeed){
  speed(Lspeed,Rspeed);
  analogWrite(Lf,0);
  analogWrite(Rb,0);
  analogWrite(Rf,0);
  analogWrite(Lb,0);
}



String command;

void setup(){

  Serial.begin(115200);
//
//  if (!mpu.begin()) {
//  Serial.println("Failed to find MPU6050 chip");
//  while (1) {
//    delay(10);
//    }
//  }
//  Serial.println("MPU6050 Found!");

//  // set accelerometer range to +-8G
//  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
//
//  // set gyro range to +- 500 deg/s
//  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
//
//  // set filter bandwidth to 21 Hz
//  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  delay(100);
  servo.attach(12);
  servo.write(90);

//  pinMode(10,OUTPUT);
  pinMode(Lf,OUTPUT);
  pinMode(Lb,OUTPUT);
  pinMode(Rf,OUTPUT);
  pinMode(Rb,OUTPUT);

  analogWrite(Lf, LOW);
  analogWrite(Lb, LOW);
  analogWrite(Rf, LOW);  
  analogWrite(Rb, LOW);

//  speed(0,0/);
  
 lc.shutdown(0,false);       //The MAX72XX is in power-saving mode on startup
 lc.setIntensity(0,brightness);      // Set the brightness, the maximum is 0,15
 lc.clearDisplay(0);         // and clear the display

 lc_m.shutdown(0,false);       //The MAX72XX is in power-saving mode on startup
 lc_m.setIntensity(0,brightness);      // Set the brightness, the maximum is 0,15
 lc_m.clearDisplay(0);

 //----------

  lc.shutdown(1,false);       //The MAX72XX is in power-saving mode on startup
 lc.setIntensity(1,brightness);      // Set the brightness, the maximum is 0,15
 lc.clearDisplay(1);         // and clear the display

 lc_m.shutdown(1,false);       //The MAX72XX is in power-saving mode on startup
 lc_m.setIntensity(1,brightness);      // Set the brightness, the maximum is 0,15
 lc_m.clearDisplay(1);

 //--------

  lc.shutdown(2,false);       //The MAX72XX is in power-saving mode on startup
 lc.setIntensity(2,brightness);      // Set the brightness, the maximum is 0,15
 lc.clearDisplay(2);         // and clear the display

 lc_m.shutdown(2,false);       //The MAX72XX is in power-saving mode on startup
 lc_m.setIntensity(2,brightness);      // Set the brightness, the maximum is 0,15
 lc_m.clearDisplay(2);

 //------

  lc.shutdown(3,false);       //The MAX72XX is in power-saving mode on startup
 lc.setIntensity(3,brightness);      // Set the brightness, the maximum is 0,15
 lc.clearDisplay(3);         // and clear the display

 lc_m.shutdown(3,false);       //The MAX72XX is in power-saving mode on startup
 lc_m.setIntensity(3,brightness);      // Set the brightness, the maximum is 0,15
 lc_m.clearDisplay(3);

 lc.shutdown(4,false);
 lc.setIntensity(4,brightness);
 lc.clearDisplay(4);

 lc.shutdown(5,false);
 lc.setIntensity(5,brightness);
 lc.clearDisplay(5);

 lc.shutdown(6,false);
 lc.setIntensity(6,brightness);
 lc.clearDisplay(6);

 lc.shutdown(7,false);
 lc.setIntensity(7,brightness);
 lc.clearDisplay(7);


Serial.setTimeout(1);

}
void test(){
  lc.setLed(0,0,0,t);lc.setLed(1,0,0,t);lc.setLed(2,0,0,t);lc.setLed(3,0,0,t);
  lc.setLed(4,0,0,t);lc.setLed(5,0,0,t);lc.setLed(6,0,0,t);lc.setLed(7,0,0,t);

  lc_m.setLed(0,0,0,t);lc_m.setLed(1,0,0,t);lc_m.setLed(2,0,0,t);lc_m.setLed(3,0,0,t);
  
 
}

void all(){
  servo.write(0);
  happy();
  delay(1000);
  surprised(1000);
  delay(1000);
  servo.write(90);
  angry();
  delay(1000);
  servo.write(0);
  wink();
  delay(1000);
  servo.write(90);
    
  }


int count = 0;
int randomNumber = random(1,25);

float avg_hit;
float limit_hit=5.2;

int test_var=0;

void loop(){  
  /* 1=happy 2=wink 3=anger */
//------------------------------------------------------------------------------------------------------------------------
//  sensors_event_t a, g, temp;
//  mpu.getEvent(&a, &g, &temp);
//
//  avg_hit=((a.acceleration.x)+(a.acceleration.y)+(a.acceleration.z))/3;
//  Serial.println(avg_hit);
//  if(avg_hit>=limit_hit){
//    surprised(1000);
//    angry();
//    } 

//  if(Serial.available()>0){   
//    while (!Serial.available());
//    command = Serial.readStringUntil('\n'); 
//    command.trim();   // Command String is containing All command values
//    Serial.println(command);
//  }
//----------------------------------------------------------------------------------------------------------------------------
  int blink_speed=5;
  if (count == randomNumber) {
    // Serial.println("Value Changed");

    // Eye closing
    glow_m(1,1,2,6,f); glow_m(2,1,1,5,f); // L1
    delay(blink_speed);
    glow_m(1,7,2,6,f); glow_m(2,7,1,5,f); // L7
    delay(blink_speed);
    glow_m(1,2,1,7,f); glow_m(2,2,0,6,f); // L2
    delay(blink_speed);
    glow_m(1,3,1,7,f); glow_m(2,3,0,6,f); // L3
    delay(blink_speed);
    glow_m(1,6,1,7,f); glow_m(2,6,0,6,f); // L6
    delay(blink_speed);
    glow_m(1,4,1,7,f); glow_m(2,4,0,6,f); // L4
    delay(blink_speed);

    // Closed 
    // Eye Opening--------
    glow_m(1,4,1,7,t); glow_m(2,4,0,6,t); // L4
    delay(blink_speed);
    glow_m(1,6,1,7,t); glow_m(2,6,0,6,t); // L6
    delay(blink_speed);
    glow_m(1,3,1,7,t); glow_m(2,3,0,6,t); // L3
    delay(blink_speed);
    glow_m(1,2,1,7,t); glow_m(2,2,0,6,t); // L2
    delay(blink_speed);
    glow_m(1,7,2,6,t); glow_m(2,7,1,5,t); // L7
    delay(blink_speed);
    glow_m(1,1,2,6,t); glow_m(2,1,1,5,t); // L1
    delay(blink_speed);

    count = 0; // Reset count to 0
    randomNumber = random(1, 25); // Generate a new random number

  }else {
    // Serial.println("Same");
    glow_m(1,1,2,6,t); glow_m(2,1,1,5,t); // L1
    glow_m(1,2,1,7,t); glow_m(2,2,0,6,t); // L2
    glow_m(1,3,1,7,t); glow_m(2,3,0,6,t); // L3
    glow_m(1,4,1,7,t); glow_m(2,4,0,6,t); // L4
    glow_m(1,5,1,7,t); glow_m(2,5,0,6,t); // L5  // not closed 
    glow_m(1,6,1,7,t); glow_m(2,6,0,6,t); // L6
    glow_m(1,7,2,6,t); glow_m(2,7,1,5,t); // L7

    count++; 
  }

//  right(500,/500);
//  all();
//  wink();
//-----------------------------------------------------------------------------------------------------------

//   forward(1000,1000);
  


}
