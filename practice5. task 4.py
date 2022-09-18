s=str(input('Enter a string'))
count=0
for i in s:
    if i== 'a':
        s.replace('a', 'o')
        count += 1

print('another text',s.replace('a','o'))

print('number of replacements',count)

print('characters of the string',len(s))
