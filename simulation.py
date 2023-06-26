from utils.queues import *
import random
import plotly.graph_objects as go
import numpy as np

# functions 
def compute_metrics(queue, arrival_rate):
    """Compute average number of customers and wait time.
    
    results: TimeSeries of queue lengths
    system: System object
    
    returns: L, W
    """
    L = np.average(list(queue.values()))
    W = L / arrival_rate
    return L, W

# Set variables

# One step per second
steps = 3600 * 10

# activity with probability as chance per second
arrival_rate = 0.165
removal_rate = 0.01

# Ride specs
ride_start_interval = 60
ride_spots = 10

# Set up
queue_system = QueueSystem()
queue_length = {}

# Simulate X number of steps
for i in range(steps):
    # to add customer to queue
    if random.random() < arrival_rate:
        add_customer = Customer("Derek")
        queue_system.add_customer(add_customer)

    # to remove customer from queue
    if random.random() < removal_rate:
        # choose random customer to be removed
        queue_dict = queue_system.give_queue_dict()
        if queue_dict:      
            customer = random.choice(list(queue_dict.values()))
            queue_system.remove_customer(customer['id'])

    # To remove customers as they board attraction
    if i % ride_start_interval == 0:
        # Request queue in dict form 
        queue_dict = queue_system.give_queue_dict()
        if queue_dict:      
            for key, customer in queue_dict.items():
                if key < ride_spots:
                    queue_system.remove_customer(customer['id'])

    # get regular updates on the queue
    if i % 37 == 0:
        print(f'At time t: {i}')
        # Display the updated queue
        queue_system.display_queue()

    # Keep track of queue length
    if isinstance(queue_system.give_queue_dict(), dict):
        queue_length[i] = len(queue_system.give_queue_dict())
    else:
        queue_length[i] = 0


## Plot simulation
# Extract keys and values from the dictionary
keys = list(queue_length.keys())
values = list(queue_length.values())

# Creating a bar plot
fig = go.Figure(data=go.Line(x=keys, y=values))

# Adding axis labels and title
fig.update_layout(
    xaxis_title='Seconds from opening',
    yaxis_title='Length of queue',
    title='Queue length over time'
)

# Displaying the plot
fig.show()
    
L, W = compute_metrics(queue_length, arrival_rate)
print(f'Average queue length: {L}')
print(f'Average waiting time: {W}')