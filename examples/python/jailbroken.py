"""Jailbroken phones (Invi Link): list apps, read the UI and tap by text.

pip install invilabs
INVI_API_KEY=... python jailbroken.py JB001 Settings
"""
import os
import sys

from invilabs import Client

phone = Client(os.environ["INVI_API_KEY"]).phone(sys.argv[1])
jb = phone.jailbroken

for app in jb.apps()["apps"][:10]:
    print(app)
for element in jb.ui_dump()["elements"][:20]:
    print(element["text"], element["frame"])
jb.tap_text(sys.argv[2])
