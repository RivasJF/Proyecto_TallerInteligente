#include <LiquidCrystal_I2C.h> // Librería para el LCD con I2C
#include <Wire.h>

// Configuración del LCD, botón y buzzer
const int buttonPin = 2;
const int buzzerPin = 9; 
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Variables para el buzzer
int duracion = 250; // Duración del sonido
int freqmin = 2000; // Frecuencia más baja 
int freqmax = 4000; // Frecuencia más alta 

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // Configura el botón como entrada 
  pinMode(buzzerPin, OUTPUT);       // Configura el buzzer como salida
  lcd.init(); // Inicializa el LCD
  lcd.backlight(); // Activa la luz de fondo del LCD
  lcd.clear();     // Limpia el LCD
}

// Función para generar el sonido en el buzzer
void generarSonido() {
  for (int i = freqmin; i <= freqmax; i ++) {
    tone(buzzerPin, i, duracion);
  }
  for (int i = freqmax; i >= freqmin; i --) {
    tone(buzzerPin, i, duracion);
  }
  noTone(buzzerPin);
}

// Función para mostrar alerta de sismo
void mostrarAlerta() {
  while (digitalRead(buttonPin) == HIGH) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("    ALERTA!    "); 
    lcd.setCursor(0, 1);
    lcd.print("     SISMO     "); 

    generarSonido(); // Llama a la función para generar el sonido

    delay(400); // Pausa entre ciclos de la alerta
  }

  noTone(buzzerPin); 
}

// Función para mostrar el mensaje inicial y desplazar texto
void mostrarMensajeInicial() {
  lcd.setCursor(0, 0);
  lcd.print("      HOLA!   ");
  lcd.setCursor(0, 1);
  lcd.print("   UES ATENCO ");
  
  for (int c = 0; c < 3; c++) {
    lcd.scrollDisplayLeft();
    delay(500);

    // Verifica si el botón está presionado durante el ciclo
    if (digitalRead(buttonPin) == HIGH) {
      mostrarAlerta(); 
      return;        
    }
  }
  
  for (int c = 0; c < 3; c++) {
    lcd.scrollDisplayRight();
    delay(600);

    // Verifica si el botón está presionado durante el ciclo
    if (digitalRead(buttonPin) == HIGH) {
      mostrarAlerta();
      return;          
    }
  }

  noTone(buzzerPin); // Asegura que el buzzer esté apagado al iniciar el mensaje inicial
}

void loop() {
  // Llama a la función mostrarMensajeInicial continuamente
  mostrarMensajeInicial();
}



