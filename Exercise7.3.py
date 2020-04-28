fname = input("Enter a file name: ")

#check the name of the file for Easter egg
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
#if real file name then run program
else:
    try:
        fh = open(fname)
    except:
        print("File cannot be opened:",fname)

    count = 0
    spam = 0

    for line in fh:
        if line.startswith('X-DSPAM-Confidence:'):
            count = count + 1
            cindex = line.find(':')
            decimal = line[cindex+2:]
            fldec = float(decimal)
            spam = spam + fldec

    average = spam/count
    print("Average spam confidence:",average)
