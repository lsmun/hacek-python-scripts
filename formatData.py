##### FILES #####

# Open files
originalData = open('newfile.csv', "r")
uniqueIP = open('newfile2.csv', "r")
formattedData = open("formattedData2.csv", "w")

# Read the first line 
ipAddress = uniqueIP.readline().rstrip()
line = originalData.readline()



##### FUNCTIONS #####

# Calculate time between stages
def calculateTime(currentTimeStamp):
    # Convert time in milliseconds
    currentTimeSplit = [float(n) for n in currentTimeStamp.split(':')]
    currentTimeSeconds = currentTimeSplit[0] * 3600 + currentTimeSplit[1] * 60 + currentTimeSplit[2]
        
    # Check to see if time is T0 or not
    ## Case where it is NOT T0
    if timeStamp != []:
        # Since this is not T0, previousTimeSeconds will be the last timeStamp
        previousTimeStamp = timeStamp[len(timeStamp)-1]
        
        # Convert timeStamp into milliseconds
        previousTimeSplit = [float(n) for n in previousTimeStamp.split(':')]
        previousTimeSeconds = previousTimeSplit[0] * 3600 + previousTimeSplit[1] * 60 + previousTimeSplit[2]
        
        # Calculate the difference between the timeStamp
        time = currentTimeSeconds - previousTimeSeconds

    ## Case where it is T0
    else:
        # Convert time server started in milliseconds
        startTimeSeconds = 11 * 3600 + 39 * 60 + 15.119628
        
        # Since this is T0, previousTimeSeconds will be the server start time
        previousTimeSeconds = startTimeSeconds
        
        # Update T0
        global t0
        t0 = currentTimeSeconds - previousTimeSeconds
        
        # Update currentTimeSeconds and time to 0 to indicate the first log entry
        currentTimeSeconds = 0
        time = 0

    # Add currentTimeStamp to the list
    timeStamp.append(currentTimeStamp)
    
    # Return result as a float
    return float("%.6f" % time)



##### MAIN #####

# Main
while ipAddress:
    # Initialize variables for each IP address
    timeStamp = [] # list of time stamps of relevant log entries
    stageTimeSum = [-1,-1,-1,-1,-1] # sum of time stamps for each stage
    ipAddressSplit = ipAddress.split('.') # split IP address to obtain the first number
    t0 = 0 # time difference from server start and first log entry

    # Cycle through each entry of the log
    while line:
        # Initialize variables for each log entry
        stage = -1 # what predetermined stage current log entry is on
        
        # Split the log entry
        data = line.split(',')
        
        # Check to see if the log entry matches the current ipAddress
        if data[2] == ipAddress:
        
            # Check to see if the log entry is a specified stage
            if 'root: Home page displayed.' in data[3]:
                stage = 0
            elif 'root: Captcha page displayed.' in data[3]:
                stage = 1
            elif 'hold: Captcha valid. Query: fall=Back' in data[3]:
                stage = 2
            elif 'get_hold' in data[3]:
                stage = 3
            elif 'sale: Redirect to confirm page' in data[3]:
                stage = 4
            
            # Check if the current log entry is on a valid state
            if stage != -1:
                # Calculate the time between current and previous log entry
                timeTemp = calculateTime(data[1])
                
                # Check to see if the current log entry is T0
                ## Case if current log entry is T0
                if timeTemp == 0:
                    stageTimeSum[stage] = timeTemp
                
                ## Case if current log entry is NOT T0
                else:
                    # Check to see if this is the first log entry of this particular stage
                    if stageTimeSum[stage] == -1:
                        # Since this is the first log entry for this particular stage, initialize to 0 so all subsequent entries can be summed up
                        stageTimeSum[stage] = 0
                    stageTimeSum[stage] += timeTemp
         
        # Read the next log entry
        line = originalData.readline()
    
    # Write the information for each stage of current IP
    for i in range(5):
        # Skip if stageTimeSum is -1 for stage i because stage i was never logged 
        if stageTimeSum[i] != -1:
            # FIRST IP ADDRESS NUM, TOTAL TIME ON STAGE, STAGE NUM, IP ADDRESS, T0
            formattedData.write(ipAddressSplit[0] + ',' + str(stageTimeSum[i]) + ',' + str(i) + ',' + ipAddress + ',' + str(t0) + ';\n')
    
    # Read next IP address
    ipAddress = uniqueIP.readline().rstrip()
    
    # Reread server log entries
    originalData.seek(0)
    line = originalData.readline()

    
    
##### FILES #####

# Close files
originalData.close()
uniqueIP.close()