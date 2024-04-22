#include<Servo.h>
Servo S[6];

void moveArm(uint8_t *B, Servo *S)
{
  static uint8_t A[6] = {0};
  for(uint8_t i=0;i<6;i++)
  {
    if(B[i]!=A[i])
    {
      if(B[i]>A[i])
      {
        A[i]=A[i]-1;
      }
      else
      {
        A[i]=A[i]+1;
      }
    }
    Serial.print(A[i]);
    if(i==5)
    {
      Serial.print(", ");
    }
    else
    {
      Serial.println("");
    }
    S[i].write(A[i]);
  }
}

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
  S[0].write(180);
  S[1].write(180);
  S[2].write(180);
  S[3].write(180);
  S[4].write(180);
  S[5].write(180);
  Serial.begin(115200);
}

char byt='\0';
char str[100]={'\0'};

uint8_t LUT_extended_hamming_encoding(uint8_t val)
{
  switch(val)
  {
    case 0: return 0;
    case 8: return 225;
    case 4: return 153;
    case 12: return 120;
    case 2: return 85;
    case 10: return 180;
    case 6: return 204;
    case 14: return 45;
    case 1: return 210;
    case 9: return 51;
    case 5: return 75;
    case 13: return 170;
    case 3: return 135;
    case 11: return 102;
    case 7: return 30;
    case 15: return 255;
  }
}

uint16_t extended_hamming84_encoding_byte(uint8_t data)
{
  uint16_t encoding=0;
  uint8_t mask_lower = 0b00001111;
  uint8_t mask_upper = 0b11110000;
  uint16_t mask_complete = 0b0000000011111111;
  encoding = LUT_extended_hamming_encoding((data&mask_upper)>>4)<<8;
  encoding += LUT_extended_hamming_encoding(data&mask_lower);
  return encoding;
}

uint8_t extended_hamming84_decoding_byte(uint16_t codeword)
{
  
}

void loop()
{
  Serial.println('A',BIN);
  Serial.println(extended_hamming84_encoding(uint8_t('A')), BIN);
  delay(100000);
}




























