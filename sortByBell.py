##### FILES #####

# Open files
f = open('formattedData2.csv', "r")
output = open('sortedData2.csv', "w")

# Read the first line 
l = f.readline().strip()



##### MAIN #####

# Global variables
sortedList = [] # sorted in descending order by stage 1's value
tempList = [] # temporary list used to group logs by IP

# Main
## First group the data by IP addresses and add to sortedList
while l:
    # Split the data
    s = l[:-1].split(',')

    # Check to see if tempList is empty
    if tempList == []:
       tempList.append(s)
    # If not empty, check to see if IP matches the IP in tempList
    else:
        # Add to tempList if IP matches
        if tempList[len(tempList)-1][3] == s[3]:
            tempList.append(s)
        
        # Else add tempList to sortedList and reinitialize tempList with current data
        else:
            # Intialize stage1 to -1 to indicate no such values were found
            stage1 = -1
            
            # Find value of stage1 and record it
            for logEntry in tempList:
                if logEntry[2] == '1':
                    stage1 = float(logEntry[1])
                    
            # Insert stage1 to front of tempList
            tempList.insert(0,stage1)
            
            # Append tempList to sortedList since this concludes current group
            sortedList.append(tempList)
            
            # Reinitialize tempList and start new group
            tempList = []
            tempList.append(s)
            
    # Read next data
    l = f.readline().strip()

## Sort sortedList in descending order
#sorted(sortedList, key=lambda x: x[0])

def insertionsort(arr):
    N = len(arr)
    for i in range(1, N):
        j = i - 1
        temp = arr[i]
        tempCounter = arr[i][0]
        while j >= 0 and tempCounter < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
                
    
insertionsort(sortedList)

def bellsort(arr):
    N = len(arr)
    removeArray = arr
    tempArray = []
    tempArray.append(removeArray[0])
    del removeArray[0]
    
    for i in range(2, N/2):
        tempArray.append(removeArray[i])
        del removeArray[i]
    
    removeArray = removeArray[::-1]
    
    return tempArray + removeArray
    
sortedList = bellsort(sortedList)
    
uniqueID = 0

for group in sortedList:
    group = group[1:]
    for line in group:
        for i in range(len(line)):
            output.write(str(uniqueID) + ',' + str(line[i]) + ",")
        output.write(str(uniqueID) + ',' + str(line[len(line)-1]) +";\n")
    uniqueID += 1
##### FILES #####

# Close files
f.close()
output.close()