dic={'final':['A','B','C'],
	 'A':['a','b'],
	 'a':['aa','bb'],
	 'B':['c','d'],
	 'C':['a','e'],
	 'aa':[4,89]
}
def leve(dic):
	root = ''
	k=dic.keys()
	l=dic.values()
	for i in k :
		for j in l  :
			if i  not in j:
				root =i
	print(dic[root])
	findleve(dic[root])
	return root
def findleve(x):
	for i in x :
		print(dic[i])
		for i in dic[i]:
			if i in dic.keys() :
				#print(" -- ",i)
				print(dic[i])
				for i in dic[i] :
					if i in dic.keys():
						print(i)
						findleve(dic[i])
				
	
print(leve(dic))