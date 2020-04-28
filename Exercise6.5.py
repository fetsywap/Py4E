str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
decimal = str[colon+1:]
number = float(decimal)
print(number)
