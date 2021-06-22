
def removespaces(str): #function to remove spaces
    return "".join([x for x in str if x != ' ']) 
def storageConversion():
    powers = {'B':10**0,'KB':10**3,'MB':10**6,'GB':10**9,'TB':10**12,'KiB':2**10,'MiB':2**20,'GiB':2**30,'TiB':2**40} #creates a dictionary of units and powers
    while True:
        userinput = removespaces(input('Storage volume: ')) #removes spaces from input
        unit = "".join([x for x in userinput[-3:] if x.isalpha()]) #gets the last three characters in input that could be the unit
        coefficient = "".join(userinput[0:0-len(unit)]) #gets the remaining digits from the userinput excluding the potential unit that was removed in prev. line
        if True in [True for x in coefficient if x.isalpha()]: #checks if a alphabet is in the coefficient (shouldn't happen) like 5b5B
            unit = 'error' #guarantees error in next check
        else:
            coefficient = float(coefficient) #makes the coefficient a float
            
        if unit in powers: #if the unit provided is in the dictionary
            bytes = coefficient*powers.get(unit) #bytes becomes the number of bytes in the userinput
            break
    while True:
        newunit = removespaces(input('New unit: ')) #removes spaces from input
        if newunit in powers: #if the unit provided is in the dictionary
            print(f"{round(bytes/powers.get(newunit),2)}{newunit}") #converts bytes into the new unit and prints it with the new unit
            break

storageConversion()

