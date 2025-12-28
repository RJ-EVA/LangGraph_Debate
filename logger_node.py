# logger_node.py
# Responsible for logging all events to a file

import json
import time
import os


class Logger:
    def __init__(self, log_path):
        """
        log_path: path to the log file (string)
        """
        self.log_path = log_path

        # Ensure the logs directory exists
        log_dir = os.path.dirname(log_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def log(self, event_type, data):
        """
        Write a single log entry as a JSON line.
        """
        entry = {
            "timestamp": time.time(),
            "event_type": event_type,
            "data": data
        }

        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
