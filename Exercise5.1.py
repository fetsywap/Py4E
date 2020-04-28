count = 0
total = 0
while True:
    entry = input('Input a number:\n')
    if entry == "Done":
        break
    if entry == 'done':
        break
    try:
        num = float(entry)
        count = count + 1
        total = total + num
        continue
    except:
        print('Please enter a number')
        continue
average = total / count
print('Total is:',total ,'Count is:',count ,'Average is:',average)
