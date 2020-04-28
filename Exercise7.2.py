#Input file name
fname = input("Enter a file name: ")

#Try to open handle
try:
    fh = open(fname)
except:
    print("File cannot be opened:",fname)

#Start count and spam total at zero
count = 0
spam = 0

for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1 #Add one to count
        cindex = line.find(':') #Locate colon index
        decimal = line[cindex+2:] #pull out decimal position
        fldec = float(decimal) #Convert decimal string to float
        spam = spam + fldec #Add to running total of spam

average = spam/count #Calculate average
print("Average spam confidence:",average)
