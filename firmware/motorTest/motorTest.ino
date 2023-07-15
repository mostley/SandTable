int motorPhiStepPin = 8; // D5
int motorPhiDirPin = 5; // D2
int motorRStepPin = 9; // D6
int motorRDirPin = 6; // D3

void setup() {
  Serial.begin(9600);
  
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(motorPhiStepPin, OUTPUT);
  pinMode(motorPhiDirPin, OUTPUT);
  pinMode(motorRStepPin, OUTPUT);
  pinMode(motorRDirPin, OUTPUT);
}

void loop() {
  digitalWrite(motorPhiDirPin, HIGH);
  digitalWrite(motorRDirPin, HIGH);
  
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(motorPhiStepPin, HIGH);
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(motorPhiStepPin, LOW);
  delay(100);
}
