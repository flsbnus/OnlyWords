import requests
from bs4 import BeautifulSoup

url="https://www.wordreference.com/enko/complicate"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
res=requests.get(url)
bs=BeautifulSoup(res.content,'html.parser')
mean=bs.select_one("#enko\:50944 > td.ToWrd")
mean1=mean.find("em")
mean.find("em").decompose()
#<td class="ToWrd">~을 복잡하게 하다 <em class="POS2" data-lang="ko">동(타)</em></td>
print(mean.text)