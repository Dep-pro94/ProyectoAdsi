#include <boards.h>
#include <SPI.h>
#include <EEPROM.h>

int DIGITAL_OUT_PIN = 7;

void setup (){

  pinMode(DIGITAL_OUT_PIN, OUTPUT);
  Serial.begin (9650);
  Serial.print ("BLE Arduino slave");
  ble_set_name("andrew");
  ble_begin(); 
}

void loop (){
  
while (ble_available(){

  byte data0 = ble_read ();
  byte data1 = ble_read ();
  byte data2 = ble_read ();

  Serial.print ("data0" + data0);
  Serial.print ("data1" + data1);

  if (data0 == 0x01){

    digitalWrite (DIGITAL_OUT_PIN, HIGH);
    Serial.print("estoi prendiendo el LED");
  }

  else {

    digitalWrite (DIGITAL_OUT-PIN, LOW);
    Serial.print("no se esta prendiendo el LED");
    
    
  }
   
}
   
  }

ble_do_events ();




  




