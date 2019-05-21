import threading
import time
import random
import sys

stop_thread = False

#Ideas: 
    #the "run" function will be what is run when a thread has all of its food

class Customer(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

        self.hamburger = 0
        self.fries = 0
        self.soda = 0
    def run(self):
        print("Customer %s is eating... " % (self.name,))
        time.sleep(0.5)
        #print_time (self, self.name)
        print("Customer %s has finished eating. " % (self.name,))
        sys.exit()
        

class Chef(threading.Thread):
    def __init(self):
        threading.Thread.__init__(self)
    def run(self):
        x = random.randint(1,3)
        y = random.randint(1,3)
        while(x == y):
            y = random.randint(1,3)
            
    def makeFood(self):
        #We use 1 as hamburger, 2 as fries, 3 as soda
        return random.randint(1,3)
    

def print_time(thread, threadName):
    print ("%s has all of the food, consuming..." % (threadName, ))
    print ("%s has consumed all of the food" % (threadName, ))
    

if __name__ == "__main__":
    #Create threads for customers and the food they have an unlimited supply of
    #Counts keep track of how many times the customer gets all 3 food types and is run
    i = 0
    count = 0
    c1_count = 0
    c2_count = 0
    c3_count = 0
    while i <= 100:
        i = i + 1
        print("Iteration: %d" % (i,))
        x = 0
        y = 0
        customer1 = Customer(1, "Customer #1", 1)
        customer2 = Customer(2, "Customer #2", 2)
        customer3 = Customer(3, "Customer #3", 3)
        customer1.hamburger = 1
        customer2.fries = 1
        customer3.soda = 1
        chef = Chef()
        chef.start()
        chef.join()
        x = chef.makeFood()
        y = chef.makeFood()
        #Run makeFood function until x and y are different
        while(x == y):
            y = chef.makeFood()
        print (x)
        print(y)
        for i in range (0, 2):
            if(x == 1 or y == 1):
                customer2.hamburger = 1
                customer3.hamburger = 1
            if(x == 2 or y == 2):
                customer1.fries = 1
                customer3.fries = 1
            if(x == 3 or y == 3):
                customer1.soda = 1
                customer2.soda = 1
        if(customer1.hamburger and customer1.fries and customer1.soda):
            c1_count = c1_count + 1
            customer1.start()
            stop_thread = True
            customer1.join()
            stop_thread = False
        if(customer2.hamburger and customer2.fries and customer2.soda):
            c2_count = c2_count + 1
            customer2.start()
            stop_thread = True
            customer2.join()
            stop_thread = False
        if(customer3.hamburger and customer3.fries and customer3.soda):
            c3_count = c3_count + 1
            customer3.start()
            stop_thread = True
            customer3.join()
            stop_thread = False

        print("Counts: ")
        print("Customer 1: %d" % (c1_count))
        print("Customer 2: %d" % (c2_count))
        print("Customer 3: %d" % (c3_count))
