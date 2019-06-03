
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


l=[]
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
	init_val=dic[root][:]		#creating a copy of the list
	init_val.insert(0,root)
	#print init_val
	l.append(root)
	l.append(init_val)
	dependant(dic[root])
	
	return root

		
def dependant(x):
	for key in x:
		if key in dic.keys():
			k=dic[key][:]		#creating a copy of list
			l.append(k)
			l[len(l)-1].insert(0,key)
			dependant(dic[key])			#calling a recursive function to create a dependant list
		
root(dic)
print l