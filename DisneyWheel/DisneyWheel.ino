/*
Adafruit Arduino - Lesson 14. Sweep
*/
 
#include <Servo.h> 
Servo myServo;
int rideSpeed = 92;
int incomingByte = 0;

void setup() 
{ 
  myServo.attach(9);
  Serial.begin(9600);
} 
 
 
void loop() 
{ 
  if (Serial.available() > 0) {    
    rideSpeed = Serial.parseInt();
  }
  
  myServo.write(rideSpeed);

} 
