## Openn files
originalData = open('newfile.csv', "r")
uniqueIP = open('newfile2.csv', "r")
formattedData = open("formattedData.csv", "w")

## Read the first line 
ipAddress = uniqueIP.readline().rstrip()
line = originalData.readline()

## Calculate time between stages

def calculateTime(currentTimeStamp):
    time = 0
    
    # Check to see if this is the first step or not
    if timeStamp != []:
        previousTimeStamp = timeStamp[len(timeStamp)-1]
        
        # Convert everything into seconds
        previousTimeSplit = [float(n) for n in previousTimeStamp.split(':')]
        currentTimeSplit = [float(n) for n in currentTimeStamp.split(':')]
        
        previousTimeSeconds = previousTimeSplit[0] * 3600 + previousTimeSplit[1] * 60 + previousTimeSplit[2]
        currentTimeSeconds = currentTimeSplit[0] * 3600 + currentTimeSplit[1] * 60 + currentTimeSplit[2]
        
        time = currentTimeSeconds - previousTimeSeconds
        
    timeStamp.append(currentTimeStamp)
    return str("%.6f" % time)



uniqueID = 0;

while ipAddress:
    timeStamp = []
    stage = -1
    ipAddressSplit = ipAddress.split('.')

    while line:
        data = line.split(',')
        
        if data[2] == ipAddress:
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
            if stage != -1:
                formattedData.write(str(uniqueID) + ',' + ipAddressSplit[0] + ',' + calculateTime(data[1]) + ',' + str(stage) + ',' + ipAddress + ';\n')
        stage = -1
        line = originalData.readline()
        
    uniqueID += 1
    ipAddress = uniqueIP.readline().rstrip()
    originalData.seek(0)
    line = originalData.readline()

originalData.close()
uniqueIP.close()