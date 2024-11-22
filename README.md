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

To use ByteZip, follow these steps:

### 1. Ensure Python is Installed
Ensure that you have Python 3.x or later installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### 2. Clone the Repository
You can clone the repository to your local machine using Git. Open a terminal (Command Prompt, PowerShell, or terminal of your choice) and run:
```bash
git clone https://github.com/yourusername/ByteZip.git
```
Alternatively, download the ZIP of the project from GitHub and extract it.

### 3.  Install Required Dependencies
If you're using Python 3, tkinter (for the graphical interface) is typically included by default. If you don’t have it installed, you can install it manually:

- For Windows:
Tkinter should be included by default. If not, you may need to install it via your Python installation options.
- For Mac/Linux: You can install tkinter using the following:
```bash
sudo apt-get install python3-tk
```
### 4. Run the Application
Once the setup is complete, run the application with the following command:
```bash
python ui.py
```
## Usage
Once ByteZip is installed and running, you can use the graphical interface to compress and decompress text files.

### Compressing a File:
1. Launch the application by running ui.py.
2. Click the "Compress File" button.
3. Select a text file (.txt) from your computer.
4. The application will compress the file using Huffman coding and save the compressed file with a .bin extension.
5. A success message will appear once the compression is complete.

### Decompressing a File:
1. Launch the application by running ui.py.
2. Click the "Decompress File" button.
3. Select a compressed file (.bin) to decompress.
4. The application will restore the original text file and save it as a .txt file with the suffix _decompressed.
5. A success message will appear once the decompression is complete.

### Error Handling:
If an error occurs during the compression or decompression process, an error message will pop up to help you troubleshoot the issue.

## Contact
For any questions or suggestions, please contact us at [vijaysb2006@gmail.com](mailto:vijaysb2006@gmail.com). You can also reach out to us on GitHub at [[Kiran Rajeev](https://github.com/KiranRajeev-KV)] and [[Vijay S B](https://github.com/vijaysb0613)].
