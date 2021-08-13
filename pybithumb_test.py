import pybithumb

# 가상화폐 고유 이름들
tickers = pybithumb.get_tickers()
#print(tickers , "\n" , len(tickers))

# 특정 티커의 현재가
price = pybithumb.get_current_price("BTC")
#print(price)

import time

# while True:
#     price = pybithumb.get_current_price("BTC")
#     #print(price)
#     time.sleep(1)

# 시가 고가 저가 종가 거래량 튜플
detail = pybithumb.get_market_detail("BTC")
#print(detail)

# 딕셔너리형식
orderbook = pybithumb.get_orderbook("BTC")
#print(orderbook)
#키값 리턴
#for i in orderbook: 
    #print(i)

# 1970년 1월1일부터 지나간 ms(milli second) 를 가져온다.
import datetime
ms = int(orderbook["timestamp"])
dt = datetime.datetime.fromtimestamp(ms/1000)
#print(dt)

#전체 티커 가져와서 #print
all = pybithumb.get_current_price("ALL")
#for k , v in all.items():
    #print(k,v)

# btt 의 모든 날짜별 시가 고가 저가 종가 거래량 가져온다.
btt = pybithumb.get_ohlcv("BTT")
print(btt)
# 종가만
close = btt['close']
print(close)
# 단순 5개의 값 5일의 이동평균선 
# print((close[0] + close[1] + close[2] + close[3] + close[4] ) / 5 )
# print((close[1] + close[2] + close[3] + close[4] + close[5] ) / 5 )
# print((close[2] + close[3] + close[4] + close[5] + close[6]) / 5 )

# # rolling 의 뜻은 모든 데이터를 그룹화 5일씩 위에서 0 1 2 3 4 로 묶듯이
# window = close.rolling(5)
# # 그렇게 5일씩 묶은 그룹당 평균을 낸 series를 ma5 라는 변수에 넣음
# ma5 = window.mean() 
# print(ma5)

#위에 3줄을 축약해서 한 라인에 표현
# 이평선 담은 series
ma5 = close.rolling(5).mean()

# 상승하락 판단
def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    last_ma5 = ma5[-2]

    price = pybithumb.get_current_price(ticker)

    if price > last_ma5:
        return True # 상승장
    else:
        return False # 하락장

is_bull = bull_market('btt')
if is_bull:
    print('상승장')

tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker , '상승장')
    else:
        print(ticker , '하락장')


















