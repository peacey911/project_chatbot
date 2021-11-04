import datetime
today =datetime.datetime.now()
print(today)

if today.strftime("%H") >= 00:
    print("good night")
