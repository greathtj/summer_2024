#define motor_pin 23


void setup() {
  pinMode(motor_pin, OUTPUT);

}

void loop() {
  digitalWrite(motor_pin, LOW);
  delay(200);
  digitalWrite(motor_pin, LOW);
  delay(200);
}
