import serial
import math
import pyautogui
import matplotlib.pyplot as plt
from pynput import keyboard
from pynput import keyboard

def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc: return False # stop listener
    if k in ['1', '2', 'left', 'right']: # keys interested
        # self.keys.append(k) # store it in global-like variable
        print('Key pressed: ' + k)
        return False # remove this if want more keys

lis = keyboard.Listener(on_press=on_press)
lis.start()


# Collect events until released

pyautogui.MINIMUM_DURATION=0
pyautogui.MINIMUM_SLEEP=0
pyautogui.PAUSE=0
xl=[]
ax=ay=az=0
i=0
lis.join()
while True:

    try:
            ser = serial.Serial('/dev/ttyACM1', 38400, timeout=1)
            tx,ty,tz=ax,ay,az

            # request data by sending a dot
            ser.write(b".")
            # while not line_done:
            line = ser.readline()

            angles = line.split(b",")
            ax = float(angles[0])
            ay = float(angles[1])
            az = float(angles[2])
            dx = ax - tx
            dy = ay - ty
            dz = az - tz
            print(dy,dx,dz)

            if(abs(dx)<0.1):
                dx=0
            if (abs(dy) < 0.1):
                dy = 0
            if (abs(dz) < 0.1):
                dz = 0
            x,y,z = math.exp(abs(dx)/30)*dx*40,math.exp(abs(dy)/50)*dy*40,math.exp(abs(dz)/50)*dz*40

            pyautogui.moveRel(int(x),int(y))

    except Exception as e:
         print(e)
         pass
        #raty = float(data[1])
    #ratz = float(data[2])
    #print(ratx,raty,ratz)
