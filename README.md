# BAIGIAMASIS DARBAS

Baigiamasis projektas Vilnius Coding School duomenų analitikos ir python programavimo pagrindų kursui
Darbo autoriai: Ala Čepelevskaja ir Edita Turčinavičiūtė.
Projekto tema: Vaistų kainų palyginimas internetinėse vaistinėse.
Projekto tikslas: palyginti vaistų kainas dvejose internetinėse vaistinėse (Eurovaistinė ir Gintarinė vaistinė) peršalimo kategorijoje. Tikslas - identifikuoti kainų skirtumus, nustatyti pigiausius ir brangiausius produktus analizuojamose vaistinese, bei išsiaiškinti, kaip kainos skiriasi priklausomai vaistų prekės ženklo ar kitų veiksnių.
Pasirinktos duomenų bazės apimtis: 2 internetinės svetainės, peršalimo kategorija :
 Eurovaistinė :
•	339 eilutės (unikalūs produktai pagal pavadinimą),
•	4 stulpeliai (gamintojas, pavadinimas, speciali kaina, reguliari kaina).
Gintarinė vaistinė :
•	306 eilutės (unikalūs produktai pagal pavadinimą),
•	4 stulpeliai (gamintojas, pavadinimas, speciali kaina, reguliari kaina).
Darbas atliktas Python kalba.

## PROJEKTO SEKA

### I.	DUOMENŲ IŠTRAUKIMAS, APDOROJIMAS, SAUGOJIMAS

Failų pavadinimai: FinalProjectEurovaistine.py, FinalProjectGintarine.py.
Panaudotos bibliotekos: Requests, BeautifulSoup, Pandas, json, StringIO.
Atlikti žingsniai: suradome analizei reikalingus duomenis internete, išsitraukėme informaciją, išsirinktus duomenis suformatavome, duomenis eksportavome dataframe formatu į csv failus.

### II.	DUOMENŲ ANALIZĖ IR VIZUALIZACIJA

Failų pavadinimai: FinalProject.py
Panaudotos bibliotekos: Pandas, MatplotLib, Numpy. 
Atlikti žingsniai: įsikėlėme rastus duomenis, apjungėme informaciją, sutvarkėme duomenis, atlikome duomenų analizę ir sukūrėme vizualizacijas. 
Atlikti skaičiavimai:
1.	unikalių gamintojų skaičius, siūlomų produktų skaičius, produktų skaičius pagal kategorijas;
2.	brangiausias ir pigiausias produktas kiekvienoje nagrinėjamoje vaistinėje;
3.	kainų vidurkis pagal vaistines;
4.	kainų mediana pagal vaistines;
5.	produktų kiekis, kurių kaina iki 10 Eur ir virš 10 Eur.


Vizualizacijos:
1.	6 pozicijų kainų palyginimas pagal vaistines:
   ![image](https://github.com/AlaCepelevskaja/Final_project_Pyton_2024-01/assets/158014250/e6777e01-2570-47fa-af32-87c383e5ab35)


 
3.	TOP5 brangiausi vaistai pagal vaistines:
   ![image](https://github.com/AlaCepelevskaja/Final_project_Pyton_2024-01/assets/158014250/36d992fa-5dea-4938-8293-e93d0c390529)


3.	TOP5 pigiausi vaistai pagal vaistines:

 
 
4.	Kainų pasiskirstymas:
 
 
5.	10 gamintojų vidutinė kaina:
 
 


III.	ANALIZĖS IŠVADOS
Abi vaistinės siūlo panašų kiekį produktų peršalimo kategorijoje (Eurovaistinė – 339, o Gintarinė vaistinė – 306), tik šiek tiek skiriasi pagrindiniai gamintojai (Eurovaistinės pagrindinis gamintojas, siūlantis daugiausia produktų peršalimo kategorijoje yra ŠVF, o Gintarinės vaistinės – AMBIO).
Siūlomų produktų kaina peršalimo kategorijoje skiriasi ženkliai pagal brangiausius produktus, nes Eurovaistinė siūlo ne tik vaistinius preparatus, bet pvz. inhaliatorius:
•	brangiausias Eurovaistinės produktas: 87.99 Eur (EVOLU inhaliatorius NANO AIR PRO);
•	brangiausias Gintarinės vaistinės produktas: 24.14 Eur (OSCILLOCOCCINUM, piliulės, vienadozė talpyklė, N30);
•	pigiausias Eurovaistinės produktas: 0.47 Eur (EUROCARE pipirinis pleistras, 10 cm x 18 cm);
•	pigiausias Gintarines produktas: 0.98 Eur (VITADAY MUKALTINAS, 10 tablečių).
Išanalizavus duomenis, matome tendenciją, kad dauguma produktų abiejose vaistinėse yra iki 10 Eur (Eurovaistinėje – apie 89 %, o Gintarinėje vaistinėje - apie 92 %).
Pagal duomenis matome, kad Gintarinės vaistinės reguliarios kainos (nuolatinės) yra šiek tiek mažesnės nei Eurovaistinės. 
Kainų mediana pagal vaistines:
•	Eurovaistinės produktų kainų mediana:  5.69;
•	Gintarinės vaistinės produktų kainų mediana:  6.29.
Pagal surinktus 2 internetinių vaistinių duomenis, matoma tendencija kad kainų lygis yra labai panašus, o skirtumai matomi tik taikant specialias kainas.
