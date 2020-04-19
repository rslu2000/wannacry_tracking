# -*- coding: utf-8 -*-
# https://repl.it/repls/LowestUnwelcomeCharacterencoding
import requests
import time
import html5lib
print 'Taiwan local time:', time.ctime()
from bs4 import BeautifulSoup
res1 = requests.get("https://blockchain.info/address/115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn")
res2= requests.get("https://blockchain.info/address/12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw")
res3= requests.get("https://blockchain.info/address/13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94")
soup1=BeautifulSoup(res1.text,"html5lib")
soup2=BeautifulSoup(res2.text,"html5lib")
soup3=BeautifulSoup(res3.text,"html5lib")
element1= soup1.select('[class="sc-8sty72-0 cyLejs"] [class="sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk"]')[2]
print 'WannaCry Account_01 = ',element1.text
element2= soup2.select('[class="sc-8sty72-0 cyLejs"] [class="sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk"]')[2]
print 'WannaCry Account_02 = ',element2.text
element3= soup3.select('[class="sc-8sty72-0 cyLejs"] [class="sc-1ryi78w-0 bFGdFC sc-16b9dsl-1 iIOvXh u3ufsr-0 gXDEBk"]')[2]
print 'WannaCry Account_03 = ',element3.text

total = float(element1.text.replace(' BTC','')) + float(element2.text.replace(' BTC','')) + float(element3.text.replace(' BTC',''))
print 'WannaCry total received =', total, 'BTC'
print 'WannaCry total received =', total*1750, 'USD' , '(in the rate 1BTC=1750 USD)'
print 'WannaCry total received =', total*1750*30.2, 'USD' , '(in the rate 1USD=30.2 TWD)'
print '勒索軟體WannaCry總共收到贖款共：', total*1750, '美元' , '(以1比特幣=1750美元換算)'
print '勒索軟體WannaCry總共收到贖款共：', total*1750*30.2, '新台幣' , '(以1美元=30.2新台幣換算)'
