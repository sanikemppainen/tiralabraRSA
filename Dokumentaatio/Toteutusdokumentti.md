# Toteutusdokumentti

### Ohjelman yleisrakenne
Ohjelman käynnistäessä luodaan ensin salausavaimet. Sitten käyttäjältä kysytään syötettä salattavaksi. Tämä sitten salataan ja palautetaan salattu syöte ja dekryptattu viesti, jotta nähdään että salaus toimii.

Yleisesti ottaen ohjelman koodi voidaan jakaa kolmeen osaan:
1. Alkulukujen luonti: Tähän käytetään erasthoteenen seulaa, alkulukulistalta randomilla kahden arvon valitseminen, sekä Rabin-Millerin algoritmi. Myös apufunktio jossa lasketaan a^b mod c lasku. Valitaan sopivat alkuluvut p ja q.

2. Avainten luonti: Tähän käytetään Eucliden algoritmia ja aiemmin valittuja ja todennettuja p ja q muuttujia.

3. Enkryptaus ja dekryptaus: Tähän käytetään luotuja avaimia ja muutetaan merkki kerrallaan viesti joko salatuksi tai se puretaan. 

### Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)

#### Aikavaativuudet käytetyillä algoritmeilla:
Listan alustaminen vie O(n) aikaa pyhthonin standardilla listan luomisella: booleanlista = [] ja sen alustamisella True arvoiksi for loopilla. Toinen loop käy läpi lukujen potenssin ja vertailee niitä n, on erasthotheenen seula ja silä on O(n * log(log(n))) aikavaativuus. Kolmas loop luo alkulukulistan booleanlistasta ja sekin vie vain O(n) aikaa. Joten O(n * log(log(n))) on loytaa_alkuluvut_erasthoteen_seulalla(n) funktion aikavaativuus. Alkulukujen luomisessa on myös loyda_p_q(alkuluku_lista) funktio jossa on while loop jonka sisällä on käytetty random kirjastoa. Tällä on vakio aikavaativuus O(1). Tämä funktio kutsuu onko_alkuluku(luku, k) funktiota joka sisältää Rabin-Millerin algoritmin jonka aikavaativuus on O(k * log^3(n)), jossa k on iteraatioiden määrä. Viimeinen osa alkulukujen luonnissa on laske_mod_exp(a, b, c) joka laskee a^b mod c laskun, ja tällä on aina aikavaativuus O(log(b)). loytaa_alkuluvut_erasthoteen_seulalla() funktio poislukien, muuiden aikavaativuuteen vaikuttaa suuresti random.choice() arvotut arvot. n näissä laskelmissa viittaa alkulukujen määrään, eli luvun luonnin yläparametriin.


### Työn mahdolliset puutteet ja parannusehdotukset
Työstä olisi voinut tehdä molemminpäin toimivan, eli käyttäjältä olisi myös voinut kysyä salattua viestiä purettavaksi. Nyt salaaminen ja purkaminen tehdään annetulle samalle syötteelle.

### Lähteet
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
http://www.mit.jyu.fi/opiskelu/seminaarit/ohjelmistotekniikka/rsa/#s24
https://en.wikipedia.org/wiki/Euclidean_algorithm
