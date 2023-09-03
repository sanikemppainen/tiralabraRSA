from dekryptaus_enkryptaus import encrypt, decrypt


def test_salaa_oikein_viesti():
    julkinen = 5
    n = 5777
    viesti = "moikkamoi"
    salainen = 4493

    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert dekryptattu_viesti == viesti


def test_samat_tiedot_listalla_kun_palautetussa_viestissa():
    julkinen = 5
    n = 5777
    viesti = "moikkamoi"
    salainen = 4493

    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)

    assert "".join(str(i) for i in palautettu_lista) == palautettu_viesti


def test_salaa_oikein_viestin_vaikka_vaan_numeroita_viestissä():
    julkinen = 5
    n = 5777
    viesti = "123456789"
    salainen = 4493

    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert dekryptattu_viesti == viesti


def test_palautettu_viesti_on_salattu_eika_sama_kuin_salaamaton():
    julkinen = 5
    n = 5777
    viesti = "123456789"
    salainen = 4493

    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert palautettu_viesti != viesti


def test_ei_pura_oikein_viestia_jos_julkisella_purkaa_viestin():
    julkinen = 5
    n = 5777
    viesti = "heippahei"
    salainen = 5

    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert dekryptattu_viesti != viesti


def test_isommmalla_avaimella_viestin_salaus_onnistuu():
    julkinen = 65537
    salainen = 1039441634754404919252550018622199493660015979636068622724301737793945979237613415334468513905445099544022487295673297763697467693667738886420980735477371914282615852136916823355568677382028886487120967741305971826181917537266442968425758239474061264119882789733041052105890364426809967810940325322504202949
    n = 50799318729977207451942110790785300683069699669954533428398630119166172737729657271271486201208915353330799216925086439626727024787399405965228795272916138899721095490050543901809875548033775131113777847677933310123246047146943086611174797456940611891578893648605796634323183001146165776811751789520459032521

    viesti = "moikkamoihei"

    palautettu_viesti, palautettu_lista = encrypt(julkinen, n, viesti)
    dekryptattu_viesti = decrypt(salainen, n, palautettu_lista)

    assert dekryptattu_viesti == viesti
