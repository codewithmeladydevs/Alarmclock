#                                        *Welcome to DataFlair Alarm Clock*


#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
#import winsound
import pygame


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)  # sleep(secs) is a method function inside the module time, which suspends execution of the calling thread for the given number of secs
        current_time = datetime.datetime.now()  # now(tz=None) is a class method of the class datetime contained in the module datetime it returns the current local date and time
        now = current_time.strftime("%H:%M:%S") # returns a string representing the date, controlled by explicit format
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        pygame.init()   # initialize all imported pygame modules
        pygame.mixer.init() # initialize the mixer module for sound loading and playback
        if now == set_alarm_timer:
            print("Time to Wake up")
            #winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            pygame.mixer.music.load("alarm-clock-01.wav")
            pygame.mixer.music.play()
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}" # f-string - formatted string literals are string literals that have a 'f' at the beginning and curly braces containing expressions that will be replaced with their values.  The expressions are evaluted at runtime and then formatted using the __format__ protocol.
    alarm(set_alarm_timer)

clock = Tk()  # initialize tkinter
clock.title("DataFlair Alarm Clock")
clock.iconbitmap(r"dataflair-logo.ico")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar() # StringVar() is tkinter types which holds a string
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()
#Execution of the window.

