import requests 
import lxml
from bs4 import BeautifulSoup 
url="https://www.snapdeal.com/search?clickSrc=top_searches&keyword=sport%20shoe%20men&categoryId=0&vertical=p&noOfResults=20&SRPID=topsearch&sort=rlvncy"
d=requests.get(url)
data=d.content
soup=BeautifulSoup(data,'lxml')
products=soup.find_all("div",{"class":"product-desc-rating"})
f=open("snapdeal_scrape.txt","w")
    
for product in products:
    title=product.find("p",{"class":"product-title"}).text.strip()
    price=product.find("span",{"class":"lfloat product-price"}).text.strip()
    discount=product.find("div",{"class":"product-discount"}).text.strip()
#        print(f'''
#        Product Name :   {title}
#        Price        :   {price}
#        Discount     :   {discount}
#              ''')
    f.write(" Product Name : "+title+"\n")
    f.write(" Price        : "+price+"\n")
    f.write(" Discount     : "+discount+"\n")
    f.write("=============================@@@@@@@@@@@@@@@@@========================\n")
f.close()