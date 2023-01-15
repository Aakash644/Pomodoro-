from itertools import count 
from tkinter import *  # basic tok import 
from turtle import bgcolor  
import time  # time 

import math # for math.floor
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20 

window=Tk() # creating basic window
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():  # reset func
    window.after_cancel(timer)  #reset timer using window after cancel
    title_label.config(text="TIMER",font=("courier",50),bg=YELLOW,fg=GREEN)
    canvas.itemconfig(timertext,text="00:00")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
global reps 
reps=0
def start(): 
    global reps  
    reps +=1 
    
    
    if(reps%8==0): 
        title_label.config(text="Break",fg=RED)
        count_down(20*60)  
       
    elif(reps%2==0 or reps%4==0 or reps%6==0): 
        title_label.config(text="Break",fg=PINK)
        count_down(5*60)  
        
    else: 
        title_label.config(text="Work",fg=GREEN)
        count_down(25*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count): 
    min=math.floor(count/60) 
    sec=count%60 
    if(sec<10): # if sec<0 then add "0" to sec
        sec=f"0{sec}"
    
    canvas.itemconfig(timertext, text= f"{min}:{sec}" )  #updating the timertext
    if(count>0): 
        global timer 
        timer=window.after(1000,count_down,count-1)  #displaying timertext after 1 sec
    else : 
        #if count==0 then start again reps+=1
        start() 

# ---------------------------- UI SETUP ------------------------------- #

window.title("POMODORO")  # creating title of the application 
window.config(padx=50,pady=50,bg=YELLOW)   # using config to change orininality or update the objects
 
canvas=Canvas(width=300,height=300,bg=YELLOW,highlightthickness=0)  # creating a canvas of size(300*300)
title_label=Label(text="TIMER",font=("courier",50),bg=YELLOW,fg=GREEN)  # creating label with text=Timer using grid() 
                                                                         #or pack()
title_label.grid(column=1,row=0) 
tomato=PhotoImage(file=r"C:\Users\Acer\Downloads\pomodoro-start\tomato.png") # adding photoimage 
canvas.create_image(153,152,image=tomato)  # using canvas to create_image with x,y coordinates and image
timertext=canvas.create_text(153,170,text="00:00",fill="white",font=("Arial",30,"bold") )
canvas.grid(column=1,row=1)  # creating timertext and filling with white colour

start_button=Button(text="Start",command=start)
start_button.grid(column=0,row=2)   # creating start button with start()


reset_button=Button(text="Reset",command=reset)
reset_button.grid(column=2,row=2) # creating reset button with reset()





window.mainloop() # mainloop()