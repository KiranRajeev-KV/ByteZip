# Finding Frequency From Text:
def Frequency(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1

        else:
            frequency[char] = 1
        
    return frequency
 

# Reading Files
def ReadFiles(FilePath):
    with open(FilePath,'r') as file:
        lines=file.readlines()
    return lines



FilePath="E:\ByteZipProj\ByteZip\compression\SampleText.txt"
lines = ReadFiles(FilePath)


data = "".join(lines)
frequencies = Frequency(data)
print(frequencies)