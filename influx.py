from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "wuIIGJEQq6HTBg4E2CX3kuZDEb8MqvQ53uDHe81hLQ_gAjZXghocdfP8vZPOw6Y3V3XKj0JzUxhAMblRMcKqKg=="
org = "amirf147@gmail.com"
bucket = "mail"

client = InfluxDBClient(url="https://europe-west1-1.gcp.cloud2.influxdata.com", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

#line protocol to write data
data = "mem,host=host2 used_percent=10"

#datapoint to write data
# point = Point("example")\\
#     .tag("host", "raspberry")\\
#     .tag("sensor", "gyroscope")\\
#     .tag("camera", "picamera")\\
#     .field("mailrx", True)\\
#     .field("picrx", True)\\
#     .time(datetime.utcnow(), WritePrecision.NS)
    

write_api.write(bucket, org, data)

