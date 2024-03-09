from tkinter import *
from time import *

# def quoteMessage():
#     quote = ["You can keep moving all", "i am blessed", "You are piece of shit", "hey you there!, get up and work!"]
#     i = ""
#     for i in quote:
#         quote_label.config(text=i)
#     return i







def update():
    message = "Hello world, This is influence. \n Today is another day to be reminded that you Suck! \n So prove me wrong, suckers"
    message_label.config(text=message)

    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()
window.title("Influence Clock")
window.geometry("600x500")

# quote_label = Label(window, font=("Ink Free", 25))
# quote_label.pack()



message_label = Label(window, font=("Ink Free", 20), fg="red")
message_label.pack()

time_label = Label(window, font=("Arial", 50), fg="#00ff00", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25))
day_label.pack()

date_label = Label(window, font=("Ink Free", 30))
date_label.pack()




# quoteMessage()
update()





window.mainloop()