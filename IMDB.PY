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
print(f"rating={m_rating.text}")
res= url.urlopen(path)
data= bs4.BeautifulSoup(res,"lxml")
m_year= data.find("span",class_="sc-8c396aa2-2 itZqyK")
print(f"year={m_year.text}")

div  = data.find("div",class_="sc-66a20916-0 lQXVY")
a_href = div.find("a")["href"]
path = Home+a_href

res= url.urlopen(path)
data= bs4.BeautifulSoup(res,"lxml")
divs = data.findAll("div",class_="review-container")
print("Reviews : ")
x =1
for div in divs:
    a = div.find("a")
    a_text = a.text.replace("\n","")
    print(f"{x}. {a_text}")
    x+=1
