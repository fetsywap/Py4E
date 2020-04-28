maximum = None
minimum = None
while True:
    inp = input('Enter a number:\n')
    if inp == 'done':
        break
    if inp == 'Done':
        break
    try:
        number = float(inp)
        if maximum is None:
            maximum = number
        elif number > maximum:
            maximum = number
        if minimum is None:
            minimum = number
        elif number < minimum:
            minimum = number
    except:
        print('Enter a number')
print('Maximum is:',maximum)
print('Minimum is:',minimum)
