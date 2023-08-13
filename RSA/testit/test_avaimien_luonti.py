from avain_generaattori import generoi_avaimet, loyda_isoin_yhteinen_jakaja, laske_mod_kaanteis

def test_generoi_avaimet_jotka_ei_ole_nolla():
    p = 56
    q = 53
    julkinen, salainen, n = generoi_avaimet(p, q)
    assert julkinen != 0
    assert salainen != 0

def test_generoi_avaimet_jotka_ei_ole_negatiivisia():
    p = 101
    q = 137
    julkinen, salainen, n = generoi_avaimet(p, q)
    assert julkinen > 0
    assert salainen > 0


def test_generoi_eri_avaimet():
    p = 131
    q = 103
    julkinen, salainen, n = generoi_avaimet(p, q)
    assert julkinen != salainen

def test_loyda_isoin_yhteinen_jakaja():
    i=60
    t=48
    assert loyda_isoin_yhteinen_jakaja(i, t) == 12

def test_loyda_isoin_yhteinen_jakaja_jos_on_vain_1():
    i=17
    t=5
    assert loyda_isoin_yhteinen_jakaja(i, t) == 1

def test_laske_mod_kaanteis_onnistuneesti():
    julkinen = 7 
    t = 40
    assert laske_mod_kaanteis(julkinen, t) == 23