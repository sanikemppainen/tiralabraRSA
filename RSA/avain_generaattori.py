"""Avaimien generointiin tarvittavat funktiot"""


def generoi_avaimet(p, q):
    """
    Generoi avaimet annettujen isojen alkulukujen p ja q avulla.
    Laskee moduluksen eli n
    Laskee totientin eli t
    Näiden avulla laske julkisen
    Näiden avulla laskee salaisen

    Itse avaimet koostuvat aina julkinen tai salainen + n osista

    Args:
        p(int): iso alkuluku
        q(int): iso alkuluku

    Returns:
        julkinen(int): generoitu julkinen avain
        salainen(int): generoitu salainen avain
        n(int): modulus

    """

    n = p * q

    t = (p - 1) * (q - 1)

    julkinen_exponentti = 65537

    # julkinen
    if loyda_isoin_yhteinen_jakaja(julkinen_exponentti, t) == 1:
        julkinen = julkinen_exponentti
    # salainen
    salainen = laske_mod_kaanteis(julkinen, t)

    return julkinen, salainen, n


def loyda_isoin_yhteinen_jakaja(julkinen_exponentti, t):
    """
    Euclidin algoritmilla etsitään isoin yhteinen jakaja.
    Kutsuu metodia rekursiivisesti kunnes t on 0.
    Args:
        i(int): läpikäytävä luku
        t(int): totient

    Returns:
        i(int): isoin yhteinen jakaja
    """
    while t:
        julkinen_exponentti, t = t, julkinen_exponentti % t
    return julkinen_exponentti


def laske_mod_kaanteis(julkinen, t):
    """
    Laske kaanteisluku modulaarisesti että saadaan salainen avain muodostettua
    Args:
        julkinen(int): julkinen eksponentti
        t(int): totient

    """

    def laajempi_yhteisen_jakajan_etsiminen(a, b):
        # nolla on erikoistapaus
        if a == 0:
            return b, 0, 1
        g, x, y = laajempi_yhteisen_jakajan_etsiminen((b % a), a)
        return g, (y - (b // a) * x), x

    g, x, y = laajempi_yhteisen_jakajan_etsiminen(julkinen, t)
    if g != 1:
        # aina pitäisi olla
        print("lukua ei olemassa")
    return x % t
