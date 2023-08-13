"""Main"""
import avain_generaattori
import dekryptaus_enkryptaus
import alkulukujen_luonti

if __name__ == "__main__":
    # lasketaan eka lista täyteen alkulukuja erasthotheenen seulalla
    alkuluku_lista = alkulukujen_luonti.loytaa_alkuluvut_erasthoteen_seulalla(500)

    # arvotaan randomilla 1024 bittisiä lukuja kunnes on löydetty kaksi alkulukua
    # jokainen arvottu luku -> jaetaan kaikilla listassa olevilla alkuluvuilla
    # jos joku jako menee tasan -> luku hylätään
    # jos luku menee läpi tästä -> testataan miller rabinilla 40 kertaa
    p = alkulukujen_luonti.loyda_p_q(alkuluku_lista)
    q = alkulukujen_luonti.loyda_p_q(alkuluku_lista)

    julkinen_avain, salainen_avain, n = avain_generaattori.generoi_avaimet(p, q)

    str_viesti = input("Anna vieti salattavaksi:")

    enkryptattu_viesti, array = dekryptaus_enkryptaus.encrypt(
        julkinen_avain, n, str_viesti
    )
    print("Tässä on salattu viesti: ", enkryptattu_viesti)
    dekryptattu_viesti = dekryptaus_enkryptaus.decrypt(salainen_avain, n, array)
    print("Tässä purettu viesti: ", dekryptattu_viesti)
