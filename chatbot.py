from datetime import datetime
import os,random,glob

helloIntent = "hi","hie","hey","hello","hey bro","wassup"
timeIntent = "time","time please","whats the time","show me time"
dateIntent = "date","time date","whats the date","show me date"
chat=True
while chat == True:
    msg = input("Enter Message")
    if msg in  helloIntent:
        print("Hi")
    elif msg in timeIntent:
        dt = datetime.now()
        print(dt.strftime("%I:%M:%S,%p"))
    elif msg in dateIntent:
        dt = datetime.now()
        print(dt.strftime("%d/%m/%Y,%a"))
    elif msg=="music":
        x = glob.glob("*.mp3")
        os.startfile(random.choice(x))
        
    elif msg =="bye":
        print("Good Bye..Tc..")
        chat=False
    else:
        print("Sorry i dont understand")
