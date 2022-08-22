import keyboard
import time
import tkinter as tk

def restart():
    n = input('Choose : ')
    if str(n) == '1': press(5)
    elif str(n) == '2': return
    else: 
        print('Plz Select 1 Or 2') 
        restart()

def press(x):
    lst = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'] #สร้างลิสต์ไว้เป็นตัวแม่พิมพ์
    if keyboard.is_pressed('q'):
        print('Exit!!!') #ถ้ากด q แล้วจะออกเกม
        return
    lst[x] = '\\/' #กำหนดตำแหน่งรถ
    print(''.join(lst)) #แสดงตำแหน่งรถ
    time.sleep(0.2)
    if keyboard.is_pressed('A'): #ถ้ากด A D จะเลี้ยว
        x -= 1
    if keyboard.is_pressed('D'):
        x += 1
    if x == 0 or x == len(lst)-1: #ถ้าเลี้ยวจนค่า x = 0 หรือเท่ากัน lenlst ของขอบถนน รถจะพัง
        print('Your Car Crash!!!')
        print('1.Restart\n2.Exit!!')
        return restart()
    press(x)
press(5)