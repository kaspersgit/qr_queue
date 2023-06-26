import queue
import uuid
from datetime import datetime
import time 

class Customer:
    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())
        self.join_ms = None

class QueueSystem:
    def __init__(self):
        self.customer_queue = queue.Queue()
        self.customers = {}

    def add_join_queue_ms(self):
        return int(round(time.time() * 1000))

    def add_customer(self, customer):
        customer.join_ms = self.add_join_queue_ms()
        self.customers[customer.id] = customer
        self.customer_queue.put(customer)

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            self.recreate_queue()

    def recreate_queue(self):
        new_queue = queue.Queue()
        for customer in self.customers.values():
            new_queue.put(customer)
        self.customer_queue = new_queue

    def display_queue(self):
        if self.customer_queue.empty():
            print("The queue is empty.")
        else:
            print("Current queue:")
            for customer in list(self.customer_queue.queue):
                print(f"Customer ID: {customer.id}, Name: {customer.name}")

    def give_queue_dict(self):
        if self.customer_queue.empty():
            return
        else:
            queue = {}
            for index, customer in enumerate(list(self.customer_queue.queue)):
                queue[index] = {"id": customer.id, "join_ms": customer.join_ms, "name": customer.name} 

            return queue

    