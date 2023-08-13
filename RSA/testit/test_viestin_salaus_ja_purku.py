from dekryptaus_enkryptaus import encrypt, decrypt

def test_salaa_oikein_viesti():
    julkinen = 5
    n = 5777
    viesti = 'moikkamoi'
    salainen= 4493

    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert dekryptattu_viesti == viesti

def test_samat_tiedot_listalla_kun_palautetussa_viestissa():
    julkinen = 5
    n = 5777
    viesti = 'moikkamoi'
    salainen= 4493

    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    
    assert ''.join(str(i) for i in palautettu_lista) == palautettu_viesti


def test_salaa_oikein_viestin_vaikka_vaan_numeroita_viestissä():
    julkinen = 5
    n = 5777
    viesti = '123456789'
    salainen= 4493
    
    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert dekryptattu_viesti == viesti

def test_palautettu_viesti_on_salattu_eika_sama_kuin_salaamaton():
    julkinen = 5
    n = 5777
    viesti = '123456789'
    salainen= 4493
    
    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert palautettu_viesti != viesti


def test_ei_pura_oikein_viestia_jos_julkisella_purkaa_viestin():
    julkinen = 5
    n = 5777
    viesti = 'heippahei'
    salainen= 5
    
    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert dekryptattu_viesti != viesti


