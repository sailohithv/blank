l2=[['final', 'A', 'B', 'C'], ['A', 'a', 'b'], ['a', 'aa', 'bb'], ['aa', 'o','p'], ['p', 'hi', 'h'], ['h', 'hey'], ['bb', '5', '10'], 
['b', 'x'], ['B', 'c', 'd'], ['C', 'a'], ['a', 'aa', 'bb'], ['aa', 'o', 'p'], ['p', 'hi', 'h'], ['h', 'hey'], ['bb', '5', '10']]

main_list=[]
j=0
c=1
r=1

tables_in_celllist=[]

col=[['r','r1','r2'],["final","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10"],["A","A1","A2","A3","A4","A5","A6","A7"],["a","a1","a2","a3","a4","a5","a6","a7"],["aa","aa1","aa2","aa3","aa4","aa5","aa6","aa7"],["o","O1","O2"],["p","P1","P2","P3","P4"],["hi","hi1","hi2"],["h","h1","h2"],["hey","hey1","hey2"]]

def col_id(intv, cc, cr):
  
  li=[]
  li.append(intv)
  li.append(cc)
  li.append(cr)
  for i in range(len(col)):
    if col[i][0]==intv:
      no_of_rows=len(col[i])
      er=cr+no_of_rows+2
      ec=cc
      li.append(ec)
      li.append(er)
  main_list.append(li)
  #print main_list

def search_index(i,j):
	var=0
	index_key=l2[i][0]
	for k in range(len(l2)):
		if index_key in l2[k]:
			var=k
			search_index=l2[k].index(index_key)
			
			ref_key=l2[k][search_index-1]
			break
	case_5(i,j,ref_key,k)
	
def case_5(i,j,ref_key,var):
	if ref_key in tables_in_celllist:
		for table_id in range(len(tables_in_celllist)):
			if ref_key==tables_in_celllist[table_id]:
				c=main_list[table_id][3]
				
				r=main_list[len(main_list)-1][4]+2
				col_id(l2[i][j],c,r)
				j=j+1
				check_condition(i,j)
	else:
		search_index=l2[var].index(ref_key)
		search_index=search_index-1
		ref_key=l2[var][search_index]
		case_5(i,j,ref_key,var)

def case_2(i,j):
	if main_list[i-1][0]==l2[i-1][0]:
		c=main_list[0][3]+2
		
		col_id(l2[i][j],c,r)
		j=j+1
		check_condition(i,j)
		
	
	else:
		c=main_list[len(main_list)-1][3]+2 
		check_condition(i,j)

def case_4(i,j):
	c=main_list[i][3]
	
	r=main_list[i][4]+2
	col_id(l2[i][j],c,r)
	check_condition(i,j)
	
def case_3(i,j,ic,ir):
	r=1
	r=r+ir
	c=main_list[i][3]+ic
	col_id(l2[i][j],c,r)

def case_6(i,j,ic,ir):
	r=main_list[len(main_list)-1][2]
	r=r+ir
	c=main_list[len(main_list)-1][3]+ic
	print 'stark'
	print c
	col_id(l2[i][j],c,r)
			
def check_condition(i,j):
	print 'hulk'
	print i,j
	if l2[i+1][0]==l2[i][j] and j==1:
		ic=2
		ir=0
		case_3(i,j,ic,ir)
		
		
	elif l2[i+1][0]!=l2[i][j] and j==1 :
		ic=2
		ir=0
		case_6(i,j,ic,ir)
		while j+1<=len(l2[i])-1:
			j+=1
			check_condition(i,j)
			
	elif l2[i+1][0]==l2[i][j] and j>1:
		ic=0
		ir=2
		c=main_list[len(main_list)-1][3]+ic
		r=main_list[len(main_list)-1][4]+ir
		col_id(l2[i][j],c,r)
		
	elif l2[i+1][0]!=l2[i][j] and j>1:
		ic=0
		ir=2
		c=main_list[len(main_list)-1][3]+ic
		r=main_list[len(main_list)-1][4]+ir
		col_id(l2[i][j],c,r)
		while j+1<=len(l2[i]-1):
			j+=1
			check_condition(i,j)

def table_list():	
	print main_list
	for table in main_list:
		tables_in_celllist.append(table[0])
	return tables_in_celllist

for i in range(len(l2)):
	t_celllist=table_list()
	
	if i==0:
		col_id(l2[0][0],1,1)
	elif i==1 and l2[i][j] not in t_celllist:
		case_2(i,j)
	elif (i>1) and (l2[i][0] in t_celllist):
		j=0
		j=j+1
		
		check_condition(i,j)
	elif i>1 and l2[i][0] not in t_celllist:
		search_index(i,j)
	
print main_list







	
