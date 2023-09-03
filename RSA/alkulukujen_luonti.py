"""Luodaan alkuluvut, niiden tarkistus ja p + q valinta"""
import random


def loytaa_alkuluvut_erasthoteen_seulalla(n):
    """
    Luo alkulukuja annettuun numeroon n asti. Käyttää Erastotheenen seulaa.

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
    for i in range(2, listan_pituus):
        if i * i <= n:
            if booleanlista[i]:
                for i in range(i * i, listan_pituus, i):
                    booleanlista[i] = False
    alkuluvut = []
    for i in range(2, listan_pituus):
        if booleanlista[i]:
            alkuluvut.append(i)
    return alkuluvut


def loyda_p_q(alkuluku_lista, bitti_pituus):
    """
    Valitaan p tai q
    Args:
        alkuluku_lista(list): lista alkuluvuista

    Returns:<
        luku(int): p tai q
    """
    n = bitti_pituus // 2
    while True:
        luku = random.getrandbits(n)
        if onko_alkuluku(luku, 40, alkuluku_lista):
            break
    return luku


def onko_alkuluku(luku, k, alkuluku_lista):
    """
    Rabin-Millerin alogritmi
    Args:
        luku(int): käsiteltävä luku
        k(int): monestikko käydään tämä läpi

    Returns:
        True tai False(boolean): True tai false sen perusteella onko alkuluku
    """

    if luku == 0 or luku == 1:
        return False
    if luku == 2:
        return True
    if luku % 2 == 0:
        return False
    if luku == 3:
        return True

    for luku_listalta in alkuluku_lista:
        if luku % luku_listalta == 0:
            return False

    y = 0
    d = luku - 1

    for y in range(luku):
        if d % 2 != 0:
            break
        y = y + 1
        d = d // 2

    for j in range(k):
        random_number_from_list = random.randint(2, luku - 2)

        tulos = laske_mod_exp(random_number_from_list, d, luku)

        if tulos == 1:
            continue
        if tulos == luku - 1:
            continue

        for j in range(y - 1):
            tulos = laske_mod_exp(tulos, 2, luku)
            if tulos == luku - 1:
                break
        else:
            return False
    return True


def laske_mod_exp(a, b, c):
    """
    Tekee a^b mod c laskun

    Args:
        a(int):
        b(int):
        c(int):

    Returns:
        tulos(int): a^b mod c laskutoimituksen tulos

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
