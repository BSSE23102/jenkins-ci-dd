import time
import datetime

while True:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] INFO: Dummy logger service is running...")
    time.sleep(5)