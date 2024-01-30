

from bs4 import BeautifulSoup
import requests
import pandas as pd

products_data = []
for i in range(1,4):
    target = f"https://www.apotheka.lt/slaugos-ir-higienos-priemones/persalimui-ir-gripui?p={i}"
    response = requests.get(target)
# print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)



    products = soup.find_all('div', class_='box-product')

    for product in products:
        title = product.find('div', class_='box-product__title').text.strip()
        price = product.find('span', class_='product-pricing__price-number')


        products_data.append({
            'Title': title,
            'Price': price
        })

# print(products_data)
df = pd.DataFrame(products_data)
df.to_csv('Apotheka.products.csv', index=False)
print(df)