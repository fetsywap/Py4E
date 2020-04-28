fhand = open("romeo.txt")

x = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in x:
            x.append(word)

x.sort()
print(x)
