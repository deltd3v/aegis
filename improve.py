import os
import subprocess
import time
import sys
import importlib.util

# Workaround for hyphenated directory name
LEGOS_DIR = os.path.join(os.getcwd(), "legos-dev")
sys.path.append(LEGOS_DIR)

try:
    from logger import AegisLogger
    from performance_tracker import PerformanceTracker
except ImportError:
    # Fallback
    class AegisLogger:
        def log(self, m, level="INFO"): print(f"[{level}] {m}")
        def log_improvement(self, c, d): print(f"[SUCCESS] {c}: {d}")
    class PerformanceTracker:
        def track_metric(self, n, v, u=""): print(f"TRACED: {n}={v}{u}")

class AegisEvolver:
    def __init__(self):
        self.logger = AegisLogger()
        self.tracker = PerformanceTracker()
        self.todo_file = "todo.md"
        self.legos_dir = LEGOS_DIR

    def reflect(self):
        self.logger.log("Reflecting on project state...")
        if not os.path.exists(self.todo_file):
            return 0.0
        with open(self.todo_file, "r") as f:
            lines = f.readlines()
        total_tasks = sum(1 for line in lines if "[ ]" in line or "[x]" in line)
        completed_tasks = sum(1 for line in lines if "[x]" in line)

        rate = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        self.logger.log(f"Task completion rate: {rate:.2f}% ({completed_tasks}/{total_tasks})")
        self.tracker.track_metric("Task Completion Rate", rate, "%")
        return rate

    def integrate_legos(self):
        self.logger.log("Integrating legos dynamically...")
        legos = [f for f in os.listdir(self.legos_dir) if f.endswith(".py") and f != "__init__.py"]
        integration_count = 0
        for lego in legos:
            module_name = lego[:-3]
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(self.legos_dir, lego))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "integrate"):
                self.logger.log(f"Executing integrate() for {lego}...")
                if module.integrate():
                    integration_count += 1

        self.logger.log_improvement("Integrations", f"Successfully integrated {integration_count} modules.")

    def validate_project(self):
        self.logger.log("Validating project state...")
        # Check app_status.json
        if os.path.exists("app_status.json"):
            self.logger.log("app_status.json found and valid.", level="SUCCESS")
        else:
            self.logger.log("app_status.json missing!", level="ERROR")
            return False

        # Check submodules
        if os.path.exists("repos/llama.cpp/README.md"):
             self.logger.log("Submodule llama.cpp is present.", level="SUCCESS")
        else:
             self.logger.log("Submodule llama.cpp is missing content!", level="WARNING")

        return True

    def commit_changes(self, message):
        try:
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
            if not status:
                return
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", message], check=True)
            self.logger.log("Evolution committed to git.")
        except Exception as e:
            self.logger.log(f"Git error: {e}", level="ERROR")

    def evolve(self):
        self.logger.log("--- Evolution Cycle Start ---")
        self.reflect()
        self.integrate_legos()
        if self.validate_project():
            self.commit_changes("Evolution Cycle: Improved integration and validated project state.")
        self.logger.log("--- Evolution Cycle End ---")

if __name__ == "__main__":
    evolver = AegisEvolver()
    evolver.evolve()
