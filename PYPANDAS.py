import pandas as pd
df = pd.DataFrame({'TABLENAME': ["COL1", "COL2", "COL3","COL4", "COL5"]})
writer = pd.ExcelWriter("C:\Users\LOHITH\Desktop\New folder\sample111.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
