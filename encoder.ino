double rawInput;
double angle;

void setup() {
  pinMode(3, INPUT);
  Serial.begin(9600);

}

void loop() {
  rawInput = pulseIn(3, HIGH); //receive pwm in on pin 3
  angle = (rawInput / 4030) * 360; //transform position to angle


  if (angle <= 360 && angle >= 0) { //while angle is valid and in expected range, print to serial 
    Serial.println(angle,BIN);
  }
}
