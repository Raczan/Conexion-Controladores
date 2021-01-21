#include <math.h>
int val = 0;
int valor;
const float a36=40.44109566; // mq136
const float b36=-1.085728557; // mq136
int valor36;
float voltaje36, rs36, ppm36;
const float a=20.6690525600; // mq7
const float b=-0.656039042; // mq7
float voltaje,rs,ppm;
float a31= 42.84561841, b31=-1.043297135,ppb31,rs31,valor31,volt; 
int measurePin = 0;
int ledPower = 12;
int samplingTime = 280;
int deltaTime = 40;
int sleepTime = 9680;
float voMeasured = 0;
float calcVoltage = 0;
float dustDensity = 0;
float pm05=0;

void setup() {
  Serial.begin(9600); //BAUDIO DEL MONITOR SERIAL
  pinMode(ledPower,OUTPUT);
  pinMode(A1,INPUT);
  pinMode (A2,INPUT);
  pinMode(A4,INPUT);
  Serial.flush();
}

void SO2(){
  valor36 = analogRead(4); //mq136
  voltaje36 = valor36*(5/1023.0); //mq136
  rs36 = ((5/voltaje36)-1)*1000; //mq136
  ppm36= pow(((rs36/11)/a36),(1/b36));//mq136
  Serial.println(ppm36);//mq136
  delay(500);
}

void polvo(){
  digitalWrite(ledPower,LOW); 
  delayMicroseconds(samplingTime);
  voMeasured = analogRead(measurePin); 
  delayMicroseconds(deltaTime);
  digitalWrite(ledPower,HIGH); 
  delayMicroseconds(sleepTime);
  calcVoltage = 5*voMeasured/1024;
  dustDensity = (0.17 * calcVoltage - 0.1)*1000;
  pm05=(calcVoltage-0.0356)*120000;
  Serial.println(dustDensity);
  delay(500);
}

void O3(){
  valor31=analogRead(2);
  volt=valor31*(5.0/1023);
  rs31 = (((5-volt)/volt)/1.5);
  ppb31= pow(((rs31/14.17)/a31),(1/b31));
  Serial.println(ppb31);
  delay(500);
}

void CO(){
  valor = analogRead(1); //mq7
  voltaje = valor*(5/1023.0); //mq7
  rs = ((5*4)/voltaje)-2; //mq7
  ppm= pow(((rs/11)/a),(1/b));//mq7
  Serial.println(ppm);//mq7
  delay(500);
}

void loop() {
  if (Serial.available() > 0) {
    int val = char(Serial.read()) - '0';
    if (val == 1) {
      SO2();
    }
    if (val == 2) {
      polvo();
    }
    if (val == 3) {
      O3();
    }    
    if (val == 4) {
      CO();
    }
  }
}
