from re import A
import urllib.request as url
import bs4
homePath = "https://www.flipkart.com"
productName = input("Enter Product You wanna Search :").replace(" ","%20")
path = "https://www.flipkart.com/search?q="+productName
res = url.urlopen(path)
data = bs4.BeautifulSoup(res,'lxml')
a_link = data.find("a",class_="_1fQZEK")["href"]

path = homePath+a_link
res = url.urlopen(path)
data = bs4.BeautifulSoup(res,'lxml')
p_name = data.find("span",class_="B_NuCI")
print(f"Product Name => {p_name.text}")
p_pricing = data.find("div",class_="_30jeq3 _16Jk6d")
print(f"Product Price => {p_pricing.text}")
div = data.find("div",class_="_2418kt")
highlight_list = div.findAll("li",class_="_21Ahn-")

print("HighLights = >")
for item in highlight_list:
    print("         ",item.text)

div= data.find("div",class_="col JOpGWq")
a = div.findAll("a")[-1]["href"]; 
path = homePath+a

res = url.urlopen(path)
data = bs4.BeautifulSoup(res,'lxml')
p = data.findAll("p",class_="_2-N8zT")
print("Reviews = >")
for item in p:
    print("         ",item.text)
