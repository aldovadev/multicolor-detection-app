#include <Servo.h>

//Penamaan pin driver motor L298N
const int EN = 11;
const int logic1 = 10;
const int logic2 = 9;

//Inisialisasi nama servo sebagai servo1 dan servo2
Servo servo1;
Servo servo2;

//inisialisasi penyimpan data yang diterima dalam variabel data_masuk dengan tipe data char
char data_masuk = 'D';

void setup() {
  // initialize both serial ports:
  Serial.begin(9600);

  //instalasi pin driver motor L298N sebagai output
  pinMode(EN, OUTPUT);
  pinMode(logic1, OUTPUT);
  pinMode(logic2, OUTPUT);
  
  //instalasi pin pwm servo pada arduino 
  servo1.attach(5);
  servo2.attach(6);

  //Normalisasi Posisi Servo 
  servo1.write(0);//normal = 0, posisi tunggu = 65
  servo2.write(10);//normal = 10, posisi tunggu = 75
}

void loop() {
 //hidupkan konveyor
 motor(220);
 
 // membaca data serial dalam tipe data character
 while (Serial.available()>0) {
    data_masuk = Serial.read();
  }

 if(data_masuk == 'A'){servo1.write(0); delay(200); servo2.write(75); delay(3000); for(int i = 75; i>10; i--){servo2.write(i); delay(5);} data_masuk = 'D';}
 else if(data_masuk == 'B'){servo2.write(10); delay(200); servo1.write(65); delay(3000); for(int i = 65; i>0; i--){servo1.write(i); delay(5);} data_masuk = 'D';}
 else if(data_masuk == 'C'){servo1.write(0); servo2.write(10);}
}

void motor(int PWM){
  digitalWrite(logic1, LOW);
  digitalWrite(logic2, HIGH);
  analogWrite(EN, PWM);
  }
