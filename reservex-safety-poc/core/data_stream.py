import csv
import time

def stream_data(file_path):
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            packet = {k: float(v) if k != "time" else v for k, v in row.items()}
            yield packet
            time.sleep(0.5)  # simulate real-time streaming
