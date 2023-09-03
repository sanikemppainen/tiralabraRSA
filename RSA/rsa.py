"""Main"""
import avain_generaattori
import dekryptaus_enkryptaus
import alkulukujen_luonti
import time
import sys

if __name__ == "__main__":
    print("--------------RSA-salaus-------------------")
    print("Tervetuloa salaamaan viesti!")
    while True:
        print("Syötä joku seuraavista numeroista valitaksesi salauksen vahvuuden:")
        print(
            "1: Heikko salaus, 2:Kohtalainen salaus, 3: Suositeltu salaus vahvuus, 4:Vahvempi salaus, 5:Vahva salaus tai 0:Sulje ohjelma"
        )
        vahvuus = input("")
        bitti_pituus = 0
        if vahvuus == "1":
            bitti_pituus = 512
            break
        if vahvuus == "2":
            bitti_pituus = 1024
            break
        if vahvuus == "3":
            bitti_pituus = 2048
            break
        if vahvuus == "4":
            bitti_pituus = 4096
            break
        if vahvuus == "5":
            bitti_pituus = 8192
            break
        if vahvuus == "0":
            print("Suljetaan ohjelma")
            sys.exit(0)
        else:
            print(
                "Syötetty numero oli väärin, syötä joku näistä: 1, 2, 3, 4 tai 5 valitatksesi vahvuuden tai 0 sulkeaksi ohjelman"
            )
    print("Odotathan kunnes sinulta kysytään syötettä")
    try:
        alkuaika = time.time()
        alkuluku_lista = alkulukujen_luonti.loytaa_alkuluvut_erasthoteen_seulalla(500)
        p = alkulukujen_luonti.loyda_p_q(alkuluku_lista, (bitti_pituus))
        q = alkulukujen_luonti.loyda_p_q(alkuluku_lista, (bitti_pituus))
        julkinen_avain, salainen_avain, n = avain_generaattori.generoi_avaimet(p, q)
        loppuaika = time.time()
        aika = loppuaika - alkuaika

        str_viesti = input("Anna viesti salattavaksi:")
        enkryptattu_viesti, array = dekryptaus_enkryptaus.encrypt(
            julkinen_avain, n, str_viesti
        )
        print("Tässä on salattu viesti: ", enkryptattu_viesti)
        dekryptattu_viesti = dekryptaus_enkryptaus.decrypt(salainen_avain, n, array)
        print("Tässä purettu viesti: ", dekryptattu_viesti)
        print("Aikaa salaukseen kului: ", loppuaika - alkuaika)
        print("-------------------------------------------")

    except:
        print("Jokin meni pieleen..... Aloita alusta!")
