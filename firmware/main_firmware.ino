
#include "power_sensor.h"
#include "relay_control.h"

void setup() {
    Serial.begin(9600);
    PowerSensor::init();
    RelayControl::init();
}

void loop() {
    float current = PowerSensor::readCurrent();
    float voltage = PowerSensor::readVoltage();
    float power = current * voltage;

    Serial.print("Power: ");
    Serial.print(power);
    Serial.println(" W");

    if (power > 100) {  // Arbitrary threshold
        RelayControl::activate();
    } else {
        RelayControl::deactivate();
    }
    delay(1000);  // Log data every second
}
