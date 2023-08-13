from alkulukujen_luonti import loytaa_alkuluvut_erasthoteen_seulalla, loyda_p_q, onko_alkuluku, laske_mod_exp

def test_loytaa_alkuluvut_erasthoteen_seulalla():
    n = 100
    varmasti_alkuluvut = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    alkuluvut = loytaa_alkuluvut_erasthoteen_seulalla(n)
    assert alkuluvut == varmasti_alkuluvut

def test_ei_loyda_ei_alkulukuja():
    n = 50
    yksi_ylimaarainen_ei_alkuluku= [2, 3, 5, 6, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    alkuluvut = loytaa_alkuluvut_erasthoteen_seulalla(n)
    assert alkuluvut != yksi_ylimaarainen_ei_alkuluku
    assert 6 not in alkuluvut

def test_palauttaa_oikeanlaiset_p_ja_q():
    alkuluku_lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    p_tai_q = loyda_p_q(alkuluku_lista)
    assert onko_alkuluku(p_tai_q, 40)

def test_ei_ole_alkuluku_nollalla():
    luku = 0
    assert onko_alkuluku(luku, 40) == False

def test_ei_ole_alkuluku_ykkosella():
    luku = 1
    assert onko_alkuluku(luku, 40) == False

def test_on_alkuluku_kakkosella():
    luku = 2
    assert onko_alkuluku(luku, 40) == True

def test_ei_ole_alkuluku_parillisilla_luvuilla():
    luku = 8
    assert onko_alkuluku(luku, 40) == False

def test_kolmonen_on_alkuluku():
    luku = 3
    assert onko_alkuluku(luku, 40) == True

def test_tunnetulla_isolla_alkuluvulla():
    luku = 5167
    assert onko_alkuluku(luku, 40) == True

def test_tunnetulla_isolla_ei_alkuluvulla():
    luku = 5168
    assert onko_alkuluku(luku, 40) == False

def test_mod_exp_laskeminen_menee_oikein():
    assert laske_mod_exp(7, 1, 13) == 7

def test_mod_exp_laskeminen_menee_oikein_testaa_if_lausetta_b_on_pariton():
    assert laske_mod_exp(2, 5, 7) == 4