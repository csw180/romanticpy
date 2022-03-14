import numpy as np
import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import datetime

class Ntester :
    def  __init__(self, stockcode,stockname) :
        self.stockcode = stockcode
        self.stockname = stockname
        self.df = None
        self.simp_df = None
        self.target_price = 0
        self.losscut_price = 0

    def  make_df(self) :
        startdate = datetime.datetime(2021, 9, 1)
        df = web.DataReader(self.stockcode, 'naver',startdate)
        
        if  len(df) < 100 :
            self.df = None
            return

        df['Open'] = df['Open'].astype(float, errors = 'ignore')
        df['High'] = df['High'].astype(float, errors = 'ignore')
        df['Low'] = df['Low'].astype(float, errors = 'ignore')
        df['Close'] = df['Close'].astype(float, errors = 'ignore')
        df['ma5'] = df['Close'].rolling(window=5).mean()
        df['ma60'] = df['Close'].rolling(window=60).mean()
        df['ma5_asc'] = df['ma5'] - df['ma5'].shift(1)
        df['Volume'] = df['Volume'].astype(float, errors = 'ignore')
        df['vma5'] = df['Volume'].rolling(window=5).mean()
        df['serial'] = pd.Series(np.arange(1,len(df.index)+1,1),index=df.index)
        conditionlist = [
                        (df['Close'] > df['ma5']) & \
                        (df['Close'].shift(1) < df['ma5'].shift(1)) & \
                        (df['Close'].shift(2) < df['ma5'].shift(2)) & \
                        (df['Close'].shift(3) < df['ma5'].shift(3))    ,\
                        (df['Close'] < df['ma5']) &\
                        (df['Close'].shift(1) > df['ma5'].shift(1)) &\
                        (df['Close'].shift(2) > df['ma5'].shift(2)) &\
                        (df['Close'].shift(3) > df['ma5'].shift(3)) \
                        ]
        choicelist1 = ['up', 'down']
        choicelist2 = [df['Low'].rolling(4).min(),df['High'].rolling(4).max()]

        df['way'] = np.select(conditionlist, choicelist1, default='')
        df['price'] = np.select(conditionlist, choicelist2, default='')

        refine_df = None
        df_copy = df.copy()
        df_copy = df_copy[df_copy['way'] > '']

        if len(df_copy.index) > 0 :
            df_copy = df_copy[::-1]

            refine_df = None
            prev_way = None
            trickery_list =[]
            for row in df_copy.itertuples():
                if (prev_way is None ) | (prev_way == row.way) :
                    trickery_list.append(row)
                    prev_way = row.way
                elif prev_way != row.way :
                    if refine_df is None :
                        refine_df = self.process_trickery(trickery_list).copy()
                    else :
                        refine_df = pd.concat([refine_df,self.process_trickery(trickery_list)])
                    trickery_list.clear()
                    trickery_list.append(row)
                    prev_way = row.way

            if  len(trickery_list) > 0 :
                if refine_df is None :
                    refine_df = self.process_trickery(trickery_list).copy()
                else :
                    refine_df = pd.concat([refine_df,self.process_trickery(trickery_list)])
            if  len(refine_df.index) > 3 :    
                refine_df['p_d1'] = refine_df['price'].shift(-1)
                refine_df['p_d1_ser'] = refine_df['serial'].shift(-1)
                refine_df['p_d2'] = refine_df['price'].shift(-2)
                refine_df['p_d2_ser'] = refine_df['serial'].shift(-2)
                refine_df['p_d3'] = refine_df['price'].shift(-3)               

                refine_df['p_d1'] = refine_df['p_d1'].astype(float, errors ='ignore')
                refine_df['p_d2'] = refine_df['p_d2'].astype(float, errors ='ignore')
                refine_df['p_d3'] = refine_df['p_d3'].astype(float, errors ='ignore')

                refine_df['p_d1_ser'] = refine_df['p_d1_ser'].astype(float, errors ='ignore')
                refine_df['p_d2_ser'] = refine_df['p_d2_ser'].astype(float, errors ='ignore')
                refine_df['price'] = refine_df['price'].astype(float, errors ='ignore')
                refine_df['attack'] = refine_df.apply( 
                    lambda row : 'good' if (row['way'] == 'up') and \
                                            (row['price'] > (row['p_d2']*1.003)) and \
                                            (row['p_d1'] > row['p_d3']*1.003) else '' ,axis=1)
            else :
                refine_df = None

        if (df is None) or (refine_df is None) :
            self.df = None
            return False

        df = df.drop(['way','price','serial'],axis = 1)
        self.df = df.join(refine_df)

        self.target_price =  0  
        df = self.df.copy()
        goodidx = df.index[df['attack']=='good'].tolist()
        if len(goodidx) > 0 :
            self.simp_df = df[df.index >= goodidx[-1]]
            if  (len(self.simp_df.index) == 2) and \
                (self.simp_df.iloc[0]['Close'] <= self.simp_df.iloc[0]['ma60']  ) and \
                (self.simp_df.iloc[-1]['ma5_asc'] > 0) and \
                (self.simp_df.iloc[0]['Close'] < max(self.simp_df.iloc[-1]['Close'],self.simp_df.iloc[-1]['Open'])) and \
                (self.simp_df.iloc[-1]['ma5'] <= self.simp_df.iloc[-1]['Close']) :
                # 5이평선이 우상향
                # 5이평돌파봉 다음봉은 고점이 돌파봉보다 높고 저점이 5이평보다 높아야함
                # 5이평돌파봉 다음다음봉도 조사시점현재 5이평보다 높아야함
                from_serial, to_serial  = self.simp_df.iloc[0]['p_d2_ser'], self.simp_df.iloc[0]['p_d1_ser']
                now_serial = self.simp_df.iloc[0]['serial']
                val_fromIdx, val_toIdx, val_nowIdx = self.df[self.df['serial']==from_serial].index.tolist(), \
                                self.df[self.df['serial']==to_serial].index.tolist(), \
                                self.df[self.df['serial']==now_serial].index.tolist()

                k1 = self.df[(val_fromIdx[0] <= self.df.index) & (self.df.index < val_toIdx[0])]['Volume'].sum()
                k2 = self.df[(val_toIdx[0] <= self.df.index) & (self.df.index <= val_nowIdx[0])]['Volume'].sum()
                k3 = self.simp_df.iloc[0]['vma5']
                d1,d2 = to_serial - from_serial, now_serial - to_serial + 1
                v1 = k1/d1/k3*100.0
                v2 = k2/d2/k3*100.0
                # print(self.stockname,f'from_serial={from_serial}, to_serial={to_serial}, now_serial={now_serial}')
                # print(self.stockname,f'val_fromIdx={val_fromIdx[0]}, val_toIdx={val_toIdx[0]}, val_nowIdx={val_nowIdx[0]}')
                print(self.stockname,f'Volume  Asc:{k1:,.2f}/{d1}={v1:,.2f}% Desc:{k2:,.2f}/{d2}={v2:,.2f}%')
                # if (d1 < 14)  and  (d2 < 14) :
                #     # 눌림일수와 직전상승일수가 20일이내 일것.
                self.target_price =  self.simp_df.iloc[-1]['ma5']
                self.losscut_price = self.simp_df.iloc[0]['price']

    def  process_trickery(self,trickery_list) :
        index_list = []
        data_dict = {}    # way, price 두개 요소
        data_dict['way'] = None
        data_dict['price'] = None
        data_dict['serial'] = None
        for row in trickery_list:
            if len(index_list) == 0 :
                index_list.append(row.Index)
                data_dict['way'] = row.way
                data_dict['price'] = row.price
                data_dict['serial'] = row.serial
                continue
            elif  ( (row.way == 'up') and (row.Low < float(data_dict['price']) )) or \
                    ( (row.way == 'down') and (row.High > float(data_dict['price']) )) :
                index_list.clear()
                index_list.append(row.Index)
                data_dict['way'] = row.way
                data_dict['price'] = row.price
                data_dict['serial'] = row.serial
        return pd.DataFrame(data_dict, index=index_list)

    def  do(self) :
        self.make_df()
        if (self.df is None) or (self.simp_df is None) or (self.target_price==0):
            return False
        else :
            print(f'{self.stockname}({self.stockcode}) target_price = {self.target_price}')
            return True

def  test() :
    f = open(r"./stockcode.txt", 'r',encoding="utf-8")
    count = 0 
    while True:
        line = f.readline()
        if not line: 
            print(f'stock processing code count = {count}')
            break
        tokens = line.strip().split('|')
        tester = Ntester(tokens[0],tokens[1])
        tester.do()
        count +=1
    f.close()

if __name__ == "__main__":
    # test()

    # 챠트그리기
    tester = Ntester('277070','린더먼')
    tester.do()
    tester.df.to_excel('a.xlsx')
    fillered_df = tester.df[tester.df['way'] > '']
    plt.figure(figsize=(9,5))
    plt.plot(tester.df.index, tester.df['ma5'], label="MA5")
    plt.plot(tester.df.index, tester.df['ma60'], label="MA60")
    plt.plot(fillered_df.index, fillered_df['price'], label="Price")
    plt.plot(tester.df.index, tester.df['Close'], label="close")
    plt.legend(loc='best')
    plt.grid()
    plt.show()


