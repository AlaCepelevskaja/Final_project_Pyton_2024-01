from bs4 import BeautifulSoup
import requests
import pandas as pd

products_data = []
for i in range(1,17):
    target = f"https://www.gintarine.lt/persalimas?pagenumber={i}"
    response = requests.get(target)
# print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)

    products = soup.find_all('form', {'data-productid':True})
    for product in products:
        brand = product.find('div', class_='product__brand').text.strip()
        title = product.find('div', class_='product__title').text.strip()
        price_special_text = product.find('span', class_='product__price--gv-club')
        price_regular_text = product.find('span', class_='product__price--regular')

        if price_special_text:
            price_special = price_special_text.text.strip().replace('€', '').replace(',', '.')
        else:
            price_special = 'N/A'
        if price_regular_text:
            price_regular = price_regular_text.text.strip().replace('€', '').replace(',', '.')
        else:
            price_regular = 'N/A'

        products_data.append({
            'Brand': brand,
            'Title': title,
            'Price_special': price_special,
            'Price_regular': price_regular

        })

# print(products_data)

df = pd.DataFrame(products_data)
df.to_csv('products_Gintarine.csv', index=False)
print(df)