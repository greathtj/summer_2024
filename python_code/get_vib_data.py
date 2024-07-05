import serial
import time
import csv

# Adjust the serial port name and baud rate as needed
SERIAL_PORT = 'COM19'  # For Windows, it might be 'COM3', 'COM4', etc.
BAUD_RATE = 115200
CSV_FILENAME = 'vibration_data.csv'

def trigger_measurement_and_read_data(serial_port, baud_rate):
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        # Send the trigger command to Arduino
        ser.write(b'1\n')
        time.sleep(1)  # Give Arduino some time to start measurement

        data_started = False
        data = []

        while True:
            line = ser.readline().decode('utf-8').strip()
            if line == 'SOF':
                data_started = True
                print("Start of Frame")
            elif line == 'EOF':
                print("End of Frame")
                break
            elif data_started:
                print(line)
                data.append(line)
        
        return data

def save_data_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'AccX', 'AccY', 'AccZ'])  # Write the header
        for line in data:
            values = line.split(',')
            writer.writerow(values)

if __name__ == '__main__':
    data = trigger_measurement_and_read_data(SERIAL_PORT, BAUD_RATE)
    print("\nCollected Data:")
    for line in data:
        print(line)

    save_data_to_csv(data, CSV_FILENAME)
    print(f"\nData saved to {CSV_FILENAME}")