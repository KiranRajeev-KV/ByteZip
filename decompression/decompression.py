import json
import os

class HeapNode():
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):  
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq
    
    def to_dict(self):
        return {
            'char': self.char,
            'freq': self.freq,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None,
        }

def removePadding(data):
    padding = data[:8]
    paddingLength = int(padding, 2)
    return data[8:][:-paddingLength]

def decodeHuffman(data, huffmanTree):
    output = ""
    node = huffmanTree
    for bit in data:
        node = node.left if bit == '0' else node.right
        if node.left is None and node.right is None:
            output += node.char
            node = huffmanTree
    return output

def loadHuffmanTree(filePath):
    with open(filePath, 'r') as f:
        tree_data = json.load(f)
    
    def build_tree(node_data):
        if node_data is None:
            return None
        node = HeapNode(node_data['char'], node_data['freq'])
        node.left = build_tree(node_data['left'])
        node.right = build_tree(node_data['right'])
        return node
    
    return build_tree(tree_data)

def decompress(filePath):
    fileName, fileExt = os.path.splitext(filePath)
    outputFileName = fileName + "_decompressed.txt"

    huffmanTreePath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scripts', 'huffman_trees', 'huffman_tree.json')
    huffmanTree = loadHuffmanTree(huffmanTreePath)
    
    with open(filePath, 'rb') as file:
        outputString = ""
        byte = file.read(1)
        
        while byte:
            byte = ord(byte)
            bit = bin(byte)[2:].rjust(8, '0')
            outputString += bit
            byte = file.read(1)
        
    outputString = removePadding(outputString)
    outputString = decodeHuffman(outputString, huffmanTree)
    
    with open(outputFileName, 'w', encoding='utf-8') as output:
        output.write(outputString)
        
    print("Decompression complete. Output file: " + outputFileName)
    return outputFileName
