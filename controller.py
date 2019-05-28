
import sys
import time
from firebase import firebase
dbase = 'https://database_name.firebaseio.com/'
firebase = firebase.FirebaseApplication( dbase, None)
from pynput.keyboard import Key, Listener

control_list = ['Key.space', 'Key.up', 'Key.down', 'Key.left', 'Key.right']
def counter():
    if 'cnt' not in counter.__dict__:
        counter.cnt = 0
    counter.cnt += 1
    return counter.cnt

def keypress(Key):
    if str(Key) == 'Key.esc':
        sys.exit()
    elif str(Key) not in control_list:
        pass
    else:
        firebase.put('/key-press/', 'counter', counter())
        firebase.put('/key-press/', 'key_data', str(Key))

with Listener(on_press = keypress) as listener:
        listener.join()

 
