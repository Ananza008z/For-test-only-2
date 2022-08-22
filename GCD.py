import win32, win32con
import random
import keyboard
import time
import pyautogui
import tkinter as tk

def press(x):
    lst = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|']
    if keyboard.is_pressed('q'):
        print('Exit!!!')
        return
    label1.configure(text=''.join(lst))
    label3.configure(text=''.join(lst))
    label4.configure(text=''.join(lst))
    lst[x] = '/\\'
    label2.configure(text=''.join(lst))
    time.sleep(0.2)
    if keyboard.is_pressed('A'):
        x -= 1
    if keyboard.is_pressed('D'):
        x += 1
    if x == 0 or x == len(lst):
        print('Your Car Crash!!!')
        return
    press(x)


show = tk.Tk()
show.title('Carrrrrrr!!!')
label1 = tk.Label()
label2 = tk.Label()
label3 = tk.Label()
label4 = tk.Label()

label4.pack()
label1.pack()
label2.pack()
label3.pack()
start_bt = tk.Button(text='start', command=press(5)).pack()

show.geometry('500x500')
show.mainloop()