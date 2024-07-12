import threading

def sample():
    print("This is a sample function to test threading function")



for i in range(0,5):
  t = threading.Thread(target=sample)
  t.start()
