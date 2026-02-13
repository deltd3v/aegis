import time
import json
import os

class PerformanceTracker:
    def __init__(self, metrics_file="performance.json"):
        self.metrics_file = metrics_file
        self.metrics = self._load_metrics()

    def _load_metrics(self):
        if os.path.exists(self.metrics_file):
            try:
                with open(self.metrics_file, "r") as f:
                    data = json.load(f)
                    if isinstance(data, dict) and "history" in data:
                        return data
            except json.JSONDecodeError:
                pass
        return {"history": []}

    def track_metric(self, name, value, unit=""):
        entry = {
            "timestamp": time.time(),
            "name": name,
            "value": value,
            "unit": unit,
            "readable_time": time.ctime()
        }
        self.metrics["history"].append(entry)
        self._save_metrics()

    def _save_metrics(self):
        with open(self.metrics_file, "w") as f:
            json.dump(self.metrics, f, indent=4)

    def get_latest_metric(self, name):
        for entry in reversed(self.metrics["history"]):
            if entry["name"] == name:
                return entry
        return None

if __name__ == "__main__":
    tracker = PerformanceTracker()
    tracker.track_metric("Task Completion Rate", 0.5, "%")
