# Määrittelydokumentti

Tämän projektin tavoite on luoda RSA-avainpareja joita käytetään tiedon salaamiseen ja purkuun. Valitsin tämän projektin sillä olen käyttänyt töissä RSA-salaukseen perustuvia komponentteja niin tämä oli hyvä mahdollisuus opetella miten RSA-avainparit luodaan ja mikä niiden toimintalogiikka on ns pinnan alla.

### Syötteet
Projektilla tulee olemaan komentoriviltä käytettävä tesktipohjainen käyttöliitymä johon käyttäjä syöttää tekstin. Ohjelma siten salaa annetun tekstin ja tulostaa sen komentoriville.
Ohjelma toimii myös toiseen suuntaan, eli sille voidaan syöttää salattu teksti jonka ohjelma sitten purkaa ja tulostaa komentoriville viestin.

### Kielet ja opinto-ohjelma
Projekti toteutetaan pythonilla ja dokumentaatio kirjoitetaan suomeksi. Voin vertaisarvioida myös Java projekteja ja englanninkielisiä projekteja.
Sisällytän kurssin tietojenkäsittelytieteen kanditutkintoon TKT.

### Mitä ongelmaa ratkaistaan?
RSA-salaus on yksi tapa salata tekstimuodossa olevaa tietoa jonka voi sitten lähettää vastaanottajalle ja jos joku saa salatun tekstin kaapattua lähetyksen aikana, teksti on lukemattomassa muodossa ilman avainparia sen purkuun.
Eli tietoa voidaan lähettää salattuna ja turvallisemmin lähettäjälle, ratkaisten tietoturvariskeihin liittuvän ongelman.

### Projektin tietorakenteet ja algoritmit ja miksi ne on valittu
#### Tietorakenteet
RSA-salauksessa luodaan avainparit jotka sisältää julkisen ja yksityisen avaimen. Avainparien luominen perustuu isojen alkulukujen löytämiseen. Eli tietorakenteita ihan vain muuttujien lisäksi ei tarvita.

#### Algoritmit
Ensin tulee luoda alkuluvut ja varmistaa että ne ovat oikeasti alkulukuja.
Alkulukujen luonti
  * Eratosteeneen seula: Löytää alkuluvut annettuun parametriin asti. Algorimi toimii aloittamalla luvusta 2 ja luo listan luonnollisista luvuista 2-> parametriin n asti. Sen jälkeen tätä lukulistaa käsitellään matemaattisin perustein ja lopulta saadaan lista jossa on jäljellä enää alkulukuja. Valittu koska luo luotettavasti alkulukuja.
Alkulukujen luonnin testaus
 * Rabin-Miller algoritmi: Varmistaa että annettu luku on alkuluku (tai varmistaa että se ei ole alkuluku). Algortimi käy lukua läpi n kertaa ja mitä enemmän sitä käydään läpi, sitä isommalla varmuudella voidaan sanoa onko luku alkuluku vai ei. Rabin-Millernin huono puoli on se, että se saattaa 25% todennäköisyydellä vättää ei-alkulukua alkuluvuksi. Tätä todennäköisyyttä siis pienennetään aina potenssiin n kun se ajetaan n kertaa. Valittu koska todennäköisyyttä että alkuluku tunnistetaan saa helposti kasvatettua.
RSA-avaimen luominen
  * Laajennettu Euklideen algoritmi: Salaimen luominen tehdään käyttäen modulaariaritmetiikkaa. Valittu koska vaikuttaa luotettavasti tekevän RSA-salaukseen tarvittavan avaimen.

### Aika- ja tilavaativuudet
z = alkulukujen yläparametri
x = läpikäyntien määrämoi
y = annettu luku
  * Eratosteeneen seula:
      - Aika O(z log (log z))
      - Tila O(1)
  * Rabin-Miller algoritmi:
      - Aika 0(x log^3 y)
      - Tila O(1)
  * Laajennettu Euklideen algoritmi:
      - Aika 0(n^2)
      - Tila O(1)

### Lähteet
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
http://www.mit.jyu.fi/opiskelu/seminaarit/ohjelmistotekniikka/rsa/#s24
https://en.wikipedia.org/wiki/Euclidean_algorithm
