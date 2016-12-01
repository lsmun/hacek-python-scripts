## Open the file with read only permit
f = open('file.txt', "r")
file = open("newfile.csv", "w")

## Read the first line 
line = f.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    #print line
    data = line.split(' ',3)
    for n in data:
        if '\n' not in n:
            file.write(n + ',')
        else:
            file.write(n)
    line = f.readline()

f.close()