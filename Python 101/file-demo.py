f = open('top-100.txt')
'''for line in f:
 print(line.strip())'''

f.close()
f = open('top-100.txt','a')

f.write('\nadding last line')
f.close()
'''f = open('top-100.txt','r')

for line in f:
 print(line.strip())

f.close()'''
with open('top-100.txt') as f:
 for line in f:
  print(line.strip())