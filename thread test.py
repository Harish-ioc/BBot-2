import threading
import time

def while_loop1():
    for i in range(0,5):
        print("Loop 1 is running")
        time.sleep(0.01)  # Simulate some work

def while_loop2():
    for i in range(0,5):
        print("Loop 2 is running")
        time.sleep(0.01)  # Simulate some work

# camera - face detect - position 
#  listen - txt - check -  ask - speak 

# Create threads for each while loop
thread1 = threading.Thread(target=while_loop1)
thread2 = threading.Thread(target=while_loop2)

# Start both threads
thread1.start()
thread2.start()

# Join both threads (wait for them to finish)
thread1.join()
thread2.join()
