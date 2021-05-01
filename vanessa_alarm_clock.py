# Vanessa's Alarm Clock Python Code (for lack of a better title)
# Simplified Alarm Clock. No Tkinter
#Goal: create a simplified alarm clock. 

import tkinter as tk
from datetime import datetime, date
import time
import pygame
from threading import *

print("Hello World. Time to Create an Alarm Clock.")


def set_time():
    get_current_time = datetime.now()
    current_time = get_current_time.strftime("%H:%M:%S %p")
    lbl.config(text = current_time)
    lbl.after(1000, set_time)
    return 

def threading():
    # call set_alarm_clock
    t1=Thread(target=set_alarm_clock)
    t1.start()

def set_alarm_clock():
    alarm_time_input = f"{hour.get()}:{min.get()}:{sec.get()}"

    while True:
        now = datetime.now().strftime("%H:%M:%S")
        
        if now == alarm_time_input:
            play_alarm()
            break

def play_alarm():

    print("Wake Up!")
    pygame.mixer.init()
    pygame.mixer.music.load("alarm-clock-01.wav")
    pygame.mixer.music.play()
    time.sleep(5)
    

def stop_alarm_clock():

    pygame.mixer.music.stop()


clock = tk.Tk()
clock.title("Vanessa's Alarm Clock")
clock.geometry("400x200")
lbl = tk.Label(clock, font = ('calibri', 40, 'bold'),
    background = 'purple',
    foreground = 'white')
lbl.pack(anchor = 'center', ipadx=30, padx=30)

set_time()

setYourAlarm = tk.Label(clock,text = "Set time to wake you up",fg="blue",relief = "solid",font=("Helevetica",10,"bold")).place(x=0, y=70)

# The Variables we require to set the alarm(initialization):
hour = tk.StringVar() # StringVar() is tkinter types which holds a string
min = tk.StringVar()
sec = tk.StringVar()

#Time required to set the alarm clock:
hourTime = tk.Entry(clock, textvariable = hour, bg="pink", width=15).place(x=100,y=100)
minTime  = tk.Entry(clock, textvariable = min, bg="pink", width=15).place(x=150,y=100)
secTime  = tk.Entry(clock, textvariable = sec, bg="pink", width=15).place(x=200,y=100)

#To take the time input by user:
submit = tk.Button(clock,text = "Set Alarm",fg="red",width = 10,command=threading).place(x =100,y=140)
stop = tk.Button(clock, text = "Stop Alarm",fg="red",width=10, command=stop_alarm_clock).place(x=240,y=140)

clock.mainloop()

