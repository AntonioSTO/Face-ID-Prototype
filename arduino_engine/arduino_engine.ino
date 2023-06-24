const int ledPin = 13;
const int buzzerPin = 12;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();
    
    if (signal == '1') {
      digitalWrite(ledPin, HIGH);    // Acender o LED
      tone(buzzerPin, 1000);         // Ativar o buzzer com uma frequência de 1000 Hz
    } else if (signal == '0') {
      digitalWrite(ledPin, LOW);     // Desligar o LED
      noTone(buzzerPin);              // Desativar o buzzer
    }
  }
}
