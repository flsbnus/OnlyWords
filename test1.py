import requests
from bs4 import BeautifulSoup

#https://www.wordreference.com/검색
wordput=input()
url=f"https://www.wordreference.com/enko/{wordput}"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}
res=requests.get(url)
bs=BeautifulSoup(res.content,'html.parser')
mean=bs.select("td.ToWrd")
print(mean)
words=[]
for i in range(len(mean)):
    words.append(bs.select("td.ToWrd")[i].get_text())
#print(words)
search="한국어"
for word in words:
    if search in word:
        words.remove(word)
print(words)

