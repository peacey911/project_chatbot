import time
import datetime

today = datetime.datetime.now()
print(today)

# if today.strftime("%H") >= 00:
#    print("good night")


def start():
    if 00 <= today.strftime("%H"):
        print("Good morning!")
    elif 12 <= today.strftime("%H"):
        if today.strftime("%H") <= 7:
            print("Good afternoon!")
    else:
        print("Good evening!")


start()
