from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import time

class FileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f"File modified: {event.src_path}")
    def on_deleted(self, event):
        logging.info(f"File deleted: {event.src_path}")

def start_file_monitor(path="."):
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
