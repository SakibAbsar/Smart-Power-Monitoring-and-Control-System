
#ifndef POWER_SENSOR_H
#define POWER_SENSOR_H

class PowerSensor {
public:
    static void init();
    static float readCurrent();
    static float readVoltage();
};

#endif
