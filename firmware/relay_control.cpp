
#include "relay_control.h"

#define RELAY_PIN 10  // Define relay control pin

void RelayControl::init() {
    pinMode(RELAY_PIN, OUTPUT);
}

void RelayControl::activate() {
    digitalWrite(RELAY_PIN, HIGH);
}

void RelayControl::deactivate() {
    digitalWrite(RELAY_PIN, LOW);
}
