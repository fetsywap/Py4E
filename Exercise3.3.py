inp1 = input('Enter score:\n ')
try:
    score = float(inp1)
    if score > 1.0:
        print('Bad score')
    elif score >= 0.9 and score <= 1.0:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
except:
    print('Bad score')
