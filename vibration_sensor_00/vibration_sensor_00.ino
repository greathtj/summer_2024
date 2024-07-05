#include "Wire.h"
#include "MPU6050.h"
#include <Esp.h>
#include <VibrationMotor.h>

#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

MPU6050 accelgyro;
int16_t ax, ay, az;

const int numReadings = 3000; // Number of readings to store
int a_ax[numReadings];   // Array to store the readings
int a_ay[numReadings];   // Array to store the readings
int a_az[numReadings];   // Array to store the readings
int readIndex = 0;           // Index of the current reading
int total = 0;               // Total of the readings for average calculation


#define OUTPUT_READABLE_ACCELGYRO
#define LED_PIN 2
bool blinkState = false;

#define motor_pin 23
VibrationMotor myVibrationMotor(motor_pin);
bool motor_run = false;

TaskHandle_t create_vibration_handle;

void create_vibration(void *pvParameters) {
  while (true) {
    if (motor_run) {
      delay(500);
      myVibrationMotor.pulse(5);
      motor_run = false;
    }
    delay(10);
  }
}

String inputString = "";

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      if (inputString == "1") {
        motor_run = true;
        delay(300);
        Serial.println("SOF");
        for (int i=0; i<numReadings; i++) {
          accelgyro.getAcceleration(&ax, &ay, &az);
          a_ax[i] = ax; a_ay[i] = ay; a_az[i] = az;
        }
        for (int i=0; i<numReadings; i++) {
          Serial.print(i); Serial.print(",");
          Serial.print(a_ax[i]); Serial.print(",");
          Serial.print(a_ay[i]); Serial.print(",");
          Serial.print(a_az[i]); Serial.println("");
        }
        Serial.println("EOF");
      }
      inputString = "";
    } else {
      inputString += inChar;
    }
  }
}

void setup() {
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
      Wire.begin();
  #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
      Fastwire::setup(400, true);
  #endif

  Serial.begin(115200);

  Serial.println("Initializing I2C devices...");
  accelgyro.initialize();

  Serial.println("Testing device connections...");
  Serial.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");

  pinMode(LED_PIN, OUTPUT);
  pinMode(motor_pin, OUTPUT);

  // Start create vibration task
  xTaskCreate(
    create_vibration,           // Function to be called
    "Vibration Task",        // Name of the task
    2000,                // Stack size (bytes)
    NULL,                // Parameter to pass
    1,                   // Task priority
    &create_vibration_handle     // Task handle
  );
}

void loop() {
    // accelgyro.getAcceleration(&ax, &ay, &az);

    // Serial.print(ax); Serial.print("\t");
    // Serial.print(ay); Serial.print("\t");
    // Serial.print(az); Serial.println("");

    // blinkState = !blinkState;
    // digitalWrite(LED_PIN, blinkState);
    // delay(100);
}
