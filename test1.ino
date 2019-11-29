//부저 센서의 핀번호를 설정한다.
int piezoPin = 3;
//초음파 센서의 핀번호를 설정한다.
int echoPin = 13;
int trigPin = 12;

void setup() 
{
  Serial.begin(9600);
  // trig를 출력모드로 설정, echo를 입력모드로 설정
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(piezoPin, OUTPUT);
}

void loop() 
{
  // trig를 출력모드로 설정, echo를 입력모드로 설정
  digitalWrite(trigPin, LOW);
  digitalWrite(echoPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // echoPin 이 HIGH를 유지한 시간을 저장 한다.
  unsigned long duration = pulseIn(echoPin, HIGH);
  
  // HIGH 였을 때 시간(초음파가 보냈다가 다시 들어온 시간)을 가지고 거리를 계산 한다.
  float distance = ((float)(340*duration) / 10000) / 2.0;

 // 50cm 미만일 때 소리가 출력됩니다. 50cm를 초과하면 소리 X
  if (distance < 20){
    tone(piezoPin, 1047); // 도
  }
  else {
    noTone(piezoPin);
  }
  
  delay(100); 
   
  Serial.print(distance);
  Serial.println("cm");
}
