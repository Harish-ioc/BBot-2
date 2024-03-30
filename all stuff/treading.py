import threading
import queue
import time

# Define a function that will run in the secondary thread
def my_function(output_queue):
    for i in range(5):
        # Simulate some work
        time.sleep(1)

        # Send data to the main thread
        data = f"Data from secondary thread: {i}"
        output_queue.put(data)

# Create a queue to pass data between threads
data_queue = queue.Queue()

# Create a thread and pass the function and the queue to it
my_thread = threading.Thread(target=my_function, args=(data_queue,))

# Start the thread
my_thread.start()

# The main thread can continue doing other work
for _ in range(3):
    print("Working in the main thread")
    received_data = data_queue.get()
    print("Received data in the main thread:", received_data)

    time.sleep(1)

# Wait for the thread to finish (optional)
# my_thread.join()

# Retrieve data from the queue sent by the secondary thread


print("Main thread and parallel thread have finished.")
