import random, time, keyboard
import tkinter as tk

app = tk.Tk()
app.minsize(height=500, width=500)

l2 = tk.Label(text='Awwwwwwwww')
l2.pack()
for i in range(10):
    l2.configure(text=str(random.randint(1, 100)))
    time.sleep(0.5)

app.mainloop()