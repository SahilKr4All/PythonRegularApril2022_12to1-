from datetime import datetime
import os,random,glob

msg = input("enter message").lower()
if msg == "ess":
    print("best institute")
if msg == "sahil sir":
    print("Nice Tutor")
elif msg == "date":
    dt= datetime.now()
    print(dt.strftime("%d/%m%a"))
elif msg == "time":
    dt = datetime.now()
    print(dt.strftime("%I:%m:%p"))
