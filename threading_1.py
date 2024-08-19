#thread = a flow of execussion. Like a separate order of instractions.
# However each thread  takes a turn running to achieve concurrency
# GIL= global interpreter lock
# allows only one thread to hold the control of  the PY interpreter 

#cpu bound : wait for internal events   multiproc
#io bound: wait for external events     multithreading


import threading
import time



def eat ():
    time.sleep(5)
    print("You eat ")

def take_a_sh ():
    time.sleep(6)
    print("You take_a_sh ")

def get_dressed():
    time.sleep(7)
    print("You get_dressed ")



# или все это одновременно
x= threading.Thread(target=eat,args=())
x.start()


y= threading.Thread(target=take_a_sh,args=())
y.start()

z= threading.Thread(target=get_dressed,args=())
z.start()

x.join()
y.join()
z.join()



print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

