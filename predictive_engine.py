import time

class DiskSample:
    def __init__(self, bytes_used: float):
        self.timestamp = time.time()
        self.bytes_used = bytes_used

class PredictiveEngine:
    @staticmethod
    def calculate_hours_to_full(samples: list, total_capacity: float) -> float:
        if len(samples) < 2:
            return -1.0 
        
        first = samples[0]
        last = samples[-1]
        
        delta_time = last.timestamp - first.timestamp
        delta_space = last.bytes_used - first.bytes_used
        
        if delta_time <= 0 or delta_space <= 0:
            return -1.0
            
        consumption_rate_per_sec = delta_space / delta_time
        remaining_space = total_capacity - last.bytes_used
        
        if remaining_space <= 0:
            return 0.0 
            
        seconds_to_full = remaining_space / consumption_rate_per_sec
        hours_to_full = seconds_to_full / 3600.0
        return round(hours_to_full, 1)