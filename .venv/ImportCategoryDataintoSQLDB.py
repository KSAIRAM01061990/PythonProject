import pandas as pd
import pyodbc
import sqlalchemy as sa

# print(pyodbc.drivers())

servername='EPINHYDW015E'
databasename='DEMO'
tablename='CATEGORY3'

df1=pd.read_excel('C:\\Users\\Sairam_Kanamarlapudi\\Desktop\\Python\\CategoryData.xlsx')
engine=sa.create_engine(f'mssql+pyodbc://{servername}/{databasename}?driver=SQL+Server+Native+Client+11.0')
df1['fullname']=df1['firstname']+df1['lastname']
# print(engine)
# print(df1)
pivot_data=df1.pivot_table(index='Category',columns='Year',values='Amount')
# print(pivot_data)
print(pivot_data.rename_axis(columns=None).reset_index())
pivot_data.to_sql(tablename,engine,if_exists='append',index=False)

# data = {
#          'name' : ['sai','ram','kumar'],
#          'age'  : [20,30,40]
#         }
#
# df=pd.DataFrame(data)
# print(df)

