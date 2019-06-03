import re
import sample as s


fileHandle = open ( 'file.txt',"r" )
lineList = fileHandle.readlines()
fileHandle.close()
k=lineList[-1]
#print (k)

#aa=re.findall(r'"\s*([^"]*?)\s*"', k)
'''aa=re.findall(r'\[(.*)\]', k)
print aa
bb=re.findall(r'\[(.*)\]', aa)
print bb'''


s="['a','b'], ['c','d'], ['e','f']"

t=(s.split(" "))

m=[]

for i in t:

	i=i.strip(",")

	i=i.strip("[")

	i=i.strip("]")

	i=i.strip(",")

	m.append(i.split(","))

print(m) 