from fastapi import FastAPI
import math

app = FastAPI()

@app.post("/calculate-maneuver")
async def calculate_maneuver(data: dict):
    alt = data.get("altitude", 550)
    inc = data.get("inclination", 0)
    dv_needed = math.sqrt(398600 / alt) * (inc / 100)
    return {
        "status": "CALCULATED",
        "delta_v_mps": round(dv_needed, 4),
        "safety_threshold": dv_needed < 50.0
    }
