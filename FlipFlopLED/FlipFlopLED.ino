#include <Wire.h>

int LED = 8;
int LED2 = 9;
int LED3 = 10;
int boton = 5;
int boton2 = 6;
int boton3 = 7;
int estado;
int estado2;
int estado3;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3 OUTPUT);
  pinMode(boton, INPUT);
  pinMode(boton2, INPUT);
  pinMode(boton3, INPUT);
}

void loop() {
  estado = digitalRead(boton);
  estado2 = digitalRead(boton2);
  estado3 = digitalRead(boton3);
  
  if (estado == HIGH) { // Si el botón 1 está presionado
    digitalWrite(LED, HIGH); // Enciende el LED 1
  } else {
    digitalWrite(LED, LOW); // Apaga el LED 1
  }
  
  if (estado2 == HIGH) { // Si el botón 2 está presionado
    digitalWrite(LED2, HIGH); // Enciende el LED 2
  } else {
    digitalWrite(LED2, LOW); // Apaga el LED 2
  }
   if (estado3 == HIGH) { // Si el botón 2 está presionado
    digitalWrite(LED3, HIGH); // Enciende el LED 2
  } else {
    digitalWrite(LED3, LOW); // Apaga el LED 2
  }
}

