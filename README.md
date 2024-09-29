# ByteZip

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Introduction
ByteZip is a tool designed to compress and decompress files efficiently. This project was created by me and my friend as part of our Data Structures and Algorithms course.

## Features
- **Compression**: Efficiently compresses text files using Huffman coding.
- **Decompression**: Restores original files from the compressed format.
- **Future Support**: Planned support for additional file types, including images and PDFs.

## Implementation Steps

### Compression
1. Build a frequency dictionary.
2. Create a priority queue (using a MinHeap).
3. Construct the Huffman Tree by selecting the two minimum nodes and merging them.
4. Assign codes to characters by traversing the tree from the root.
5. Encode the input text by replacing each character with its corresponding code.
6. If the overall length of the final encoded bit stream is not a multiple of 8, add padding to the text.
7. Store the padding information (in 8 bits) at the start of the encoded bit stream.
8. Write the result to an output binary file.

### Decompression
1. Read the binary file.
2. Extract and remove the padding information.
3. Decode the bits by reading them and replacing valid Huffman code bits with their corresponding character values.
4. Save the decoded data into the output file.

## Installation
To be added later. Please ensure you have Python installed, as ByteZip is built using Python.

## Usage
To be added later. Once installed, you can use the command line to compress or decompress files. Example commands will be provided.

## Contact
For any questions or suggestions, please contact us at [vijaysb2006@gmail.com](mailto:vijaysb2006@gmail.com). You can also reach out to us on GitHub at [[Kiran Rajeev](https://github.com/KiranRajeev-KV)] and [[Vijay S B](https://github.com/vijaysb0613)].
