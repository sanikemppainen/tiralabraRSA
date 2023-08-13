import random

def loytaa_alkuluvut_erasthoteen_seulalla(n):
    """
    Luo alkulukuja annettuun numeroon n asti.

    Args:
        n(int): tähän numeroon asti luodaan alkulukuja

    Returns:
        alkuluvut(List): palauttaa luodun listan alkuluvuista
    """


    listan_pituus = n + 1
    booleanlista = []
    for i in range(listan_pituus):
        i = True
        booleanlista.append(i)

    # käy läpi jokaisen 2-n luvun potenssi ja vertaa onko se n isompi,
    # skippaa 0 ja 1 koska erasthotheen seula aloittaa aina 2 koska 0 ja 1 ei ole alkulukuja
    for i in range(2, listan_pituus):
        if i * i <= n:
            # jos ei, niin katso onko sen indeksin booleanlistan arvo
            # True (eli ei vielä käsitelty tai arvo jätetty Trueksi)
            if booleanlista[i]:
                # käy läpi kaikki sen luvun kertoimet ja muuta ne Falseksi,
                # ne ei ole alkulukuja
                for i in range(i * i, listan_pituus, i):
                    booleanlista[i] = False

    # käy läpi 2-n luvut ja katso onko se boolean listalla,
    # jos indeksi on True niin lisää alkulukulistalle
    alkuluvut = []
    for i in range(2, listan_pituus):
        if booleanlista[i]:
            alkuluvut.append(i)
    return alkuluvut

def loyda_p_q(alkuluku_lista):
    bits = 1024

    while True:
        luku = random.choice(alkuluku_lista)

        if onko_alkuluku(luku, k=40):
            return luku


def onko_alkuluku(luku, k):
    """Rabin-Millerin alogritmi"""

    if luku == 0 or luku == 1:
        return False
    if luku == 2:
        return True
    if luku % 2 == 0:
        return False
    if luku == 3:
        return True

    y = 0
    d = luku - 1

    for y in range(luku):
        if d % 2 != 0:
            break
        y = y + 1
        d = d // 2

    # loopataan alkulukutarkistusta läpi iteraatiot muuttujan monta kertaa
    for j in range(k):
        # sattumanvarinen luku joka iteraatiolla
        random_number_from_list = random.randint(2, luku - 2)

        # tämä count_mod_exp tekee laskun : random_number_from_list^pariton mod i
        tulos = laske_mod_exp(random_number_from_list, d, luku)

        # jos on 1 tai n-1 niin voi hypätä seuraavaan,
        # sillä silloin tulos on joko 1 tai -1 ja tämän algoritmin mukaan
        # se ei silloin ole ei-alkuluku
        if tulos == 1:
            continue
        if tulos == luku - 1:
            continue

        # sitten käydään läpi
        for j in range(y - 1):
            tulos = laske_mod_exp(tulos, 2, luku)
            # jos missään vaiheessa i == 1 niin sitten sitten se ei ole alkuluku
            if tulos == luku - 1:
                break
        else:
            # jos vikankaan jälkeen ei ole vielä false niin sitten viimeistään
            return False
    return True




#arvotaan randomilla 1024 bittisiä lukuja kunnes on löydetty kaksi alkulukua
#jokainen arvottu luku -> jaetaan kaikilla listassa olevilla alkuluvuilla
#jos joku jako menee tasan -> luku hylätään
# jos luku menee läpi tästä -> testataan miller rabinilla 40 kertaa

def laske_mod_exp(a, b, c):
    """
    Tekee a^b mod c laskun
    """
    tulos = 1
    a %= c
    while b > 0:
        # jos b on pariton niin kerro a tuloksella
        if b & 1:
            tulos = (tulos * a) % c
        a = (a * a) % c
        b >>= 1
    return tulos