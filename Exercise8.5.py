fname = input("Input a file name:\n")
fhandle = open(fname)

count = 0

for line in fhandle:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
