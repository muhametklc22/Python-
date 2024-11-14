# Python ile RSA algoritması uygulaması
# Sayılar teorisi ve kriptografi öğrendiğim üniversitemdeki Ayrık Yapılar dersinden ilham aldım.

# Çalıştırmak için: Kopyalanmış deponun kök dizininde Terminal'i açın, "python RSA_Algorithm/RSA_Python.py" yazın. Enter'a basın.

import math
from pprint import pprint
from string import ascii_lowercase

# Karakterlerin sayısal karşılıkları
kodlama = {c: ascii_lowercase.index(c) + 1 for c in ascii_lowercase}
kodlama[" "] = 27


def genisletilmis_oklid(a, b):
    # (d,x,y) döndürür, öyle ki a*x + b*y = d = gcd(a,b)
    # x ve y Bezout katsayılarıdır
    # Genisletilmiş Öklid algoritmasının özyinelemeli versiyonunu uygular
    if a == 0:
        return b, 0, 1  # Temel durum, çünkü 0*0 + b*1 = 1

    # Euclid Teoremi ve özyineleme ile
    d, x1, y1 = genisletilmis_oklid(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return d, x, y


def genisletilmis_oklid_iteratif(a, b):
    # Yukarıdaki işlemin özyinelemesiz hali

    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, a, b = math.floor(b / a), b % a, a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1

    return b, x0, y0


def mod_alma_tersi(a, m):
    if genisletilmis_oklid(a, m)[0] != 1:
        return "Ters mod yok"
    _, inv_a, _ = genisletilmis_oklid(a, m)
    if inv_a < 0:
        return (inv_a + m)
    return inv_a


def rsa_acik_ozel_anahtarlar(p, q):
    uygun_e_bulundu = False
    e = 2
    while not uygun_e_bulundu and e < (p - 1) * (q - 1):
        g, _, _ = genisletilmis_oklid(e, (p - 1) * (q - 1))
        if g == 1:
            uygun_e_bulundu = True
        else:
            e += 1

    d = mod_alma_tersi(e, (p - 1) * (q - 1))
    return (e, d)


def rsa_sifrele(mesaj, n, e):
    C = mesaj ** e % n
    return C


def rsa_sifre_coz(sifreli, n, d):
    mesaj = sifreli ** d % n
    return mesaj


def kodla(mesaj):
    kodlanmis = ""
    for c in mesaj:
        i = kodlama[c]
        if i < 10:
            kodlanmis += "0" + str(i)
        else:
            kodlanmis += str(i)
    return int(kodlanmis)


def kod_coz(int_mesaj):
    s_mesaj = str(int_mesaj)
    cozulmus = ""
    i = 0
    if len(s_mesaj) % 2 != 0:
        s_mesaj = "0" + s_mesaj
    while i < len(s_mesaj):
        int_c = int(s_mesaj[i] + s_mesaj[i + 1])
        for k, v in kodlama.items():
            if v == int_c:
                cozulmus += k
        i += 2
    return cozulmus


def asal_mi(n, verbose=False):
    eleme = sorted(list(range(2, math.floor(math.sqrt(n)) + 1)))
    eleme_boyutu = len(eleme)
    while eleme_boyutu > 0:
        i = eleme.pop(0)
        if n % i == 0 and i != n:
            if verbose:
                print("%s, %s'nin katıdır" % (n, i))
            return False
        else:
            i_icin_katlar = [k for k in eleme if k % i == 0]
            eleme = sorted([x for x in eleme if x not in i_icin_katlar])
            eleme_boyutu = len(eleme)
    if verbose:
        print("%s asaldır" % n)
    return True


def sinirdan_kucuk_buyuk_asal_uret(ust_sinir):
    for i in sorted(range(2, ust_sinir), reverse=True):
        if asal_mi(i, False):
            return i
    return "Aralıkta asal bulunamadı"


def rsa_ile_eglen(ust_sinir, mesaj):
    p = sinirdan_kucuk_buyuk_asal_uret(ust_sinir)
    q = sinirdan_kucuk_buyuk_asal_uret(p)
    e, d = rsa_acik_ozel_anahtarlar(p, q)
    n = p * q

    kodlanmis = kodla(mesaj)
    if kodlanmis > n:
        pprint((mesaj, kodlanmis))
        mesajlar = kucuk_mesajlara_ayir(kodlanmis, n)
        for kodlanmis_i in mesajlar:
            sifreli_i = rsa_sifrele(kodlanmis_i, n, e)
            cozulmus_i = rsa_sifre_coz(sifreli_i, n, d)
            cozulmus_mesaj = kod_coz(cozulmus_i)
            pprint((kodlanmis_i, sifreli_i, cozulmus_i, cozulmus_mesaj))


def kucuk_mesajlara_ayir(mesaj, n):
    mesaj_uzunlugu = len(str(mesaj))
    rakam_sayisi = len(str(n))
    mesajlar = []
    if rakam_sayisi > 2:
        mesaj_boyutu = max([i for i in range(rakam_sayisi) if i % 2 == 0])
        mesaj_sayisi = math.ceil(mesaj_uzunlugu / mesaj_boyutu)
        for i in range(0, mesaj_sayisi):
            mesaj_i = ""
            for c in range(i * mesaj_boyutu, (i + 1) * mesaj_boyutu):
                if c < mesaj_uzunlugu:
                    mesaj_i += str(mesaj)[c]
            mesajlar.append(int(mesaj_i))
    return mesajlar


rsa_ile_eglen(1000, "julie ekmek yiyor")
