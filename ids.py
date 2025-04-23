from monitor.file_monitor import start_file_monitor
from monitor.port_monitor import check_open_ports
from monitor.login_monitor import check_login_attempts
import time
import logging

logging.basicConfig(filename="logs/ids.log", level=logging.INFO, format="%(asctime)s — %(message)s")

print("IDS monitoring started...")

while True:
    try:
        check_open_ports()
        check_login_attempts()
        time.sleep(10)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
        break
