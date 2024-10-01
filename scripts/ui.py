import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from compression.compression import Compress
from decompression.decompression import decompress

class CompressionApp:
    def __init__(self, master):
        self.master = master
        master.title("Text File Compression and Decompression")

        self.label = tk.Label(master, text="Select a text file to compress or decompress:")
        self.label.pack(pady=10)

        self.compress_button = tk.Button(master, text="Compress File", command=self.compress_file)
        self.compress_button.pack(pady=5)

        self.decompress_button = tk.Button(master, text="Decompress File", command=self.decompress_file)
        self.decompress_button.pack(pady=5)

    def compress_file(self):
        file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                compressor = Compress(file_path)
                compressor.Compression()
                messagebox.showinfo("Success", f"File compressed successfully: {os.path.splitext(file_path)[0]}.bin")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def decompress_file(self):
        file_path = filedialog.askopenfilename(title="Select a Compressed File", filetypes=[("Binary Files", "*.bin")])
        if file_path:
            try:
                output_file = decompress(file_path)
                messagebox.showinfo("Success", f"File decompressed successfully: {output_file}")
            except Exception as e:
                messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CompressionApp(root)
    root.mainloop()
