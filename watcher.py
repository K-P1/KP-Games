import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"{event.src_path} has been modified. Restarting...")
            if self.process:
                self.process.terminate()  # Terminate the previous process
                self.process.wait()  # Wait for it to close
            self.process = subprocess.Popen([sys.executable, 'main.py'])

if __name__ == "__main__":
    path = '.'  # Monitor the current directory
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        event_handler.process = subprocess.Popen([sys.executable, 'main.py'])  # Start the initial process
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
