import FinanceDataReader as fdr
import pandas   as pd
import pymysql
from datetime import datetime
import matplotlib.pyplot as plt

connection = pymysql.connect(host='localhost', port=3306, db='Investar', \
	user='root', passwd ='', autocommit=True)
cursor = connection.cursor()

query = "                                                                \
select a.code, b.name, a.date, a.open, a.high, a.low, a.close, a.volume  \
from  daily_price  a                                                     \
join  company_info  b                                                    \
	on  a.code = b.symbol                                                \
where  1=1                                                               \
and    date_format(a.date,'%Y%m%d') > '20210901'                         \
and    code = '009150'                                                   \
"

df = pd.read_sql(query,connection)
df['MA20'] = df['close'].rolling(window=20).mead()
df['stddev'] = df['close'].rolling(window=20).std()
df['upper'] = df['MA20'] + (df['stddev']*2)
df['lower'] = df['MA20'] - (df['stddev']*2)
df=df[19:]

plt.figure(figsize=(9,5))
plt.plot(df.index, df['close'], color = '#0000FF', label='close')
plt.plot(df.index, df['upper'], 'r--',label = 'Upper band')
plt.plot(df.index, df['lower'], 'k--',label = 'lower band')
plt.plot(df.index, df['MA20'], 'o--',label = 'MA20')
plt.fill_between(df.index, df['upper'],df['lower'],color= '0.9')
plt.legend(loc='best')
plt.title('Samsung jungi')
plt.show()
connection.close()