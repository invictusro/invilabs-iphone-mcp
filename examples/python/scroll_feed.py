"""Scroll a feed a few times and save a screenshot after each scroll.

pip install invilabs
INVI_API_KEY=... python scroll_feed.py SE001 Safari 5
"""
import os
import sys
import time

from invilabs import Client

phone_code, app, count = sys.argv[1], sys.argv[2], int(sys.argv[3])
phone = Client(os.environ["INVI_API_KEY"]).phone(phone_code)

phone.open_app(app)
time.sleep(4)  # let the app load
for i in range(count):
    phone.scroll("down")
    time.sleep(2)
    phone.save_screenshot(f"feed-{i + 1}.png")
    print(f"Saved feed-{i + 1}.png")
