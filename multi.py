import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1.5)

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(2)


# print_numbers()
# print_letters()


# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# # Start threads
thread1.start()
thread2.start()

# # Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished.")
