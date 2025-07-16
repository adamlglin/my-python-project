import time
import json
import random
import boto3
import datetime

iot = boto3.client('iot-data', region_name='ap-northeast-1')  # Example: Tokyo Region

while True:
    payload = {
        'device_id': 'sensor-001',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'pressure': round(random.uniform(5.8, 6.5), 2),
        'temperature': round(random.uniform(21.5, 26.0), 2)
    }

    iot.publish(
        topic='factory/data',
        qos=0,
        payload=json.dumps(payload)
    )

    print(f"Sent data: {payload}")
    time.sleep(10)  # 每 10 秒傳送一筆
