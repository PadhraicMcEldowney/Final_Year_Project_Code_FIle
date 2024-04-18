import serial
import chardet
from datetime import datetime
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

temp = None
humidity = None
voc = None

ser = serial.Serial('/dev/cu.usbmodem14101', 38400, timeout=1)

# creat a client instance
client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token="37QpaEcOHF30-orDfdQV1MwksjQ95k4mNNtjXNoIWoOZzHaqBHwzUwlRkK_qVk5xlf-ND35Bb6ifdGdnR_l_TA==", org="Student Final Year Project", verify_ssl=False)

# create a write API instance with synchronous writes
write_api = client.write_api(write_options=SYNCHRONOUS)

ser = serial.Serial('/dev/cu.usbmodem14101', 38400)
    
while True:
    try:
        line = ser.readline()
        encoding = chardet.detect(line).get('encoding', 'utf-8')  # Get the detected encoding or default to 'utf-8'
        print("encoded data:", encoding)
        line_decoded = line.decode(encoding).strip()
        print("Decoded line:", line_decoded)  # Debug print to show the received line

        if line_decoded.startswith("Slave 1 data:"):
            # Read the next line
            line = ser.readline()
            line_decoded = line.decode(encoding).strip()
            print("Next decoded line:", line_decoded)  # Debug print to show the received line

            # Extract numbers after each indicator (T1, H1, V1)
            data_parts = []
            indicators = ["T1:", "H1:", "V1:"]
            for indicator in indicators:
                start_index = line_decoded.index(indicator)
                end_index = line_decoded.index(indicators[indicators.index(indicator) + 1]) if indicators.index(indicator) < len(indicators) - 1 else len(line_decoded)
                number = line_decoded[start_index + len(indicator):end_index].strip().split()[0]  # Split by space and take the first part
                data_parts.append(number)

                print("Separated numbers:", [number])  # Print each separated number
            
            # Check if data_parts is not empty
            if len(data_parts) == 3:  # Check if all three numbers are present

                # Convert strings to floats
                temp = float(data_parts[0])  # Temperature is the first number
                humidity = float(data_parts[1])  # Humidity is the second number
                voc = float(data_parts[2])  # VOC is the third number

                # Print extracted data
                print("Temperature:", temp)
                print("Humidity:", humidity)
                print("VOC:", voc)

                # Write data to InfluxDB
                write_api.write(bucket="FYP Database",
                                record=[
                                    Point("temperature").tag("sensor", "Slave 1").field("value", temp).time(datetime.utcnow()),
                                    Point("humidity").tag("sensor", "Slave 1").field("value", humidity).time(datetime.utcnow()),
                                    Point("voc").tag("sensor", "Slave 1").field("value", voc).time(datetime.utcnow())
                                ])
                print("Data added to InfluxDB:", {"Temperature": temp, "Humidity": humidity, "VOC": voc})
            else:
                print("Skipping line: Incorrect data format")
    except Exception as e:
        print("Error:", e)
        print("Error: Unable to parse data")

# Close the serial port
ser.close()

