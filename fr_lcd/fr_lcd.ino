#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);
int buzzer = 7;
int LED = 6;
String mystring = "Kokakola";

void setup() {
  // set up the LCD's number of columns and rows:
  pinMode(buzzer, OUTPUT);
  pinMode(LED, OUTPUT);
  lcd.init();
  lcd.clear();         
  lcd.backlight();
  // initialize the serial communications:
  Serial.begin(9600);
}

void loop() {
  // when characters arrive over the serial port...
  if (Serial.available()) {
    
    delay(100);
    
    lcd.clear();

    tone(buzzer, 1000);
    digitalWrite(LED, HIGH);
    delay(500);        
    noTone(buzzer);
    digitalWrite(LED, LOW);    
   
    while (Serial.available() > 0) {
      
      lcd.setCursor(0,0);
      lcd.print(Serial.readString());
      
    }
  }
}