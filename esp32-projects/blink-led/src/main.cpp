#include <Arduino.h>

#define LED_BUILTIN 26

void setup() {
  pinMode(26, OUTPUT);
  Serial.begin(115200);
  Serial.println("ESP32 started");
}

void loop() {
  digitalWrite(26, HIGH);
  Serial.println("LED ON");
  delay(200);
  digitalWrite(26, LOW);
  Serial.println("LED OFF");
  delay(200);
}