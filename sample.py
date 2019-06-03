dic={'final':['A','B','C'],
	 'A':['a','b'],
	 'B':['c','d'],
	 'a':['aa','bb'],
	 'C':['a','e'],
	 'aa':['o','p'],
	 'p':['hi','h'],
	 'bb':['5','10'],
	 'h':['hey'],
	 'b':['x']
	 
}

#root(dic) function is to find the primary target table in the dictionary

def root(dic):	
	keys=dic.keys()
	values=dic.values()
	new_list=[]
	for i in values:			
		new_list+=i				#forming a single list that holds all the values in the dictionary
	#print keys,values
	for key in keys:
		if key not in new_list:
			root=key
	#print dic[root]
	dependant(dic[root])
	
	return root

l=[]		
def dependant(x):
	sep_dic={}
	for key in x:
		if key in dic.keys():
			k=dic[key]
			#print k
			
			l.append(k)
			print l
			s=str(l)
			f = open("file.txt", "a")
			f.write(s+'\n')
			f.close()
			#sep_dic[key]=k
			dependant(dic[key])				#calling a recursive function to create a dependant list
									
	#print sep_dic	
	
		
root(dic)
