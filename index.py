import tkinter as tk
import pyautogui 
import keyboard
import time 
import threading
from tkinter import messagebox
def th2():
    th = threading.Thread(target=press2)
    th.daemon = True
    th.start()
def press2():
    global input_text
    input_text=C.get()
    try:
      input_text=float(input_text)      
      L5.configure(text=f"설정하신 시간은\"{input_text}\"초 입니다")
      time.sleep(3)
      L5.configure(text="")                                        
    except:
      L5.configure(text="설정하신 시간이 이상합니다")
      time.sleep(2)
      L5.configure(text="다시 입력하세요")
      time.sleep(3)
      L5.configure(text="")                                        
      print("stop program.")      
   
def th():
    th = threading.Thread(target=press)
    th.daemon = True
    th.start()
def press():
    global input_text
    input_text=A.get()
    global a
    a=C.get() 
    try:
      a=float(a)
      L2.configure(text=f"누르실 키는\"{input_text}\"입니다")
      time.sleep(1)
      L2.configure(text="start:\'1\' exit:\'2\'\n rightClick:\'3\' leftClick:\'4\' ")  
      while 1:    
          if keyboard.is_pressed('1'):       
              L2.configure(text="stop:\'5\'") 
              while 1:
                pyautogui.press(input_text)
                print('Do it') 
                time.sleep(a) 
                if keyboard.is_pressed('5'):
                  L2.configure(text="Restart:click button")
                  time.sleep(3)
                  L2.configure(text="")                                        
                  print("stop program.")      
                  break
          elif keyboard.is_pressed('3'):
              L2.configure(text="stop:\'5\'")        
              while 1:               
                pyautogui.rightClick()
                print('Do it') 
                time.sleep(a)
                if keyboard.is_pressed('5'): 
                  L2.configure(text="Restart:click button")
                  time.sleep(3)
                  L2.configure(text="")                                        
                  print("stop program.")      
                  break                                       
          elif keyboard.is_pressed('4'): 
              L2.configure(text="stop:\'5\'")       
              while 1:               
                pyautogui.leftClick()
                print('Do it') 
                time.sleep(a)
                if keyboard.is_pressed('5'):
                  L2.configure(text="Restart:click button")
                  time.sleep(3)
                  L2.configure(text="")                                        
                  print("stop program.")      
                  break                                      
                               
          if keyboard.is_pressed('2'):
            L2.configure(text="Restart:click button")
            time.sleep(3)
            L2.configure(text="")
            print("stop program.")      
            break
    except:
      
      messagebox.showwarning("경고","입력하신 시간이 이상합니다")
      
        
    
window1=tk.Tk()
window1.geometry("600x500")
window1.resizable(False,False)
window1.title('Macro')

L1=tk.Label(window1,text=" 원하는 키를 입력하세요 \n ex) f12,enter,shift....",height=4)
L1.pack()

A=tk.Entry(window1)
A.pack(ipadx=10, padx=10)

L0=tk.Label(window1,text="",height=1)
L0.pack()

B=tk.Button(window1, text="Click",command=th)
B.pack()

L2=tk.Label(window1, text=' ',height=5)
L2.pack()

L3=tk.Label(window1,text="설정할 시간을 입력하세요",height=2)
L3.pack()

C=tk.Entry(window1)
C.pack(ipadx=10, padx=10)

L4=tk.Label(window1,text="",height=1)
L4.pack()

D=tk.Button(window1, text="Click",command=th2)
D.pack()

L5=tk.Label(window1, text=' ',height=5)
L5.pack()






window1.mainloop()


