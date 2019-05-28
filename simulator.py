
# coding: utf-8

# In[20]:


import sys,time
from firebase import firebase
from pynput.keyboard import Key, Controller

dbase = 'https://database_name.firebaseio.com/'

firebase = firebase.FirebaseApplication( dbase, None)

keyboard = Controller()


counter = firebase.get('/key-press/counter/', '')
while(1):
    counter_up = firebase.get('/key-press/counter/', '')
    if counter != counter_up:
        counter = counter_up
        key_data = firebase.get('/key-press/key_data/', '')
        if key_data == 'Key.esc':
            sys.exit() 
        else:
            keyboard.press(eval(key_data))
            keyboard.release(eval(key_data))

