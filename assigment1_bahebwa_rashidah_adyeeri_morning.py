
#context manager  is an object that defines a temporary context for a block of code
#example one
#opens a file and returns a context manager instance
file = 'example.txt' 
 # Replace with the actual file path

# Using a context manager to handle file resources
with open(file, 'r') as file:
    # Perform operations on the file
    for line in file:
        # Process each line of the file
        print(line)

# File is automatically closed outside the context manager

#mutli-threading and mulit-processing
#techniques that can be used to improve performance of a python program
#mutli-threading is where multiple threads are created within a single process
#mutli-processing is where multiple threads are created within a single process

import threading

def print_numbers():
    for i in range(1, 11):
        print("Thread 1:", i)

def print_letters():
    for i in range(ord('A'), ord('K')):
        print("Thread 2:", chr(i))

# Create the threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Main thread execution completed.")

#example of mult_prcocessing
import multiprocessing

def print_numbers():
    for i in range(1, 11):
        print("Process 1:", i)

def print_letters():
    for i in range(ord('A'), ord('K')):
        print("Process 2:", chr(i))

# Create the processes
process1 = multiprocessing.Process(target=print_numbers)
process2 = multiprocessing.Process(target=print_letters)

# Start the processes
process1.start()
process2.start()

# Wait for the processes to finish
process1.join()
process2.join()

print("Main process execution completed.")



