# utils.py
def predict(data: dict):
    return {"prediction": "positive", "confidence": 0.85}

def basic_analytics():
    return {"total_requests": 134, "avg_response_time_ms": 120}

def full_analytics():
    return {
        "total_requests": 134,
        "avg_response_time_ms": 120,
        "model_accuracy": 0.91,
        "retrain_needed": False,
        "last_training": "2025-07-10"
    }
