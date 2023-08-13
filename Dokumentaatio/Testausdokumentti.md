### Testausdokumentti

## Yksikkötestauksen kattavuusraportti.
Yksikkötestaus on hyvällä mallilla, codecoverage 99%. Codecoveragen saa ajettua kun menee /RSA kansioon ja ajaa komennon:
coverage run -m pytest 

ja sen jälkeen komennon:
coverage report

ja näillä saadaan tämminen kattavuusraportti aikaiseksi:


## Mitä on testattu, miten tämä tehtiin?
Yksikkötestit tehty sitä mukaa kun koodia on edistetty. Nämä on tehty pythonin yksikkätestausta pytestiä käyttäen. 

## Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
Testeihin on kirjoitettu syötteet valmiiksi niin testaajan ei tarvitse niistä huolehtia. Testien syötteet on ohjelmaa rakentaessa otettuja arvoja joiden oikeenlisuus on varmistettu myös valmiilla algoritmeilla. Esimerkiksi laske_mod_exp() fuktion testaamisessa käytetyt arvot testattiin valmiilla kirjastolla joka tekee saman työn, joten voi luottaa että nämä syötteet on oikeanlaisia. 

## Miten testit voidaan toistaa?
Testit voidaan ajaa ylläolevien ohjeidne mukaisesti. 

## Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa
TBA
