l2=[['final', 'A', 'B', 'C'], ['A', 'a', 'b'], ['a', 'aa', 'bb'], ['aa', 'o', 'p'], ['p', 'hi', 'h'], ['h', 'hey'], ['bb', '5', '10'], 
['b', 'x'], ['B', 'c', 'd'], ['C', 'a', 'e'], ['a', 'aa', 'bb'], ['aa', 'o', 'p'], ['p', 'hi', 'h'], ['h', 'hey'], ['bb', '5', '10']]


j=0
c=1
r=1
tables_in_celllist=[]
for table in cell_list:
	tables_in_celllist.append(table[0])
	
for i in range(len(l2)):
	if i==0:
		#col_id(l2[0][0],clm_list,1,1)
	elif i==1 and l2[i][0] not in tables_in_celllist[]:
		case_2(i)
	elif i>1 and l2[i][0] in tables_in_celllist[]:
		j=j+1
		check_condition(i,j)
	elif i>1 and l2[i][0] not in tables_in_celllist[]:
		search_index(i,j)


def search_index(i,j):
	index_key=l2[i][0]
	for k in range(len(i)):
		if index_key in l2[k]:
			search_index=l2[k].index(index_key)
			ref_key=l2[k][search_index-1]
	case_5(i,j,ref_key)
	
def case_5(i,j,ref_key):
	for table_id in range(len(tables_in_celllist)):
		if ref_key==tables_in_celllist[table_id]:
			c=cell_list[table_id][3]
			r=cell_list[len(cell_list)-1][4]+2
			col_id(l2[i][j],clm_list,c,r)
			j=j+1
			check_condition(i,j)

def case_2(i,j):
	if cell_list[i-1][0]==l2[i-1][0]:
		c=cell_list[0][3]+2
		r=1
		col_id(l2[i][j]),clm_list,c,r)
		j=j+1
		check_condition(i,j)
	
	else:
		c=cell_list[len(cell_list)-1][3]+2 
		check_condition(i,j)
	
'''def case_4(i,j):
	for i in range(len(tables_in_celllist)):
		if tables_in_celllist[i]==l2[i][0]:
			c=cell_list[i][3]+2'''

def case_4(i,j):
	c=cell_list[i][3]
	r=cell_list[i][4]+2
	col_id(l2[i][j],clm_list,c,r)
	check_condition(i,j)
	
def case_3(i,j,ic,ir):
	c=cell_list[i][3]+ic
	r=r+ir
	col_id(l2[i][j],clm_list,c,r)
	
			
def check_condition(i,j):
	if l2[i+1][0]==l2[i][j] and j==1:
		ic=2
		ir=0
		case_3(i,j,ic,ir)
	'''elif l2[i+1][0]==l2[i][j+1]:
		ic=0
		ir=2
		case_3(i,j,ic+2,ir-2)'''
	elif l2[i+1][0]!=l2[i][j] and j==1 :
		ic=2
		ir=0
		case_3(i,j,ic,ir)
		while j+1<=len(l2[i]-1):
			j+=1
			check_condition(i,j)
			
	elif l2[i+1][0]==l2[i][j] and j>1:
		ic=0
		ir=2
		c=cell_list[len(cell_list)-1][3]+ic
		r=cell_list[len(cell_list)-1][4]+ir
		col_id(l2[i][j],clm_list,c,r)
		
	elif l2[i+1][0]!=l2[i][j] and j>1:
		ic=0
		ir=2
		c=cell_list[len(cell_list)-1][3]+ic
		r=cell_list[len(cell_list)-1][4]+ir
		col_id(l2[i][j],clm_list,c,r)
		while j+1<=len(l2[i]-1):
			j+=1
			check_condition(i,j)
			
			
		
		'''while j<=len(l2[i]-1) and (l2[i][j]!=l2[i+1][0]):
			
			ir=2
			ic=0
			case_3(i,j,ic,ir)
			j=j+1
			check_condition(i,j)'''
		
		
		
	'''elif l2[i+1][0]!=l2[i][j] and len(l2[i])>2:
		j=j+1
		ic=2
		ir=0
		check_condition(i,j)'''
		
		#case_3(i+1,j,ic,ir)