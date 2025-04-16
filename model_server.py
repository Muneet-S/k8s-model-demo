# model_server.py
from fastapi import FastAPI, Request
import os
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    user_id: Optional[str] = "default"
    input: float

@app.post("/predict")
async def predict(request: PredictionRequest):
    return {
        "user_id": request.user_id,
        "input": request.input,
        "prediction": request.input ** 2,
        "pod_name": os.getenv('POD_NAME', 'unknown')
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
