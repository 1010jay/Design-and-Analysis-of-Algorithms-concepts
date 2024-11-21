import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Make HuffmanNode comparable for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(frequencies):
    # Create a priority queue with initial nodes
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build the tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # Root of the tree

# Function to generate Huffman codes
def generate_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    
    if root is None:
        return codes

    if root.char is not None:  # Leaf node
        codes[root.char] = current_code

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
    
    return codes

# Example Usage
if __name__ == "__main__":
    # Example character frequencies
    frequencies = {
        'A': 5,
        'B': 9,
        'C': 12,
        'D': 13,
        'E': 16,
        'F': 45
    }

    # Build the Huffman Tree
    huffman_tree = build_huffman_tree(frequencies)

    # Generate Huffman Codes
    huffman_codes = generate_codes(huffman_tree)

    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    print("\nEncoded String Example:")
    example = "ABBCCCDDDD"
    encoded = "".join(huffman_codes[char] for char in example)
    print(f"Original: {example}")
    print(f"Encoded: {encoded}")
