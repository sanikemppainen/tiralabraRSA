"""Luo alkuluvut ja tarkistaa niiden oikeellisuuden"""
import random

#miller-rabinin seula
def tarkistaa_alkuluvut_miller_rabin_algoritmilla(alkuluvut, iteraatiot):
    """
    Tarkistaa onko alkuluvut listalla todennäköisesti oikeasti alkulukuja. Iteraatiot arvoa kasvattamalla tämä algoritmi ajetaan useempaan kertaan, 
    tehden tästä varmemman sillä algoritmi on todennäköisyysperustainen ja voi antaa vääriä positiivisa väittämiä alkuluvusta. 
    Mutta jos se ajetaan moneen kertaan, niin todennäköisyys virheille laskee.

    Args:
        alkuluvut(List): annettu alkulukulista joka käydään läpi
        iteraatiot(int): monesti algoritmi käydään läpi

    Returns:
        tarkistetut_alkuluvut(List): palauttaa luodun listan tarkistetuista alkuluvuista
    """
    tarkistetut_alkuluvut = []
    for i in alkuluvut:
        if on_todennakoisesti_alkuluku(i, len(alkuluvut), iteraatiot):
            tarkistetut_alkuluvut.append(i)
    return tarkistetut_alkuluvut

def on_todennakoisesti_alkuluku(i, listanpituus, iteraatiot):
    """
    Itse Miller-rabin algoritmin käyttäminen jokaisen alkuluvun tarkistukseen.
    Alkuluku on lukua 1 suurempi luonnollinen luku, joka ei ole jaollinen muilla positiivisilla kokonaisluvuilla kuin yhdellä ja itsellään. 2 on ainut parillinen alkuluku. 

    Args:
        i(int): alkuluku ehdokas
    
    Returns:
        onko_alkuluku(boolean): True jos on todnäk alkuluku, False jos ei 
    """
    # 0 ja 1 ei ole alkulukuja
    if i == 0 or i == 1:
        return False
    # 2 jaolliset ei ole alkulukuja, paitsi 2
    if i == 2:
        return True
    if i % 2 == 0:
        return False

    #entä 3? sekin pitää laittaa trueksi heti alussa, muuten iteraation mukainen looppaus ei toimi (se ei katso 3, alottaa 4)
    if i == 3:
        return True

    #käy lukua läpi ja jaa sitä 2 kunnes tulee pariton luku, tätä tarvii myöhemmmin
    y = 0
    pariton = listanpituus - 1

    for y in range(listanpituus):
        if pariton % 2 != 0:
            break
        y = y+1
        pariton = pariton // 2

    #loopataan alkulukutarkistusta läpi iteraatiot muuttujan monta kertaa
    for k in range(iteraatiot):
        #sattumanvarinen luku joka iteraatiolla
        random_number_from_list = random.randint(2, i-2)
        
        #tämä count_mod_exp tekee laskun : random_number_from_list^pariton mod i 
        tulos = count_mod_exp(random_number_from_list, pariton, i)
        
        # jos on 1 tai n-1 niin voi hypätä seuraavaan, sillä silloin tulos on joko 1 tai -1 ja tämän algoritmin mukaan se ei silloin ole ei-alkuluku
        if tulos == 1:
            continue
        if tulos == i -1:
            continue
        
        #sitten käydään läpi 
        for j in range(y-1):
            tulos = count_mod_exp(tulos, 2, i)
            # jos missään vaiheessa i == 1 niin sitten sitten se ei ole alkuluku
            if tulos == i-1:
                break
        else:
            #jos vikankaan jälkeen ei ole vielä false niin sitten viimeistään
            return False
        #jos tuo algoritmi ei ole laittanut i falseksi niin sitten i on luultavaksi alkuluku ja palautetaan True
    return True


def count_mod_exp(a,b,c):
    """
    Tekee a^b mod c laskun
    """
    tulos = 1
    a %= c
    while b > 0:
        #jos b on pariton niin kerro a tuloksella
        if b & 1:
            tulos = (tulos*a) % c
        a = (a*a) % c
        b >>= 1
    return tulos

#erastotheen seula
def loytaa_alkuluvut_erasthoteen_seulalla(n):
    """
    Luo alkulukuja annettuun numeroon n asti.
   
    Args:
        n(int): tähän numeroon asti luodaan alkulukuja

    Returns:
        alkuluvut(List): palauttaa luodun listan alkuluvuista
    """
    #luo listan jossa arvo = True jokaisella indeksillä
    listan_pituus = n+1
    booleanlista = []
    for i in range(listan_pituus):
        i = True
        booleanlista.append(i)

    #käy läpi jokaisen 2-n luvun potenssi ja vertaa onko se n isompi, skippaa 0 ja 1 koska erasthotheen seula aloittaa aina 2 koska 0 ja 1 ei ole alkulukuja
    for i in range(2, listan_pituus):
        if i * i <= n:
            #jos ei, niin katso onko sen indeksin booleanlistan arvo True (eli ei vielä käsitelty tai arvo jätetty Trueksi)
            if booleanlista[i]:
                #käy läpi kaikki sen luvun kertoimet ja muuta ne Falseksi, ne ei ole alkulukuja
                for i in range(i*i, listan_pituus, i):
                    booleanlista[i] = False
    
    #käy läpi 2-n luvut ja katso onko se boolean listalla, jos indeksi on True niin lisää alkulukulistalle
    alkuluvut = []
    for i in range(2, listan_pituus):
        if booleanlista[i]:
            alkuluvut.append(i)
    return alkuluvut

print(loytaa_alkuluvut_erasthoteen_seulalla(500))
alkuluvut = loytaa_alkuluvut_erasthoteen_seulalla(500)
tarkistetut_alkuluvut = tarkistaa_alkuluvut_miller_rabin_algoritmilla(alkuluvut, 10)