#define PIR_PIN 2

#define LED1 3
#define LED2 4
#define LED3 5
#define LED4 6
#define LED5 7
#define LED6 8
#define LED7 9
#define LED8 10

void setup() {
  pinMode(PIR_PIN, INPUT);

  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT); pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT); pinMode(LED6, OUTPUT);
  pinMode(LED7, OUTPUT); pinMode(LED8, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  int motion = digitalRead(PIR_PIN);

  digitalWrite(LED1, motion);
  digitalWrite(LED2, motion);
  digitalWrite(LED3, motion);
  digitalWrite(LED4, motion);
  digitalWrite(LED5, motion);
  digitalWrite(LED6, motion);
  digitalWrite(LED7, motion);
  digitalWrite(LED8, motion);
}