from collections import deque, defaultdict

class SocialNetworkGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_connection(self, user1, user2):
        # Add undirected edge
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)

    def find_mutual_friends(self, user1, user2):
        # Use BFS to find direct friends
        def bfs(user):
            visited = set()
            queue = deque([user])
            friends = set()

            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    friends.update(self.graph[current])
                    queue.extend(self.graph[current])
            friends.discard(user)  # Remove self from the friend list
            return friends

        # Get friend lists of both users
        friends_user1 = bfs(user1)
        friends_user2 = bfs(user2)

        # Find mutual friends
        mutual_friends = friends_user1.intersection(friends_user2)
        return mutual_friends

# Example usage
network = SocialNetworkGraph()

# Adding connections (friendships)
connections = [
    ("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Charlie"),
    ("Bob", "David"), ("Charlie", "Eve"), ("David", "Eve")
]

for u1, u2 in connections:
    network.add_connection(u1, u2)

# Find mutual friends
user1 = "Alice"
user2 = "Bob"
mutual = network.find_mutual_friends(user1, user2)

print(f"Mutual Friends between {user1} and {user2}: {mutual}")
