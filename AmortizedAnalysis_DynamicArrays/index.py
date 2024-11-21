class DynamicArray:
    def __init__(self):
        self.array = []
        self.capacity = 1
        self.size = 0
        self.total_resize_cost = 0

    def insert(self, value):
        if self.size == self.capacity:
            self._resize()
        self.array.append(value)
        self.size += 1

    def _resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        # Simulate the cost of copying elements
        resize_cost = self.size
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        self.total_resize_cost += resize_cost

    def get_amortized_cost(self):
        total_operations = self.size
        return (self.total_resize_cost + total_operations) / total_operations

# Simulation
posts = 10  # Number of posts to insert
dynamic_array = DynamicArray()

for i in range(posts):
    dynamic_array.insert(f"Post {i + 1}")

print(f"Total Posts: {dynamic_array.size}")
print(f"Amortized Cost per Insertion: {dynamic_array.get_amortized_cost():.2f}")
