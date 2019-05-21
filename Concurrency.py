import threading
import time

exitFlag = 0

#Ideas: 
    #the "run" function will be what is run when a thread has all of its food

class Customer(threading.Thread):
    def __init__(self, threadID, name, counter, providedFood):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.providedFood = providedFood
    def run(self):
        print("Starting " + self.name)
        print_time (self.name, self.counter, 5)
        print ("Exiting " +self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("Customer %s has all of the food, consuming..." % (threadName, ))
        #print ("%s: %s" % (threadName, time.ctime(time.time())))
        print ("Customer %s has consumed all of the food" % (threadName, ))
        counter -= 1
    

if __name__ == "__main__":
    thread1 = Customer(1, "Customer #1", 1, "Hamburger")
    thread2 = Customer(2, "Customer #2", 2, "Fries")
    thread3 = Customer(3, "Customer #3", 3, "Soda")

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print("Exiting Main Thread")
