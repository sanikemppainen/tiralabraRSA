"""Tiedostosa on viestin dekryptaus ja enkryptaukseen vaadittavat toiminnot"""
from alkulukujen_luonti import laske_mod_exp


def encrypt(julkinen: int, n: int, viesti: str):
    """
    Palauttaa julkisella avaimella salatun viestin
    Args:
        julkinen(int): laskettu eksponentti julkisen avaimen muodostukseen
        n(int): modulo
        viesti(str): annettu viesti joka salataan

    Returns:
        salattu_viesti(str): salattu viesti
        jokainen_merkki_salattu(list): lista jossa jokainen merkki salattuna omassa indeksissä

    """
    jokainen_merkki_salattu = []
    for merkki in viesti:
        merkin_koodi = ord(merkki)
        salattu_merkki = laske_mod_exp(merkin_koodi, julkinen, n)
        jokainen_merkki_salattu.append(salattu_merkki)
    salattu_viesti = "".join(str(i) for i in jokainen_merkki_salattu)
    return salattu_viesti, jokainen_merkki_salattu


def decrypt(salainen: int, n: int, viesti: str):
    """
    Palauttaa salatulla avaimella puretun viestin
    Args:
        salainen(int): laskett eksponentti salaisen avaimen muodostukseen
        n(int): modulo
        viesti(str): annettu viesti jonka salaus puretaan

    Returns:
        salattu_viesti(str): viesti josta on purettu salaus
    """
    jokainen_merkki_purettu = []

    for merkki in viesti:
        purettu_merkki = laske_mod_exp(merkki, salainen, n)
        chr_merkki = chr(purettu_merkki)
        jokainen_merkki_purettu.append(chr_merkki)
    purettu_viesti = "".join(str(i) for i in jokainen_merkki_purettu)
    return purettu_viesti
