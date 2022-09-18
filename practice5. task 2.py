
s=str(input('Enter a string'))
count=0
for i in s:
    if i== ':':
        s.replace(':', '%')
        count += 1

print('another text',s.replace(':','%'))

print(count)
    
