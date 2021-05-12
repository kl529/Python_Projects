#검색어를 입력하면 결과값을 CSV파일에 저장
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

search = input('검색어를 입력하세요 : ')
url = f'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={quote_plus(search)}'
html = urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

total = soup.select('.api_txt_lines.total_tit')
searchList = []

for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)

f = open(f'{search}.csv', 'w', encoding='utf-8',newline='')
csvwriter = csv.writer(f)
for i in searchList:
    csvwriter.writerow(i)

f.close()
print('완료')