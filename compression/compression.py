import json
import os
import heapq

class HeapNode():
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None

    def __lt__(self,other):  
        return self.freq<other.freq

    def __eq__(self, other):
        return self.freq == other.freq
    
    def to_dict(self):
        return {
            'char': self.char,
            'freq': self.freq,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None,
        }

class Compress():
    def __init__(self,FilePath):
        self.FilePath=FilePath
        self.Heap=[]
        self.codes={}
    #Finding Frequency
    def Frequency(self,text):
        frequency = {}
        for char in text:
            if char in frequency:
                frequency[char] += 1

            else:
                frequency[char] = 1
            
        return frequency
    
    # Reading Files
    def ReadFiles(self):
        FileName,FileExtension = os.path.splitext(self.FilePath)                 # -> To Get File Name and Extension Type

        with open(self.FilePath,'r') as file:
            lines=file.read()
        return lines
    
    # Writing Binary File
    def WriteFiles(self,text):
        FileName,FileExtension = os.path.splitext(self.FilePath)                 # -> To Get File Name and Extension Type
        OutputFile = FileName + ".bin"

        with open(OutputFile,'wb') as output_file:
            output_file.write(text)
        
    # Creating a MinHeap Priority Heap 
    def CreateMinHeap(self,frequency):

        for char in frequency:
            node=HeapNode(char,frequency[char])
            heapq.heappush(self.Heap,node)

    
    def CombineTwoNode(self):
        while(len(self.Heap)>1):
            node1=heapq.heappop(self.Heap)
            node2=heapq.heappop(self.Heap)
            MergedNode=HeapNode(None,node1.freq+node2.freq)
            MergedNode.left=node1
            MergedNode.right=node2
            
            heapq.heappush(self.Heap,MergedNode)

    def Traversal(self,root,CurrentCode):
        if root is None:
            return
        if (root.char != None ):
            self.codes[root.char]= CurrentCode

        self.Traversal(root.left,CurrentCode+"0")
        self.Traversal(root.right,CurrentCode+"1")
    
    # create unique code for each characters
    def MakeCode(self):
        if not self.Heap:
            raise ValueError("Heap is empty, cannot generate Huffman codes.")
        
        root = heapq.heappop(self.Heap)
        self.save_trees(root)
        CurrentCode = ""
        self.Traversal(root, CurrentCode)  
    
    def CreateEncrytpedText(self,text):
        EncodedString=""
        for char in text:
            EncodedString += (self.codes[char])
        return EncodedString
    
    # Adding extra padding to make its length divisible by 8 
    def AddPadingText(self,text):
        ExtraPadding = 8 - len(text) % 8
        for i in range(ExtraPadding):
            text += "0"
             
        PaddedInfo = "{:08b}".format(ExtraPadding)

        text=PaddedInfo+text
        return text
        
    # Convert to A byte Array    
    def ConvertToByte(self,text):
        b=bytearray()
        for i in range(0,len(text),8):
            byte=text[i:i+8]
            b.append(int(byte,2))
        return b


    def Compression(self):
        FileLines=self.ReadFiles()
        Frequency=self.Frequency(FileLines)
        
        self.CreateMinHeap(Frequency)
        self.CombineTwoNode()
        self.MakeCode()
        EncodedString=self.CreateEncrytpedText(FileLines)
        PaddedEncodedString=self.AddPadingText(EncodedString)
        ByteEncodedString=self.ConvertToByte(PaddedEncodedString)
        
        self.WriteFiles(ByteEncodedString)

    def save_trees(self, root, directory='huffman_trees'):
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(os.path.join(directory, 'huffman_tree.json'), 'w') as f:
                json.dump(root.to_dict(), f)
