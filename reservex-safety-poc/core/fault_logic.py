def check_fault(data):
    if data['voltage'] < 320 or data['temperature'] > 80:
        return "FAULT"
    return "NORMAL"

def fallback_action(state):
    if state == "FAULT":
        return "Limit power, isolate HV system, alert driver"
    return "All systems normal"
