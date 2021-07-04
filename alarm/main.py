import datetime
from playsound import playsound
alarmH = int(input("What hour do you want the alarm to ring? "))
alarmM = int(input("What minute do you want the alarm to ring? "))
amPm = str(input("am or pm? "))

print("Waiting for alarm",alarmH,alarmM,amPm)
if (amPm == "pm"):
        alarmH = alarmH + 12
while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute) :
        print("Time to wake up")
        playsound('annoying_dance.mp3')
        if(alarmH+2 == datetime.datetime.now().hour and
            alarmM+2 == datetime.datetime.now().minute) :
            print("Time to wake up")
            playsound('annoying_dance.mp3')
        break