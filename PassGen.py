word = input('Enter a word or phrase:')
password = ''

for i in range(len(word)):
    if word[i] == 'i':
        password += '!'
        
    elif word[i] == 'a':
        password += '@'
        
    elif word[i] == 'm':
        password += 'M'
        
    elif word[i] == 'B':
        password += '8'
        
    elif word[i] == 'o':
        password += '.'
        
    elif word[i] == 'S':
        password += '$'
        
    elif word[i] == 'e':
        password += '3'
        
    else:
        password += word[i]
        
if len(password) <= 4:
    password += 'q*s00'

print(password)
