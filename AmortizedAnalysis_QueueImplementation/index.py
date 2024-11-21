class Queue:
    def __init__(self):
        self.queue = []
        self.move_count = 0  # Tracks how many times we have moved elements

    def enqueue(self, customer):
        self.queue.append(customer)
        print(f"Enqueued: {customer}")

    def dequeue(self):
        if self.queue:
            customer = self.queue.pop(0)
            print(f"Dequeued: {customer}")
        else:
            print("Queue is empty!")

    def move_elements(self):
        # Move all elements to the front (simulated by reversing the queue)
        self.queue = self.queue[::-1]
        self.move_count += 1
        print(f"Moved elements to the front. Total moves: {self.move_count}")

    def get_amortized_cost(self, total_operations):
        # Amortized cost per operation is the total cost divided by the number of operations
        total_cost = len(self.queue) * self.move_count + total_operations  # Example of cost calculation
        return total_cost / total_operations

# Simulate the queue operations
queue = Queue()

# Perform 10 enqueues
for i in range(1, 11):
    queue.enqueue(f"Customer {i}")

# Move elements to the front (only once in this simulation)
queue.move_elements()

# Perform 10 dequeues
for i in range(1, 11):
    queue.dequeue()

# Calculate the amortized cost after 21 operations
total_operations = 21
amortized_cost = queue.get_amortized_cost(total_operations)
print(f"Amortized cost per operation: O({amortized_cost})")
