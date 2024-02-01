import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',2000)

file_path = "products_Eurovaistine.csv"
products_df_E = pd.read_csv(file_path)

file_path_2 = "products_Gintarine.csv"
products_df_G = pd.read_csv(file_path_2)

# tvarkem Eurovaistines kaina, is centu vertem i Eurus
products_df_E['Price_special'] = products_df_E['Price_special'] / 100
products_df_E['Price_regular'] = products_df_E['Price_regular'] / 100
# print(products_df_E)

# sutvarkem: tikrinom ar Price_special yra N/A , jeigu taip - grazinom Price_regular reiksme
products_df_G['Price_special'] = products_df_G.apply(lambda x: x['Price_regular'] if pd.isna(x['Price_special']) else x['Price_special'], axis=1)
# print(products_df_G)

# apjungem 2 lenteles pagal "Title"
df1=products_df_E
df2=products_df_G
df3=df1.merge(df2,on='Title', how='outer', indicator=True)
# print(df3)

df = pd.DataFrame(df3)
# df.to_csv('products_analizei.csv', index=False)
# print(df)
# print(df.dtypes)

# pagal vaistine, persalimo kategorija, kiek rasta produktu (Title, Brand: unikaliu reiksmiu, kiek per kategorija produktu)
filtered_brand_G_df2 = df2['Brand'].nunique()
filtered_title_G_df2 = df2['Title'].count()
filtered_by_brand_G_df2 = df2['Brand'].value_counts()
# print('Gintarines siulomu produktu skaicius pagal gamintojus: ', filtered_by_brand_G_df2)
# print('Gintarines gamintoju persalimo vaistu kategorijoje: ', filtered_brand_G_df2)
# print('Gintarines siulomu produktu skaicius persalimo vaistu kategorijoje: ', filtered_title_G_df2)

filtered_brand_E_df1 = df1['Brand'].nunique()
filtered_title_E_df1 = df1['Title'].count()
filtered_by_brand_E_df1 = df1['Brand'].value_counts()
# print('Eurovaistines siulomu produktu skaicius pagal gamintojus: ', filtered_by_brand_E_df1)
# print('Eurovaistines gamintoju persalimo vaistu kategorijoje: ', filtered_brand_E_df1)
# print('Eurovaistines siulomu produktu skaicius persalimo vaistu kategorijoje: ', filtered_title_E_df1)

# pagal vaistine, randam brangiausia ir pigiausia produkta (max, min kainos)
max_price_E = df1['Price_special'].max()
min_price_E = df1['Price_special'].min()
max_price_G = df2['Price_special'].max()
min_price_G = df2['Price_special'].min()
# print('Brangiausias Eurovaistines produktas: ', max_price_E)
# print('Pigiausias Eurovaistines produktas: ', min_price_E)
# print('Brangiausias Gintarines produktas: ', max_price_G)
# print('Pigiausias Gintarines produktas: ', min_price_G)


# pagal vaistine: kainu vidurkis
average_price_by_brand_E = df1.groupby('Brand')['Price_special'].mean().round(2)
average_price_by_brand_G = df2.groupby('Brand')['Price_special'].mean().round(2)
# print('Eurovaistines siulomu produktu vidutine kaina pagal gamintoja: ', average_price_by_brand_E)
# print('Gintarines siulomu produktu vidutine kaina pagal gamintoja: ', average_price_by_brand_G)


# pagal vaistine: siulomu persalimo kategorijos produktu kainu mediana
median_price_E = df1['Price_special'].median()
median_price_G = df2['Price_special'].median()
# print('Eurovaistines produktu kainu mediana: ', median_price_E)
# print('Gintarines produktu kainu mediana: ', median_price_G)

# pagal vaistines: atfiltruoti produktus: iki 10 Eur ir virs 10 Eur. nubraizyti grafika
filtered_iki_10_E = df1['Price_special'][df1['Price_special'] <= 10].count()
filtered_virs_10_E = df1['Price_special'][df1['Price_special'] > 10].count()
filtered_iki_10_G = df2['Price_special'][df2['Price_special'] <= 10].count()
filtered_virs_10_G = df2['Price_special'][df2['Price_special'] > 10].count()
# print('Eurovaistines siulomu produktu kiekis iki (<=) 10 Eur: ', filtered_iki_10_E)
# print('Eurovaistines siulomu produktu kiekis  virs 10 Eur: ', filtered_virs_10_E)
# print('Gintarines siulomu produktu kiekis  iki (<=) 10 Eur: ', filtered_iki_10_G)
# print('Gintarines siulomu produktu kiekis  virs 10 Eur: ', filtered_virs_10_G)

# isrenkam 13 poziciju, is abieju vaistiniu
# group by _merge = both
filtras = 'both'
df3_filtered = df3[df3['_merge'] == filtras]
# print(df3_filtered.head(6))

# GRAFIKAI

# nr. 1: kainu palyginimas pagal vaistines
# plt.figure(figsize=(10,6))
# x = np.array(df3_filtered['Title'].head(6))
# y = np.array(df3_filtered['Price_special_x'].head(6))
# plt.scatter( 2, 2)
# plt.plot(x,y, 'o:g', label='Eurovaistine')
# y = np.array(df3_filtered['Price_special_y'].head(6))
# plt.plot(x,y, 'o:b', label='Gintarine')
# plt.xticks(rotation =270)
# plt.legend(loc="upper left")
# plt.xticks(rotation=90, ha='right', va='center', wrap=True)
# plt.subplots_adjust(bottom = 0.20)
# plt.suptitle('Kainu palyginimas pagal vaistines')
# plt.show()

# nr. 2: brangiausi vaistai pagal vaistine TOP5
# sorted_products = df1.sort_values(by='Price_special', ascending=False).reset_index(drop=True).head(5)
# # reset pakeisti numeracija, o head apibrezia kiek rezultatu norime
# plt.figure(figsize=(12,6))
# bars = plt.bar(sorted_products['Title'], sorted_products['Price_special'], color='green')
# for bar in bars:
#     yval=bar.get_height()
#     plt.text(bar.get_x()+bar.get_width()/2.0,yval,round(yval,2), va='bottom', ha='center')
# plt.xlabel('Produkto pavadinimas')
# plt.ylabel('Kaina, Eur')
# plt.title('Top 5 brangiausi produktai Eurovaistineje persalimo kategorijoje')
# plt.xticks(rotation=90, ha='right', va='center', wrap=True)
# plt.subplots_adjust(bottom = 0.20)
# plt.show()

# sorted_products = df2.sort_values(by='Price_special', ascending=False).reset_index(drop=True).head(5)
# # reset pakeisti numeracija, o head apibrezia kiek rezultatu norime
# plt.figure(figsize=(12,6))
# bars = plt.bar(sorted_products['Title'], sorted_products['Price_special'], color='blue')
# for bar in bars:
#     yval=bar.get_height()
#     plt.text(bar.get_x()+bar.get_width()/2.0,yval,round(yval,2), va='bottom', ha='center')
# plt.xlabel('Produkto pavadinimas')
# plt.ylabel('Kaina, Eur')
# plt.title('Top 5 brangiausi produktai Gintarineje vaistineje persalimo kategorijoje')
# plt.xticks(rotation=90, ha='right', va='center', wrap=True)
# plt.subplots_adjust(bottom = 0.20)
# plt.show()

# nr. 3: pigiausi vaistai pagal vaistine TOP5
# sorted_products = df1.sort_values(by='Price_special', ascending=True).reset_index(drop=True).head(5)
# # reset pakeisti numeracija, o head apibrezia kiek rezultatu norime
# plt.figure(figsize=(10,6))
# bars = plt.bar(sorted_products['Title'], sorted_products['Price_special'], color='green')
# for bar in bars:
#     yval=bar.get_height()
#     plt.text(bar.get_x()+bar.get_width()/2.0,yval,round(yval,2), va='bottom', ha='center')
# plt.xlabel('Produkto pavadinimas')
# plt.ylabel('Kaina, Eur')
# plt.title('Top 5 pigiausi produktai Eurovaistineje persalimo kategorijoje')
# plt.xticks(rotation=90, ha='right', va='center', wrap=True)
# plt.subplots_adjust(bottom = 0.20)
# plt.show()

# sorted_products = df2.sort_values(by='Price_special', ascending=True).reset_index(drop=True).head(5)
# # reset pakeisti numeracija, o head apibrezia kiek rezultatu norime
# plt.figure(figsize=(10,6))
# bars = plt.bar(sorted_products['Title'], sorted_products['Price_special'], color='blue')
# for bar in bars:
#     yval=bar.get_height()
#     plt.text(bar.get_x()+bar.get_width()/2.0,yval,round(yval,2), va='bottom', ha='center')
# plt.xlabel('Produkto pavadinimas')
# plt.ylabel('Kaina, Eur')
# plt.title('Top 5 pigiausi produktai Gintarineje vaistineje persalimo kategorijoje')
# plt.xticks(rotation=90, ha='right', va='center', wrap=True)
# plt.subplots_adjust(bottom = 0.20)
# plt.show()

# nr. 4: statistika
# plt.figure(figsize=(10,6))
# plt.hist(df1['Price_special'], bins=20, color="green")
# plt.title("Eurovaistines siulomu produktu kainu pasiskirstymas")
# plt.xlabel('Kaina, Eur')
# plt.ylabel('Produktu skaicius')
# plt.grid(True)
# plt.xticks(np.arange(0, 100, 5))
# plt.show()

# plt.figure(figsize=(10,6))
# plt.hist(df2['Price_special'], bins=20, color="blue")
# plt.title("Gintarines vaistines siulomu produktu kainu pasiskirstymas")
# plt.xlabel('Kaina, Eur')
# plt.ylabel('Produktu skaicius')
# plt.grid(True)
# plt.xticks(np.arange(0, 30, 5))
# plt.show()

# nr. 5: vidutine kaina pagal gamintoja
# plt.figure(figsize=(10,6))
# average_price_by_brand_E.head(10).plot(kind='bar', color="green")
# plt.title("Eurovaistines siulomu produktu vidutines kainos pagal 10 gamintoju")
# plt.xlabel('Gamintojas')
# plt.ylabel('Vidutine kaina')
# plt.xticks(rotation=90, ha='right', va='center', wrap=True)
# plt.subplots_adjust(bottom = 0.20)
# plt.show()

# plt.figure(figsize=(10,6))
# average_price_by_brand_G.head(10).plot(kind='bar', color="blue")
# plt.title("Gintarines vaistines siulomu produktu vidutines kainos pagal 10 gamintoju")
# plt.xlabel('Gamintojas')
# plt.ylabel('Vidutine kaina')
# plt.xticks(rotation=90, ha='right', va='center', wrap=True)
# plt.subplots_adjust(bottom = 0.20)
# plt.show()
