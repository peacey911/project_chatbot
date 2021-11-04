import time
import datetime

today = datetime.datetime.now()
print(today)


def error_m():
    print("I couldn't understand that. Sorry :[")


def end():
    print("Good bye")


def sunny_bot():
    print("Hello, my name is Sunny. Lovely to meet you.:]")
    time.sleep(1.5)
    print("What should I call you?")


sunny_bot()


user = raw_input("My name is... >> ")
time.sleep(1.0)
print("Hi " + user + " I am your personal assistant chat bot!")


def greeting():
    if today.strftime("%H") >= 00:
        print("Good morning!" + user + ":]")
    elif 12 <= today.strftime("%H"):
        if today.strftime("%H") <= 7:
            print("Good afternoon! " + user + ":]")
    else:
        print("Good evening!" + user + ":]")


a = raw_input(">>")
if a == "what can you do":
    print("Here is the options you can ask me. Try anything! ;]\n[greeting]")
else:
    error_m()

# user's input
b = raw_input(">>")
if b == "greeting":
    greeting()
else:
    error_m()
    print("Here is the options you can ask me. Try anything! ;]\n[greeting]")







