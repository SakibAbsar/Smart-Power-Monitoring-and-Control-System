
import unittest
from firmware import power_sensor

class TestPowerSensor(unittest.TestCase):
    def test_current_reading(self):
        current = power_sensor.PowerSensor.readCurrent()
        self.assertTrue(0 <= current <= 10)  # Arbitrary range for current

    def test_voltage_reading(self):
        voltage = power_sensor.PowerSensor.readVoltage()
        self.assertTrue(200 <= voltage <= 250)  # Standard voltage range

if __name__ == "__main__":
    unittest.main()
