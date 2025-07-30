# ReserveX – EV HV Safety PoC

This prototype simulates ReserveX, an embedded intelligence module for EV high-voltage systems.  
It detects early warning signs of HV failures and triggers safe fallback actions.

## Run

```bash
pip install -r requirements.txt
python core/monitor.py
```

## Outputs
- NORMAL operation when safe
- FAULT state triggers power limit, system isolation, and driver alert
