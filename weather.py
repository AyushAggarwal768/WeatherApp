# -*- coding: utf-8 -*-
from tkinter import *
import time 
import datetime
import requests
from tkinter import messagebox
root = Tk()
root.geometry("600x600")
root.title("Weather App")
root.configure(background="white")

api = 'https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22&q='

#--------------------frame------------------------------------------------------

fr = Frame(root, width = 600, height = 600, bg="white",  relief="flat")
fr.pack()

#----------------lable----------------------------------------------------------

lbl = Label(fr, font=( 'arial' ,23, 'bold' ),text="Weather Details",fg="black",bg="white")
lbl.grid(row=0,column=0)
lbl = Label(fr, font=( 'arial' ,15, ),text="Enter Your City : ",fg="black",bg="white")
lbl.grid(row=1,column=0)
txt = Entry(fr,font=('arial' ,12,'bold') , bd=6,insertwidth=4,bg="Sky Blue" ,justify='right')
txt.grid(row=2,column=0)  

#-------------------------------------------------------------------------------

def show_detail():
        city=txt.get()
        url = api+city   
        data = requests.get(url).json()
        cityL= Label(fr,text= city,font=('arial' ,15,'bold'),fg='blue',bg='white')
        cityL.grid(row=3,column=0)
        show_weather(data) 
        
submit_1 = Button(fr,font=('arial' ,12,'bold'),text='Show Weather',command=show_detail)
submit_1.grid(row= 2,column=1)

#-------------------------------------------------------------------------------
                
def show_weather(data):
     localtime=time.asctime(time.localtime(time.time()))
     lblinfo=Label(fr,text=localtime,font = ('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 4,column=0)
#-------------------------------------------------------------------------------   
     lblinfo=Label(fr,text="Temperature :",font=('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 5,column=0)
     lblinfo=Label(fr,text="Max Temperature :",font=('arial' ,10,'bold'),bg='white')
     lblinfo.grid(row= 6,column=0)
     lblinfo=Label(fr,text="Min Temperature :",font=('arial' ,10,'bold'),bg='white')
     lblinfo.grid(row= 7,column=0)
     temp = data['main']['temp']
     t = str(temp)+str(' °C')
     
     temp_max = data['main']['temp_max']
     tmax = str(temp_max)+str(' °C')

     temp_min = data['main']['temp_min']
     tmin = str(temp_min)+str(' °C')
     
     lblinfo=Label(fr,text=t,font = ('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 5,column=1)
     lblinfo=Label(fr,text=tmax,font = ('arial' ,10,'bold'),bg='white')
     lblinfo.grid(row= 6,column=1)
     lblinfo=Label(fr,text=tmin,font = ('arial' ,10,'bold'),bg='white')
     lblinfo.grid(row= 7,column=1)
#-------------------------------------------------------------------------------     
     lblinfo=Label(fr,text="Wind Speed :",font=('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 8,column=0)
     wind = data['wind']['speed']
     w = str(wind)+str(' m/s')
     lblinfo=Label(fr,text=w,font = ('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 8,column=1)
#-------------------------------------------------------------------------------

     lblinfo=Label(fr,text="Type :",font=('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 9,column=0)
     description = data['weather'][0]['description']
     d = str(description)
     lblinfo=Label(fr,text=d,font = ('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 9,column=1)     

#-------------------------------------------------------------------------------     
  
     lblinfo=Label(fr,text="Humidity :",font=('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 10,column=0)
     humid = data['main']['humidity']
     h = str(humid)+str(' %')
     lblinfo=Label(fr,text=h,font = ('arial' ,12,'bold'),bg='white')
     lblinfo.grid(row= 10,column=1)     

#------------------------------------------------------------------------------- 

def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return   
        

exit=Button(fr,font=('arial' ,12,'bold'),text="Exit",command=qExit)
exit.grid(row=13, column=0)

           
root.mainloop()
