import FinanceDataReader as fdr
import pandas   as pd
import pymysql
from datetime import datetime

connection = pymysql.connect(host='localhost', port=3306, db='home', \
  user='root', passwd ='arfrom', autocommit=True)
cursor = connection.cursor()

df_krx = fdr.StockListing('KRX')  # KRX는 KOSPI,KOSDAQ,KONEX 모두 포함
df_krx = df_krx.loc[df_krx['Code'].str.isdigit(),['Code','Name','Market']]  #테이블로 로딩할 칼럼만 선택한다.

count = 0
today = datetime.today().strftime('%Y%m%d')
for  idx,row in df_krx.iterrows() :
  count += 1
  
  sql = "REPLACE INTO company_info (code, company, market, last_update) VALUES (%s,%s,%s,%s)"
  cursor.execute(sql,(*row,today))
  connection.commit()
  # print(f"[company_info] {count:,} rows upsert completed")  

sql = "select max(date) from daily_price"
cursor.execute(sql)
sdate = cursor.fetchone()[0]   # empty 이면 None  fetchone 의 return 타입은 tuple

if sdate is None :
	sdate = '20220101'

# sdate='20220101'
count=0
for idx,row in df_krx.iterrows() :
  df = fdr.DataReader(row[0],'20230101')
  # df = fdr.DataReader(row[0],'20220701', '20230101')
  # df = fdr.DataReader(row[0],'20220101', '20220701')
  if df.empty :
    continue
  df = df.dropna().reset_index()  #
  df["Date"] = df["Date"].dt.strftime("%Y%m%d")
  for sidx,srow in df.iterrows() :
    sql = """REPLACE INTO daily_price (code, date, open, high, low, close,  volume, chg) VALUES ('{}','{}',{},{},{},{},{},{})
          """.format(row[0],*srow)
    cursor.execute(sql)
    connection.commit()
  count += 1
  print(f"[daily_price]  {count:,} upsert completed")