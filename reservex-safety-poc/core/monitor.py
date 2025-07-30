import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.data_stream import stream_data
from core.fault_logic import check_fault, fallback_action

if __name__ == "__main__":
    for packet in stream_data("data/hv_log.csv"):
        state = check_fault(packet)
        action = fallback_action(state)
        print(f"t={packet['time']} | Voltage={packet['voltage']} | Temp={packet['temperature']} "
              f"| {state} | {action}")
