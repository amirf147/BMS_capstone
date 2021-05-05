from influxdb import InfluxDBClient
import serial

#set up database
database_name = "LTC6811"
client = InfluxDBClient('localhost', 8086, 'pi',
                        'raspberry', database_name)
client = InfluxDBClient(username = 'admin', password = 'admin')

while True:
    with serial.Serial("/dev/rfcomm0", 115200, timeout=1) \
    as sim808:
            while sim808.isOpen():
                if sim808.inWaiting(): 
                    data_length = sim808.inWaiting()
                    data = sim808.read(data_length).decode() \
                           .split(',')[:-1]
                    for i in range(len(data)):
                        line_protocol = database_name + "," + \
                                        "sensor=Voltage cell" + \
                                        str(i + 1) + "=" + data[i]
                        client.write([line_protocol], \
                                     {'db': database_name}, \
                                     204,'line')
                    