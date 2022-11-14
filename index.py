import tkinter as tk
import pyautogui 
import keyboard
import time 
import threading
def th():
    th = threading.Thread(target=press)
    th.daemon = True
    th.start()
def press():
    global input_text
    input_text=A.get()
    L2.configure(text="누르실 키는"+input_text+"입니다")
    time.sleep(1)
    L2.configure(text="start:\'1\' exit:\'2\'\n rightClick:\'3\' leftClick:\'4\' ")  
    while 1:    
        if keyboard.is_pressed('1'):       
            L2.configure(text="stop:\'5\'") 
            while 1:
              pyautogui.press(input_text)
              print('Do it') 
              time.sleep(0.01) 
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
              time.sleep(0.01)
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
              time.sleep(0.01)
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
        
    
window1=tk.Tk()
window1.geometry("600x400")
window1.resizable(False,False)
window1.title('매크로')

L1=tk.Label(window1,text=" 원하는 키를 입력하세요 \n ex) f12,enter,shift....",height=4)
L1.pack()

A=tk.Entry(window1)
A.pack(ipadx=10, padx=10)

L0=L1=tk.Label(window1,text="",height=1)
L0.pack()

B=tk.Button(window1, text="입력",command=th)
B.pack()

L2=tk.Label(window1, text=' ',height=5)
L2.pack()







window1.mainloop()


