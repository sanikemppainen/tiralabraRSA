"""Main"""
import avain_generaattori
import dekryptaus_enkryptaus
import alkulukujen_luonti
import time

if __name__ == "__main__":
    print("--------------RSA-salaus-------------------")
    print("Tervetuloa salaamaan viesti!")
    print("Syötä joku seuraavista numeroista valitaksesi salauksen vahvuuden:")
    print(
        "1: Heikko salaus, 2:Kohtalainen salaus, 3: Suositeltu salaus vahvuus, 4:Vahvempi salaus, 5:Vahva salaus"
    )
    vahvuus = input("")
    print("Valittu vahvuus: ", vahvuus)
    if vahvuus == "1":
        bitti_pituus = 512
    if vahvuus == "2":
        bitti_pituus = 1024
    if vahvuus == "3":
        bitti_pituus = 2048
    if vahvuus == "4":
        bitti_pituus = 4096
    if vahvuus == "5":
        bitti_pituus = 8192

    for i in range(50):
        alkuaika = time.time()
        alkuluku_lista = alkulukujen_luonti.loytaa_alkuluvut_erasthoteen_seulalla(500)
        p = alkulukujen_luonti.loyda_p_q(alkuluku_lista, (bitti_pituus // 2))
        q = alkulukujen_luonti.loyda_p_q(alkuluku_lista, (bitti_pituus // 2))
        julkinen_avain, salainen_avain, n = avain_generaattori.generoi_avaimet(p, q)
        loppuaika = time.time()
        aika = loppuaika - alkuaika
    print("keskivertoaika: ", aika / 50)
    str_viesti = input("Anna viesti salattavaksi:")
    enkryptattu_viesti, array = dekryptaus_enkryptaus.encrypt(
        julkinen_avain, n, str_viesti
    )
    print("Tässä on salattu viesti: ", enkryptattu_viesti)
    dekryptattu_viesti = dekryptaus_enkryptaus.decrypt(salainen_avain, n, array)
    print("Tässä purettu viesti: ", dekryptattu_viesti)
    print("Aikaa salaukseen kului: ", loppuaika - alkuaika)
    print("-------------------------------------------")
