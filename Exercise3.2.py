inp1 = input('How many hours did you work?\n')
inp2 = input('What is your pay rate?\n')
try:
    hours = float(inp1)
    rate = float(inp2)
    if hours <= 40:
        pay = hours * rate
        print(pay)
    else:
        pay = 40 * rate + ((hours - 40) * (rate * 1.5))
        print(pay)
except:
    print('Error, enter numeric input')
