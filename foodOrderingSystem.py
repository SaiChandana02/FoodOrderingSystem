from collections import deque
from concurrent.futures import thread
from threading import Thread, current_thread
from time import sleep, time


class Queue:
    def __init__(self):
        self.container = deque()
    
    def enqueue(self,element):
        self.container.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty!!")
            return True
        return self.container.popleft()
    
    def isEmpty(self):
        if len(self.container)==0:
            return True
        return False
    
    def front(self):
        if self.isEmpty():
            print("queue is empty!!")
            return True
        return self.container[0] 


class FoodOrdering:
    def __init__(self,orders):
        self.orders = orders
        self.queue = Queue()


    def placeOrder(self):
        sleep(0.5)
        for order in self.orders:
            self.queue.enqueue(order)
            sleep(0.5)
        return

    def serveOrder(self):
        sleep(1)
        while not self.queue.isEmpty():
            print("serving order "+self.queue.dequeue())
            sleep(2)
        return 


orders = ['pizza','samosa','pasta','biryani','burger']
foodOrder = FoodOrdering(orders)
t1 = Thread(target = foodOrder.placeOrder)
t2 = Thread(target = foodOrder.serveOrder)

t1.start()
t2.start()