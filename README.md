# ReserveX-PoC
# ReserveX – EV HV Safety PoC

This prototype simulates ReserveX, an embedded intelligence module for EV high-voltage systems.  
It detects early warning signs of HV failures and triggers safe fallback actions.

## Run

```bash
pip install -r requirements.txt
python core/monitor.py
Outputs
NORMAL operation when safe

FAULT state triggers power limit, system isolation, and driver alert

yaml
Copy
Edit

---

### ✅ (Optional) `docs/diagram.png`

Create a block diagram like this:

HV Sensors (Voltage, Current, Temperature)
↓
ReserveX Module
├── Data Monitor
├── Fault Prediction
└── Safe Fallback Logic
↓
Driver Alert / Power Limiting / HV Isolation

yaml
Copy
Edit

Use **draw.io / PowerPoint**, export as PNG, and save as `docs/diagram.png`.

---

### ✅ How to Run Locally

```bash
git clone <your-repo-url>
cd reservex-safety-poc
pip install -r requirements.txt
python core/monitor.py
You’ll see output like:

bash
Copy
Edit
t=0 | Voltage=380.0 | Temp=45.0 | NORMAL | All systems normal
t=1 | Voltage=375.0 | Temp=48.0 | NORMAL | All systems normal
t=2 | Voltage=360.0 | Temp=52.0 | NORMAL | All systems normal
t=3 | Voltage=310.0 | Temp=70.0 | FAULT | Limit power, isolate HV system, alert driver
t=4 | Voltage=295.0 | Temp=90.0 | FAULT | Limit power, isolate HV system, alert driver
