
import serial
import csv
import time

def log_data():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    with open("power_data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Power (W)"])

        while True:
            line = ser.readline().decode().strip()
            if line.startswith("Power:"):
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                power = line.split(" ")[1]
                writer.writerow([timestamp, power])
                print(f"{timestamp} - Power: {power} W")
            time.sleep(1)

if __name__ == "__main__":
    log_data()
