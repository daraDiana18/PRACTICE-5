s=str(input('Enter a string'))
count=0
for i in s:
    if i== 'a':
        s.replace('a', '')
        count += 1

print('another text',s.replace('a',''))

print('removed characters',count)

