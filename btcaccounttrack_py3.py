# -*- coding: utf-8 -*-
import requests
import time
print ("Taiwan local time:"), time.ctime()
print ("")
from bs4 import BeautifulSoup
res1 = requests.get("https://blockchain.info/address/115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn")
res2= requests.get("https://blockchain.info/address/12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw")
res3= requests.get("https://blockchain.info/address/13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94")
soup1=BeautifulSoup(res1.text,"html5lib")
soup2=BeautifulSoup(res2.text,"html5lib")
soup3=BeautifulSoup(res3.text,"html5lib")
for n1 in soup1.select("#total_received"):
     print ('WannaCry Account_01 = ',n1.text)
for n2 in soup2.select("#total_received"):
     print ('WannaCry Account_02 = ',n2.text)
for n3 in soup3.select("#total_received"):
     print ('WannaCry Account_03 = ',n3.text)

for t1 in soup1.select("#n_transactions"):
     print ('Number Transactions in account_01 = ',t1.text,'txs')
for t2 in soup2.select("#n_transactions"):
     print ('Number Transactions in account_02 = ',t2.text,'txs')
for t3 in soup3.select("#n_transactions"):
     print ('Number Transactions in account_03 = ',t3.text,'txs')

total = float(n1.text.replace(' BTC','')) + float(n2.text.replace(' BTC','')) + float(n3.text.replace(' BTC',''))
ts=int(t1.text)+int(t2.text)+int(t3.text)
print ('WannaCry total received =', total, 'BTC')
print ('WannaCry total received =', total*1750, 'USD' , '(in the rate 1BTC=1750 USD)')
print ('WannaCry total received =', total*1750*30.2, 'NT' , '(in the rate 1USD=30.2 TWD)')
print ('WannaCry total transcations received=',ts,'txs')
print ('WannaCry average received per transaction =', total/ts, 'BTC')
print ('WannaCry average received per transaction =', (total/ts)*1750, 'USD')
print ('WannaCry average received per transaction =', (total/ts)*1750*30.2, 'NT')
print ('')
print ('台灣本地時間:', time.ctime())
print ('勒索軟體WannaCry總共收到贖款共 =', total, '比特幣')
print ('勒索軟體WannaCry總共收到贖款共：', total*1750, '美元' , '(以1比特幣=1750美元換算)')
print ('勒索軟體WannaCry總共收到贖款共：', total*1750*30.2, '新台幣' , '(以1美元=30.2新台幣換算)')
print ('勒索軟體WannaCry總共收到贖款筆數:',ts,'筆')
print ('勒索軟體WannaCry平均每筆贖款 =', total/ts, '比特幣')
print ('勒索軟體WannaCry平均每筆贖款 =', (total/ts)*1750, '美元')
print ('勒索軟體WannaCry平均每筆贖款 =', (total/ts)*1750*30.2, '新台幣')

