import FinanceDataReader as fdr
import pandas   as pd
import pymysql
from datetime import datetime

def  main(sdate,edate='None') :
	df_krx = fdr.StockListing('KRX')  # KRX는 KOSPI,KOSDAQ,KONEX 모두 포함
	df_krx = df_krx.set_index('Symbol')  # 'Symbol 칼럼을 인덱스칼럼으로 지정한다.

	df_krx = df_krx[['Market','Name','Sector','Industry']]  #테이블로 로딩할 칼럼만 선택한다.
	# df_krx = df_krx.loc[df_krx['Name'].str.contains('WR') == False]  # WR(신주인수권) 요상한 종목들이 있어서 걸러냈다
	df_krx['Industry'] = df_krx['Industry'].str.replace("'",' ') # 데이터 안에 싱글이 있어서 제거했다.
	df_krx['Sector'].fillna('',inplace=True)
	df_krx['Industry'].fillna('',inplace=True)
	df_krx = df_krx.loc[(df_krx.index.str.len() == 6) & (df_krx.index.str.isdigit() == True)]

	connection = pymysql.connect(host='localhost', port=3306, db='Investar', \
		user='root', passwd ='', autocommit=True)
	cursor = connection.cursor()
	today = datetime.today().strftime('%Y-%m-%d')
	count = 0
	for  row in df_krx.itertuples(name='KRX') :
		count += 1
		
		sql =  f"REPLACE INTO company_info (symbol, market, name, sector, industry, last_update) "+ \
			f"VALUES ('{row.Index}', '{row.Market}', '{row.Name}', '{row.Sector}', '{row.Industry}', '{today}')"
		
		tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
		cursor.execute(sql)
		connection.commit()
	print(f"[company_info] {count:,} rows upsert completed")

	today = datetime.today().strftime('%Y-%m-%d')
	count = 0

	for  row in df_krx.itertuples(name='KRX') :
		df : pd.DataFrame
		try :
			if edate :
				df = fdr.DataReader(row.Index, sdate, edate)
			else :
				df = fdr.DataReader(row.Index, sdate)
		except  ValueError :
			continue
		if df.empty : continue
		df['Change'].fillna(0,inplace=True)
		for srow in df.itertuples(name='D') :
			sql =  f"REPLACE INTO daily_price (code, date, open, high, low, close, volume, chg) "+ \
			f"VALUES ('{row.Index}', '{srow.Index}', '{srow.Open}', '{srow.High}', '{srow.Low}', '{srow.Close}', '{srow.Volume}', '{srow.Change:.2f}')"
			tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
			cursor.execute(sql)
			connection.commit()
		count += 1
		print(f"{count:,} : ({row.Index}){row.Name} upserted ")
	print(f"[daily_price]  {count:,} upsert completed")

if __name__=="__main__" :
	main('2021-11-01',None)

