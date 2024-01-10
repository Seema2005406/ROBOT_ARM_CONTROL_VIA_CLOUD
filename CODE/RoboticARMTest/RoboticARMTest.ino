#include<Servo.h>
Servo S[6];
void setup() 
{
  Serial.begin(115200);
  pinMode(3,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  S[0].attach(3);
  S[1].attach(5);
  S[2].attach(6);
  S[3].attach(9);
  S[4].attach(10);
  S[5].attach(11);
}

void loop() 
{
  //  for(int i=0;i<6;i++)
  //  {
  //    S[i].write(0);
  //  }
  //  delay(1000);
  //  for(int i=0;i<6;i++)
  //  {
  //    S[i].write(90);
  //  }
  //  delay(1000);
  //  for(int i=0;i<6;i++)
  //  {
  //    S[i].write(180);
  //  }
  //  delay(1000);
  S[1].write(0);
  Serial.println("Moving to 0");
  delay(5000);
  S[1].write(90);
  Serial.println("Moving to 90");
  delay(5000);
}
