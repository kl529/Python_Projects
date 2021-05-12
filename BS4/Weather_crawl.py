#네이버 날씨의 미세먼지 수치를 알려주는 프로그램
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')

soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'})

data2 = data1.findAll('dd')
# pprint(data2[0])

find_dust = data2[0].find('span',{'class':'num'}).text
pprint(find_dust)
