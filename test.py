import threading
import multiprocessing
import time
import random
import sys

#Ideas: 
    #the "run" function will be what is run when a thread has all of its food

class Customer(multiprocessing.Process):
    def __init__(self, threadID, name, counter):
        multiprocessing.Process.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

        self.hamburger = 0
        self.fries = 0
        self.soda = 0
    def run(self):
        print("Customer %s is eating... " % (self.name,))
        time.sleep(1)
        #print_time (self, self.name)
        #print ("Customer %s has finished eating. " % (self.name,))
        print("Customer %s has finished eating. " % (self.name,))
        self.terminate()
        

class Chef(threading.Thread):
    def __init(self):
        threading.Thread.__init__(self)
        madeBurger = 0
        madeFries = 0
        madeSoda = 0
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
    c1_count = 0
    c2_count = 0
    c3_count = 0
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
    #customer1.start()
    #customer2.start()
    #customer3.start()
    for i in range (1, 100):
        chef.join()
        x = chef.makeFood()
        y = chef.makeFood()
        #Run makeFood function until x and y are different
        while(x == y):
            y = chef.makeFood()
    
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
        '''
        if(customer1.fries == 0 and x == 2 or y == 2):
            customer1.fries = 1
        elif(customer1.soda == 0 and x == 3 or y == 3):
            customer1.soda = 1
        elif(customer2.hamburger == 0 and x == 1 or y == 1):
            customer2.hamburger = 1
        elif(customer2.soda == 0 and x == 3 or y == 3):
            customer2.soda = 1
        elif(customer3.hamburger == 0 and x == 1 or y == 1):
            customer3.hamburger = 1
        elif(customer3.fries == 0 and x == 2 or y == 2):
            customer3.fries = 1
        '''
        if(customer1.hamburger and customer1.fries and customer1.soda):
            c1_count = c1_count + 1
            customer1.start()
            customer1.join()
        if(customer2.hamburger and customer2.fries and customer2.soda):
            c2_count = c2_count + 1
            customer2.start()
            customer2.join()
        if(customer3.hamburger and customer3.fries and customer3.soda):
            c3_count = c3_count + 1
            customer3.start()
            customer3.join()
        
        '''
        customer1.fries = 0
        customer1.soda = 0
        customer2.hamburger = 0
        customer2.soda = 0
        customer3.hamburger = 0
        customer3.fries = 0
        '''
    print("Counts: ")
    print("Customer 1: %d" % (c1_count))
    print("Customer 2: %d" % (c2_count))
    print("Customer 3: %d" % (c3_count))
