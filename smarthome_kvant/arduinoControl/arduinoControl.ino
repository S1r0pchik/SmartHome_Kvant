#include "DHT.h"
#define DHTPIN 3

DHT dht(DHTPIN, DHT11);
const int relPin = 4;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  Serial.write("1");
  Serial.write("2");
  dht.begin();
  pinMode(relPin, OUTPUT);
}

void loop() {
    if (Serial.available() == 1){
    digitalWrite(relPin, HIGH);
    delay(1000);
    digitalWrite(relPin, LOW);
    delay(3000);
    Serial.write('0');
    };
    if (Serial.available() == 2){
      float h = dht.readHumidity();
      float t = dht.readTemperature();
      if (isnan(h) || isnan(t)) {
        Serial.println("Ошибка считывания");
        return;
    }
      Serial.print("Влажность: ");
      Serial.print(h);
      Serial.print(" %\t");
      Serial.print("Температура: ");
      Serial.print(t);
      Serial.println(" *C ");
}
