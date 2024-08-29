import pandas as pd
from bs4 import BeautifulSoup
import requests
Product_name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(2,12):
    url = 'https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_8_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_8_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=17138e79-4aa9-424a-a23a-4aee80cf6d1f&page='+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    box=soup.find("div", class_="DOjaWF gdgoEp")

    if box is not None:

        names=box.find_all("div",class_="KzDlHZ")
        for i in names:
            name=i.text
            Product_name.append(name)
        #print(Product_name)
            
        prices=box.find_all("div",class_="Nx9bqj _4b5DiR")
        for i in prices:
            price=i.text
            Prices.append(price)
        #print(Prices)

        desc=box.find_all("ul",class_="G4BRas")
        for i in desc:
            descr=i.text
            Description.append(descr)
        #print(Description)


        review=box.find_all("div",class_="XQDdHH")
        for i in review:
            reviews=i.text
            Reviews.append(reviews)
        #print(Reviews)
    else:
        print(f"No box found on page {i}")

df=pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
print(df)



# #while True:
# np=soup.find("a",class_="_9QVEpD").get("href")
# cnp="https://www.flipkart.com"+np
# print(cnp)

# # url=cnp
# # r = requests.get(url)
# # soup = BeautifulSoup(r.text, 'html.parser')
