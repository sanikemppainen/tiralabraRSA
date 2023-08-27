### Testausdokumentti

## Mitä on testattu, miten tämä tehtiin?

### Yksikkötestaus
Yksikkötestit tehty sitä mukaa kun koodia on edistetty. Nämä on tehty pythonin yksikkätestausta pytestiä käyttäen. Kaikki metodit testataan automaattisesti pytestiä käyttäen ennen loppupalautusta.

#### Yksikkötestauksen kattavuusraportti.
Yksikkötestaus on hyvällä mallilla, codecoverage 99%. Codecoveragen saa ajettua kun menee /RSA kansioon ja ajaa komennon:

```coverage run -m pytest```

ja sen jälkeen komennon:
```coverage report```

ja näillä saadaan tämminen kattavuusraportti aikaiseksi:

![kattavuusraportti](https://github.com/sanikemppainen/tiralabraRSA/blob/main/Dokumentaatio/image.png)

### Järjestelmätestaus
Sovellusta on testattu manuaalisesti ja se on todettu toimivaksi.

### Suorituskykytestaus
Suorituskykytestauksessa laskettiin kauanko avaimien luonnisa kesti aikaa. Tämä tehtiin kaikilla viidellä eri vahvuus luokilla.
Yleisesti hyväksytty alhaisin [avaimen pituus on 2048 bittiä](https://en.wikipedia.org/wiki/Key_size). Nopean logiikkatestauksen sekä salauksen riippuvuuden avaimen pituudesta hahmottamiseksi valitsin neljä muutakin bitti pituutta salauksen vahvuuden vaihtoehdoiksi. Tässä ei ole laskettu salausta/purkamista koska se on syöte riippuvainen. Joten tämä ajanmittaus on tehty alkulukujen luonnin, validoinnnin ja aivaimien generoimisen perusteella. Saatu aika on 50 suorituskerran keskiarvo.

Keskivertotulokset olivat seuraavanlaiset näillä avaimen pituuksilla:

512:    0.000133s

1024:   0.000551s

2048:   0.001542s

4096:   0.013516s

8192:   0.480271s

## Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
Automaattisiin testeihin on kirjoitettu syötteet valmiiksi niin testaajan ei tarvitse niistä huolehtia. Testien syötteet on ohjelmaa rakentaessa otettuja arvoja joiden oikeenlisuus on varmistettu myös valmiilla algoritmeilla. Esimerkiksi laske_mod_exp() fuktion testaamisessa käytetyt arvot testattiin valmiilla kirjastolla joka tekee saman työn, joten voi luottaa että nämä syötteet on oikeanlaisia. Manuaalisessa järjestelmätestauksessa kirjoitettiin lorem ipsumia salattavaksi viestiksi ja todettiin sen salauksen purkauksen jälkeenkin olevan vielä samassa muodossa.

## Miten testit voidaan toistaa?
Testit voidaan ajaa ylläolevien ohjeiden mukaisesti. 

## Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa
TBA
