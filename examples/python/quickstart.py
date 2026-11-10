"""Look at a phone, go Home, open Settings and save a screenshot.

pip install invilabs
INVI_API_KEY=... python quickstart.py SE001
"""
import os
import sys

from invilabs import Client

client = Client(os.environ["INVI_API_KEY"])
phone = client.phone(sys.argv[1] if len(sys.argv) > 1 else "SE001")  # the phone's code in the panel

print(phone.details())
phone.press("home")
phone.open_app("Settings")
phone.save_screenshot("settings.png")
print("Saved settings.png")
