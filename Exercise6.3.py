def lettercount(inp):
    count = 0
    for letter in inp:
        if letter == 'a':
            count = count + 1
    print('Count is:',count)

word = input('Input a word:\n')
selection = input('Pick a letter to count:\n')
if selection in word:
     lettercount(word)
else:
    print('Select a letter in the word chosen')
