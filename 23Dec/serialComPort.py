import serial
import time

# Function to initialize the serial connection
def initialize_serial(port, baud_rate=9600):
    ser = serial.Serial(port, baud_rate)
    return ser

# Function to send data over the serial connection
def send_data(ser, data):
    ser.write(data.encode())

# Function to read data from the serial connection
def read_data(ser):
    return ser.readline().decode()

# Function to close the serial connection
def close_serial(ser):
    ser.close()

if __name__ == "__main__":
    # Set the serial port and baud rate
    serial_port = "COM4"  # Change this to the appropriate port on your system
    baud_rate = 115200  

    # Initialize the serial connection
    serial_connection = initialize_serial(serial_port, baud_rate)

    try:
        while True:
            # Read and print the response from the device
            received_data = read_data(serial_connection)
            print(f"Received data: {received_data}")

    except KeyboardInterrupt:
        print("\nUser interrupted the program.")

    finally:
        # Close the serial connection when done
        close_serial(serial_connection)
