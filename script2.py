## Open the file with read only permit
f = open('newfile.csv', "r")
file = open("newfile2.csv", "w")

## Read the first line 
line = f.readline()

listA = []

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    #print line
    data = line.split(',')
    listA.append(data[2])
    print(data[2]);
    line = f.readline()

setA = set(listA)

for a in setA:
    file.write(a + '\n')
    

f.close()