# Implement a file compression algorithm that uses binary tree. Your program should  allow 
# the  user  to  compress  and  decompress  messages containing alphabets  using  the 
# standard  Huffman  algorithm  for  encoding  and  decoding. 


import heapq
import collections
import os

class TreeNode:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    priority_queue = [TreeNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = TreeNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_huffman_codes(root):
    codes = {}

    def traverse(node, code=""):
        if node:
            if node.char:
                codes[node.char] = code
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(root)
    return codes

def compress(message, codes):
    compressed_bits = ""
    for char in message:
        compressed_bits += codes[char]
    return compressed_bits

def decompress(compressed_bits, root):
    decompressed_message = ""
    current = root
    for bit in compressed_bits:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char:
            decompressed_message += current.char
            current = root
    return decompressed_message

def huffman_compress(input_file, output_file):
    with open(input_file, 'r') as file:
        message = file.read()

    frequencies = collections.Counter(message)
    root = build_huffman_tree(frequencies)
    codes = generate_huffman_codes(root)
    compressed_bits = compress(message, codes)

    with open(output_file, 'w') as file:
        file.write(compressed_bits)

def huffman_decompress(input_file, output_file):
    with open(input_file, 'r') as file:
        compressed_bits = file.read()

    root = build_huffman_tree({})
    current = root
    decompressed_message = ""

    for bit in compressed_bits:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char:
            decompressed_message += current.char
            current = root

    with open(output_file, 'w') as file:
        file.write(decompressed_message)

# Example usage:

# Compress a file
input_file = "input.txt"
output_file = "compressed.txt"
huffman_compress(input_file, output_file)

# Decompress the compressed file
decompressed_file = "decompressed.txt"
huffman_decompress(output_file, decompressed_file)

