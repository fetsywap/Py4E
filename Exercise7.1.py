fhand = open('mbox-short.txt')
print(fhand)

for lines in fhand:
    caps = lines.rstrip()
    print(caps.upper())
