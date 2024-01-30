import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from io import StringIO

eurovaistine_data = []
for i in range(1, 9):
    target = f"https://www.eurovaistine.lt/paieska/rezultatai?q=persalimui&page={i}"
    response = requests.get(target)
    soup = BeautifulSoup(response.content, 'html.parser')
    script_tags = soup.find_all('script', type='application/json')

    for script in script_tags:
        data_component_name = script.get('data-component-name')
        if data_component_name and 'ProductsList' in data_component_name:
            products_json = json.loads(script.string)
            for product in products_json['products']:
                for variant in product['variants']:
                    item = {
                        'Brand': variant['brand'],
                        'Title': variant['name'],
                        'Price_special': variant['price']['price'],
                        'Price_regular': variant['price']['regularPrice']
                    }
                    eurovaistine_data.append(item)

json_data = json.dumps(eurovaistine_data, indent=4, ensure_ascii=False)
print(json_data)
# json_data_io = StringIO(json_data)
# df = pd.read_json(json_data_io)
# df.to_csv('products_Eurovaistine.csv', index=False)