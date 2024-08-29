import pandas as pd
from bs4 import BeautifulSoup
import requests

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 20):
    url = f'https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_8_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_8_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=17138e79-4aa9-424a-a23a-4aee80cf6d1f&page={i}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    box = soup.find("div", class_="DOjaWF gdgoEp")

    if box is not None:
        names = box.find_all("div", class_="KzDlHZ")
        prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
        descs = box.find_all("ul", class_="G4BRas")
        reviews = box.find_all("div", class_="XQDdHH")
        
        for name, price, desc, review in zip(names, prices, descs, reviews):
            Product_name.append(name.text)
            Prices.append(price.text)
            Description.append(desc.text)
            Reviews.append(review.text)
    else:
        print(f"No box found on page {i}")

# Check the length of all lists
min_len = min(len(Product_name), len(Prices), len(Description), len(Reviews))

# Trim all lists to the same length
Product_name = Product_name[:min_len]
Prices = Prices[:min_len]
Description = Description[:min_len]
Reviews = Reviews[:min_len]

df = pd.DataFrame({
    "Product Name": Product_name,
    "Prices": Prices,
    "Description": Description,
    "Reviews": Reviews
})

#print(df)

df.to_csv("D:/Flipkart_mobiles_under_50k.csv")
