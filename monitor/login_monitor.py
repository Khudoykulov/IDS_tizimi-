import logging
import os

def check_login_attempts():
    try:
        with open("/var/log/auth.log", "r") as f:
            lines = f.readlines()[-50:]
            for line in lines:
                if "Failed password" in line or "Accepted password" in line:
                    logging.info(f"Login event: {line.strip()}")
    except FileNotFoundError:
        logging.warning("auth.log file not found.")
