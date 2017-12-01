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

print('hello')
lis.join()