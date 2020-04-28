fname = input("Enter a file name:\n")

fhandle = open(fname)
collection = dict()
count = 1

for line in fhandle:
    words = line.split()
    for word in words:
        if word not in collection:
            collection[word] = count
            count = count + 1

print(collection)

check = input("Choose a word from the dictionary:\n")
if check in collection:
    print(collection[check])
else:
    print("Enter a valid word")
