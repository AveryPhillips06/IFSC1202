fileToRead="06.04 EmptyLinesInput.txt"
fileToWrite="06.04 EmptyLinesOutput.txt"
fout=open(fileToWrite,"w")
readCount=0
writeCount=0
with open(fileToRead,"r") as f:
    for line in f:
        readCount+=1
        if line.strip():
            writeCount+=1
            fout.write(line)
fout.close()
print(readCount,'records read')
print(writeCount,'records written')