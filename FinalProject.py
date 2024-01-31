import numpy
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',2000)


file_path = "products_Eurovaistine.csv"
products_df_E = pd.read_csv(file_path)

file_path_2 = "products_Gintarine.csv"
products_df_G = pd.read_csv(file_path_2)

# tvarkem kaina, is centu vertem i Eurus
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
print(df3_filtered)

# lyginam 2 vaistiniu kainas

# grafikas nr. 1
# plt.figure(figsize=(10,6))
# plt.hist(products_df['Price'], bins=20, color="darksalmon")
# plt.title("Histogram of product prices")
# plt.xlabel('Price')
# plt.ylabel('Number of products')
# plt.grid(True)
# plt.show()

# grafikas nr. 2
# sorted_products = df3_filtered.sort_values(by='Price_special', ascending=False).reset_index(drop=True).head(10)
#reset pakeisti numeracija, o head apibrezia kiek rezultatu norime
# plt.figure(figsize=(12,6))
# plt.bar(sorted_products['Title'], sorted_products['Price'], color='teal')
# plt.xlabel('Product Title')
# plt.ylabel('Price(€)')
# plt.title('Top 10 most expensive products')
# plt.xticks(rotation=90)
# plt.show()

# grafikas nr. 3
# plt.figure(figsize=(12,8))
# average_salary_by_dep.plot(kind='bar')
# plt.title('Vidutine kaina pagal gamintoja')
# plt.xlabel('Gamintojas')
# plt.ylabel('Vidutine kaina')
# plt.xticks(rotation=0) #padarom kad nesuktu teksto ant x asies
# plt.show()

# grafikas nr. 4
# df['Price'].plot(kind='hist', bins=20)
# plt.xlabel=('Kaina')
# plt.title('Kainu pasiskirstymas')
# plt.show()

# grafikas nr. 5
#ant kiekvieno stulpelio - reiksme
# data_to_plot=df['Price'].head(10)
# plt.figure(figsize=(10,6))
# bars=plt.bar(data_to_plot.index, data_to_plot.values)
# for bar in bars:
#     yval=bar.get_height()
#     plt.text(bar.get_x()+bar.get_width()/2.0,yval,round(yval,2), va='bottom', ha='center')
# plt.title('Produktu kainos')
# plt.xlabel('Produktu indeksai')
# plt.ylabel('Kaina')
# plt.show()