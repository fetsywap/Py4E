finput = input("Enter a file name:\n")
if len(finput) < 1 :finput = "mbox-short.txt"

try:
    fhandle = open(finput)
except:
    print("File cannot be opened")

counts = dict()
for line in fhandle:
    if line.startswith("From "):
        day = line.split()[2]
        if day not in counts:
            counts[day] = 1
        else:
            counts[day] += 1

print(counts)
