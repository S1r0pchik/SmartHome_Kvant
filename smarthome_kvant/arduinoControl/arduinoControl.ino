void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  Serial.write("1"); 
}

void loop() {
    if(Serial.available() > 0){
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    delay(500); 
    digitalWrite(13, HIGH);
    delay(500);            
    digitalWrite(13, LOW);
    Serial.write('0');
}
}
