#
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import csv
# import json
#
# # Eurovaistine, nereceptiniai vaistai, nuo persalimo
#
# products_data = []
# for i in range(1, 6):
#     url = f"https://www.eurovaistine.lt/vaistai-nereceptiniai/persalimui?page={i}"
#     response = requests.get(url)
#     # print(response.status_code)
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#     # products = soup.find_all('div', class_='content')
#     products = soup.find_all('div', class_='productCard')
#
#     for product in products:
#         gamintojas = product.find('div', class_='brand mt-0').text.strip()
#         pavadinimas = product.find('div', class_='title').text.strip()
#         kaina = product.find('div', class_='productPrice text-end').text.strip().replace(' €', '')
#         likutis = product.find('div', class_='soldOut').text.strip()
#
#         products_data.append({
#             'Gamintojas': gamintojas,
#             'Pavadinimas': pavadinimas,
#             'Kaina': kaina,
#             'Likutis': likutis
#         })
#
#
#
#     json_data = json.dumps(products_data, indent=4)
#
#     with open('eurovaistine_data.csv', mode='w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=json_data[0].keys())
#         writer.writeheader()
#         writer.writerows(json_data)
#
#
# #
# #
# # # df = pd.DataFrame(products_data)
# # # print(df)
# # # df.to_csv('eurovaistine.csv', index=False)
# # # print(df)



import requests
import pandas as pd
import json


def data_scraping():

    # jungimasis prie reikiam url ir neformatuotų duomenų atsisiuntimas

    print("prisijungimas prie svetainės")
    for i in range(1, 6):
    url = f"https://www.eurovaistine.lt/vaistai-nereceptiniai/persalimui?page={i}"
    response = requests.get(url)
    print(response)

    # išvestį formatuojame json formatu ir duomenis išsirenkame pagal stulpelius

    print('duomenų surinkimas')
    y=response.json()['_data']
    products_data = []
    print('dataframe kūrimas')
    for entry in y:
        products_data.append([entry['_id'], entry['centras'].strip(), entry['registravimo_vieta'].strip(), entry['miestas'].strip(), entry['galutine_diagnoze'].strip(), entry['ligonis_hospitalizuotas'], entry['socialiai_apdraustas'], entry['infekcijos_tipas'].strip(), entry['is_salies'].strip(), entry['ligos_klinikine_eiga'].strip(), entry['atvyk'], entry['kreip_diag'], entry['pranesimo_menuo'], entry['mirtis'], entry['sukelejo_rusis'].strip()])
    gamintojas = product.find('div', class_='brand mt-0').text.strip()
    #         pavadinimas = product.find('div', class_='title').text.strip()
    #         kaina = product.find('div', class_='productPrice text-end').text.strip().replace(' €', '')
    #         likutis = product.find('div', class_='soldOut').text.strip()
    df = pd.DataFrame(products_data)
    df.columns =['_id','centras', 'registravimo_vieta', 'miestas','galutine_diagnoze','ligonis_hospitalizuotas','socialiai_apdraustas','infekcijos_tipas','is_salies','ligos_klinikine_eiga','atvyk','kreip_diag','pranesimo_menuo','mirtis','sukelejo_rusis']

    # pd.set_option('display.max_columns', 30)  # or 1000
    # pd.set_option('display.max_rows', 30)  # or 1000
    # pd.set_option('display.max_colwidth', 30)  # or 199

    # duomenis eksportuojame dataframe formatu
    return df

# print(data_scraping())