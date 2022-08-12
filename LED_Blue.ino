char Incoming_value=0;
int led = 21;

void setup() {
  pinMode(led, OUTPUT);
  Serial1.begin(9600);
}

void loop() {
  if(Serial1.available()>0)
  {
  Incoming_value=Serial1.read();
  Serial1.print(Incoming_value);
  Serial1.print("\n");

  if(Incoming_value=='1')
    digitalWrite(led, HIGH);
  else if(Incoming_value=='0')
    digitalWrite(led, LOW);
  }
}
