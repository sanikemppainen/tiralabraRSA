from create_keys import loytaa_alkuluvut_erasthoteen_seulalla, tarkistaa_alkuluvut_miller_rabin_algoritmilla

#TODO tesktikäyttöliittymä joka kysyy inputtia konsolista 
    #onko kyseessä decrypt vai encrypt

def main():
    #encrypt: 

    #str_viesti = input()
    #b64_viesti = decode_viesti(str_viesti)
        #b64 formaattiin
    #int_viesti = b64_to_int(b64_viesti)

    #ITSE SALAUS:
    #tee alkuluvut
    alkuluvut = loytaa_alkuluvut_erasthoteen_seulalla()
    #500 pienimmällä tuotetulla alkuvulla alkukarsinta 
    karsittu_lista = tarkistaa_alkuluvut_miller_rabin_algoritmilla(alkuluvut, 500)
    #luo avaimet
    #salaa viesti avaimilla
    #palauta salattu viesti

    #decrypt:
