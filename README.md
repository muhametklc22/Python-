# Keylogger Projesi

Bu proje, Python kullanarak basit bir keylogger oluşturmayı amaçlar. Keylogger, kullanıcının klavyesinde bastığı tuşları kaydeder ve belirli aralıklarla kayıt dosyasını e-posta yoluyla gönderir. Bu örnek, eğitim amaçlı hazırlanmış olup yalnızca yasal kullanım içindir.

## Proje Açıklaması

Keylogger, kullanıcının klavye girişlerini "keylogger.txt" adlı bir dosyaya kaydeder. Aynı zamanda bu dosyanın içeriğini, tanımlanmış bir e-posta adresine gönderebilir. **Not:** Bu kodu kullanırken etik kurallara dikkat edilmelidir ve yalnızca izinli ortamda çalıştırılmalıdır.

## Özellikler

- Klavyede basılan tüm tuşları "keylogger.txt" dosyasına kaydeder.
- E-posta gönderimi ile kayıt dosyasını belirli bir e-posta adresine iletir.
- Python'un `smtplib`, `ssl` ve `pynput` modüllerini kullanır.

## Gereksinimler

Bu keylogger aşağıdaki Python kütüphanelerini kullanır:

- `smtplib`: SMTP sunucuları ile iletişim kurmak için kullanılır.
- `ssl`: Güvenli veri aktarımı için SSL/TLS protokolünü sağlar.
- `pynput`: Klavye girişlerini izlemek için kullanılır.

**Kurulum**: Aşağıdaki komut ile gerekli kütüphaneyi yükleyebilirsiniz:
```bash
pip install pynput
E-posta Bilgileri : Kodda sender_mail, receiver_mail ve password alanlarına kendi e-posta bilgilerinizi ekleyin.

sender_mail = "user@domain.com"
receiver_mail = "user@domain.com"
password = "passcode"

Not : E-posta gönderimi için Gmail kullanılıyorsa, iki faktörlü doğrulama kapatılmalı ve "Uygulama Şifreleri" oluşturulmalıdır.

Keylogger’ı Çalıştırma: Terminali açın ve aşağıdaki komutu girin:

python keylogger.py

Çıkış Yapma : Keylogger'ı durdurmak için Esc tuşuna basabilirsiniz. 
