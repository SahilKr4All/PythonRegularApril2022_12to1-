import urllib.request as url
import bs4
Home = "https://www.imdb.com"
path = "https://www.imdb.com/find?q="
moviename= input("movie name you wanna search=> ").replace(" ","%20")
path= path+moviename
res= url.urlopen(path)
data= bs4.BeautifulSoup(res,"lxml")
td= data.find("td", class_="result_text")
a= td.find("a")["href"]
path= Home+a
res= url.urlopen(path)
data= bs4.BeautifulSoup(res,"lxml")
m_rating= data.find("span",class_="sc-7ab21ed2-1 jGRxWM")
#print(f"rating={m_rating.text}")
res= url.urlopen(path)
data= bs4.BeautifulSoup(res,"lxml")
m_year= data.find("span",class_="sc-8c396aa2-2 itZqyK")
print(f"year={m_year.text}")

