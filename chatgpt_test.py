import queue
import random
import time

class Customer:
    def __init__(self, name):
        self.name = name
        self.entry_time = None

class QueueSystem:
    def __init__(self):
        self.customer_queue = queue.Queue()
        self.customers = {}
        self.queue_duration = 2 * 60  # 2 minutes

    def generate_unique_id(self):
        return len(self.customers) + 1

    def add_customer(self, customer):
        customer.entry_time = time.time()
        customer.id = self.generate_unique_id()
        self.customers[customer.id] = customer
        self.customer_queue.put(customer)
        print(f"Customer {customer.id} ({customer.name}) joined the queue.")

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} has been removed from the queue.")

    def simulate_queue(self, simulation_duration, simulation_speed=1):
        start_time = time.time()
        end_time = start_time + simulation_duration * 60 * 60  # Convert simulation duration from hours to seconds
        while time.time() < end_time:
            # Randomly determine whether a customer enters or leaves the queue
            if random.random() < (20 / 60):  # Approximately 20 customers per hour
                customer = Customer(f"Customer_{time.time()}")
                self.add_customer(customer)
            else:
                if not self.customer_queue.empty():
                    customer = self.customer_queue.get()
                    if time.time() - customer.entry_time > self.queue_duration:
                        self.remove_customer(customer.id)
                    else:
                        self.customer_queue.put(customer)

            time.sleep(1 / simulation_speed)  # Delay based on the simulation speed

# Example usage
queue_system = QueueSystem()
queue_system.simulate_queue(10, simulation_speed=100)  # Simulate for 10 hours at 100x speed
