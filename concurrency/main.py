import threading
import time

def fetch_user_data():
    for i in range(0,5):
        print(f"Fetching user data {i}")
        time.sleep(1)

def process_user_data():
    for i in range(0,3):
        print(f"Processing user data {i}")
        time.sleep(5)

fetch_thread = threading.Thread(target=fetch_user_data)        
process_thread = threading.Thread(target=process_user_data)        

fetch_thread.start()
process_thread.start()

fetch_thread.join()
# process_thread.join()

print("Hello")