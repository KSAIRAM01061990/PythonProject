import pandas as pd
import pyodbc
import sqlalchemy as sa
import pymysql

# print(pyodbc.drivers())
# print(sqlalchemy.drivers())

servername='EPINHYDW015E'
databasename='DEMO'
tablename='CATEGORY'

df1=pd.read_excel('C:\\Users\\Sairam_Kanamarlapudi\\Desktop\\Python\\CategoryData.xlsx')
print(df1)
df2=pd.read_csv('C:\\Users\\Sairam_Kanamarlapudi\\Desktop\\Python\\Data.csv')
print(df2)
engine=sa.create_engine(f'mssql+pyodbc://{servername}/{databasename}?driver=SQL+Server+Native+Client+11.0')
df1.to_sql(tablename,engine,if_exists='append',index=False)
print(engine)
df1['fullname']=df1['firstname']+df1['lastname']
print(engine)
print(df1)
pivot_data=df1.pivot_table(index='Category',columns='Year',values='Amount')
print(pivot_data)
print(pivot_data.rename_axis(columns=None).reset_index())
pivot_data.to_sql(tablename,engine,if_exists='append',index=False)



# # data = {
#          'name' : ['sai','ram','kumar'],
#          'age'  : [20,30,40]
#         }
#
# df=pd.DataFrame(data)
# print(df)

