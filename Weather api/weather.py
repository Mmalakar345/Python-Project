# All function modules importing
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Display creation
root=Tk()
root.title("Weather App")
root.geometry("900x500+300+50")
root.resizable(False,False)

# #################################### Search ##############################

#search box image import
Search_image=PhotoImage(file="Image\search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

# search box text write function
textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="lightgray")
textfield.place(x=50,y=40)
textfield.focus()


# Search icon working function
def getWeather():
    try:
        city=textfield.get()

        geolocator = Nominatim(user_agent="GEOAPIeXERCISES")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        # print(result)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather 
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7951909b84402fb22ac62d1bca7139bd"
        json_data = requests.get(api).json()
        print(json_data)
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        temp_min = int(json_data['main']['temp_min']-273.15)
        temp_max = int(json_data['main']['temp_max']-273.15)
        

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        mn.config(text=temp_min)
        mx.config(text=temp_max)

    except Exception as e:
        messagebox.showinfo("Weather App","City not found!! ")
        




# search icon seatting
Search_icon=PhotoImage(file="Image\search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg='#404040',command=getWeather)
myimage_icon.place(x=400,y=34)

# logo
Logo_image=PhotoImage(file="Image\logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

# Button box
Frame_image=PhotoImage(file="Image\Box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)


# Button frame labels creation
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400) 

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=230,y=400)

label3=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=375,y=400)

label4=Label(root,text="MIN_Temp",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=520,y=400)

label5=Label(root,text="MAX_Temp",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label5.place(x=655,y=400)



label6=Label(root,text="DESCRIPTION :",font=("Helvetica",15,"bold"),fg="black")
label6.place(x=300,y=340)


# Time clock
name=Label(root,font=("arial",15,"bold")) # FOR USE CLOCK NAME PROVIDE
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20)) # for use provide current location time
clock.place(x=30,y=130)


# temperature and condition
t=Label(font=('arial',70,'bold'),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

# Buttom frame labels output display creation
# Wind
w=Label(text="??",font=("arial",20,'bold'),bg="#1ab5ef")
w.place(x=125,y=430)
# humidity
h=Label(text="??",font=("arial",20,'bold'),bg="#1ab5ef")
h.place(x=244,y=430)
# Pressure
p=Label(text="??",font=("arial",20,'bold'),bg="#1ab5ef")
p.place(x=393,y=430)
# Min Temperature
mn=Label(text="??",font=("arial",20,'bold'),bg="#1ab5ef")
mn.place(x=538,y=430)
# Max Temperature
mx=Label(text="??",font=("arial",20,'bold'),bg="#1ab5ef")
mx.place(x=680,y=430)


# Decription
d=Label(text="??",font=("arial",20,'bold'),fg="#ee666d")
d.place(x=465,y=335)



root.mainloop()
