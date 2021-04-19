#include <Arduino.h>
int ledPin = 13;   // select the pin for the LED
int val = 0; 
int val_2 = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(6, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
//  Serial.print("babs");
  val = analogRead(A0);
  val_2 = (val / 4);
  Serial.print(val_2);
  analogWrite(6, val_2);
//  digitalWrite(13, HIGH);

}