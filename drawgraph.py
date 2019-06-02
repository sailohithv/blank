import xlsxwriter
workbook = xlsxwriter.Workbook("C:\Users\LOHITH\Desktop\New folder\list.xlsx")
worksheet = workbook.add_worksheet()

cellist = [['final', 1, 1, 1, 14],
            ['A', 3, 1, 3, 11], ['a', 5, 1, 5, 11], ['aa', 7, 1, 7, 11], ['o', 9, 1, 9, 6],
           ['p', 9, 8, 9, 15], ['hi', 11, 8, 11, 13], ['h', 11, 15, 11, 20], ['hey', 13, 15, 13, 20],
           ['bb', 7, 22, 7, 28], ['k', 9, 22, 9, 27], ['l', 9, 29, 9, 34], ['b', 5, 36, 5, 41],
           ['x', 7, 36, 7, 41], ['B', 3, 43, 3, 48], ['c', 5, 43, 5, 48], ['d', 5, 50, 5, 55],
           ['C', 3, 57, 3, 62], ['a', 5, 57, 5, 67], ['aa', 7, 57, 7, 67], ['o', 9, 57, 9, 62],
           ['p', 9, 64, 9, 71], ['hi', 11, 64, 11, 69], ['h', 11, 71, 11, 76], ['hey', 13, 71, 13, 76],
           ['bb', 7, 78, 7, 84], ['k', 9, 78, 9, 83], ['l', 9, 85, 9, 90]]



columnlist=[["C","C1","C2"],["e","e1","e2"],["r","r1","r2"],["d","d1","d2"],
                ["c","c1","c2"],["B","B1","B2"],["x","x1","x2"],["b","b1","b2"],['r','r1','r2'],["bb","bb1","bb2","bb3"],
                ["k","k1","k2"],["l","l1","l2"],["final","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10"],["A","A1","A2","A3","A4","A5","A6","A7"],
                ["a","a1","a2","a3","a4","a5","a6","a7"],["aa","aa1","aa2","aa3","aa4","aa5","aa6","aa7"],["o","O1","O2"],
                ["p","P1","P2","P3","P4"],["hi","hi1","hi2"],["h","h1","h2"],["hey","hey1","hey2"]]


format2 = workbook.add_format({'border': 2})


for i in range(0, len(cellist)):
    sc = cellist[i][1]
    sr = cellist[i][2]
    for j in range(0,len(columnlist)):
      if columnlist[j][0]==cellist[i][0]:
          for k in range(0,len(columnlist[j])):
              value=columnlist[j][k]
              worksheet.write(sr,sc,value,format2)
              sr+=1
workbook.close()