const int ledPin = 11;
const int soilPin = 21;
// the setup() method runs once, when the sketch starts

void setup() {
// initialize the digital pin as an output. 
  pinMode(ledPin, OUTPUT);
  Serial1.begin(9800);
}
void loop() {
  int val = analogRead(soilPin); 
  Serial1.print("Soil : "); 
  Serial1.println(val); 
  digitalWrite(ledPin, HIGH); 
  delay(1000); 
  digitalWrite(ledPin, LOW); 
  delay(100);
}
