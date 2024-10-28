
import serial
import time

def control_load(command):
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    if command == "ON":
        ser.write(b'1')
    elif command == "OFF":
        ser.write(b'0')
    print(f"Load turned {command}")

if __name__ == "__main__":
    while True:
        command = input("Enter command (ON/OFF): ")
        if command in ["ON", "OFF"]:
            control_load(command)
        else:
            print("Invalid command")
