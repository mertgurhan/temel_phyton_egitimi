# Mantık Hatası(LogicError)
#Söz dizimsel Haya(Syntax Error)
#hata olma ihtimallerini try bloğu içerisine yazıyoruz
from döngüler import sicaklik

try:
    a=int(input("İlk sayiyi giriniz"))
    b=int(input("İkinci sayiyi giriniz"))
    sonuc=a/b
    print(int(sonuc))
    liste=[12,43,12,43,77,987,4]
    print(liste[a])
except ValueError:
    print("Bir hata ile karşılaşıldı sayi değil!")
except ZeroDivisionError:
    print("Bölen sıfır olamaz")

except:
    print("Beklenmeyen Hata oluştu")

    #FINALLY her zaman çalışır ister hata olsun ister olmasın
try:
    a=int(input("İlk sayiyi giriniz"))
    b=int(input("İkinci sayiyi giriniz"))
    sonuc=a/b
except ValueError:
    print("Girilen deger bir sayi değil")
except ZeroDivisionError:
    print("Sıfır bölen olamaz!")
finally:
    print("Program sonlandı")
    #Hata tanımlama raise
    a=int(input("Bir sayi girinz"))
    if a>100:
        raise Exception("Girilen değer 100 den büyük olamaz!")
    #veya genelde  olabilir
    a = int(input("Bir sayi girinz"))
    if a > 100:
        raise OverflowError("Girilen değer 100 den büyük olamaz!")
    #ASSERT
    # Bizim istediğimiz iddaları kabul eden ama farklı bir şey istediğimizi söylediğimizde iste sroun yaşadığımız durumlardır
    print("Programın açılması için lütfen gerekli bilgileri giriniz")
    kullanici=input("Kullanıcı Adınızı giriniz")
    assert kullanici=="mert"
    sifre=int(input("Şifrenizi giriniz"))
    assert sifre=="123"
    print("Programa hos geldiniz")
    #başka bir şeyle giriş yapmaya çalıştığımızda ise AssertionError hatası alacağız!

    sicaklik=int(input("Hava kaç derece?"))
    assert sicaklik>=20,"Hava sıcak"
    print("Güzel bir gün")
