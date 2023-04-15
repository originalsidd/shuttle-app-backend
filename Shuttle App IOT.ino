#include <SoftwareSerial.h>

// defines pins numbers
const int trigPin1 = 7;
const int echoPin1 = 6;
const int trigPin2 = 10;
const int echoPin2 = 11;
const int ledPin = 2;
// defines variables
long duration1;
long duration2;
int distance1;
int distance2;
int flag1 = 1;
int flag2 = 1;

SoftwareSerial BTserial(0, 1);

void setup() {
    pinMode(trigPin1, OUTPUT);  // Sets the trigPin as an Output
    pinMode(echoPin1, INPUT);   // Sets the echoPin as an Input
    pinMode(trigPin2, OUTPUT);  // Sets the trigPin as an Output
    pinMode(echoPin2, INPUT);   // Sets the echoPin as an Input
    pinMode(ledPin, OUTPUT);
    Serial.begin(9500);  // Starts the serial communication
    BTserial.begin(9600);
}
void loop() {
    // Clears the trigPin
    digitalWrite(trigPin1, LOW);

    delayMicroseconds(1000);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin1, HIGH);

    delayMicroseconds(1000);
    digitalWrite(trigPin1, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration1 = pulseIn(echoPin1, HIGH);

    // Calculating the distance
    distance1 = duration1 * 0.034 / 2;

    digitalWrite(trigPin2, LOW);
    delayMicroseconds(1000);
    digitalWrite(trigPin2, HIGH);
    delayMicroseconds(1000);
    digitalWrite(trigPin2, LOW);
    duration2 = pulseIn(echoPin2, HIGH);
    distance2 = duration2 * 0.034 / 2;

    if (distance1 < 12 && flag1 == 1) {
        if (flag1 == 1) {
            Serial.print("A");
            BTserial.write(Serial.read());
            flag1 = 0;
        }
    } else if (distance1 > 12) {
        flag1 = 1;
    }

    if (distance2 < 12 && flag2 == 1) {
        if (flag2 == 1) {
            Serial.print("B");
            BTserial.write(Serial.read());
            flag2 = 0;
        }
    } else if (distance2 > 12) {
        flag2 = 1;
    }

    if (distance1 < 12 || distance2 < 12) {
        digitalWrite(ledPin, HIGH);
    } else {
        digitalWrite(ledPin, LOW);
    }
}