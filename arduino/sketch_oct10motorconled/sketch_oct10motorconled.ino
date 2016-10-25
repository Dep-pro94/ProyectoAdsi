int pin = 9;

void setup() {
  
  
  pinMode(pin, OUTPUT);
  
}

void loop() {
  
  for( int  i=0; i<225;i++) {
    
    analogWrite (pin,i);
    delay (100);
  }
  
}
   
