sozluk={"apple":"elma","honor":"fenerbahce","cat":"kedi","strawberry":"cilek","orange":"portakal"}
kelime=sozluk["orange"]
#eger sozlukte olmayan bir şey yazsaydım hata alırıdm
kelime=sozluk.get("orange")
print(kelime) #değer yoksa none çıkar
#eleman eklemek için
sozluk["rose"]="gul"
#elemanı değiştirmek istersen
sozluk["apple"]="eksi elma"
#eleman silme
del sozluk["apple"]
#sozlugu temizlemek icin
sozluk.clear()
#elemanları listelemek için
sozluk={"apple":"elma","honor":"fenerbahce","cat":"kedi","strawberry":"cilek","orange":"portakal"}
for i in sozluk:
    print("İngilizcesi:",i,"Turkcesi",sozluk[i])
#item anahtar ve değerlerine aynı anda ulaşılmasını sağlar
sozluk={"apple":"elma","honor":"fenerbahce","cat":"kedi","strawberry":"cilek","orange":"portakal"}
print(sozluk.items())
#dict_items([('apple', 'elma'), ('honor', 'fenerbahce'), ('cat', 'kedi'), ('strawberry', 'cilek'), ('orange', 'portakal')])
#for döngüsü ile yapmak istersek
for anahtar,deger in sozluk.items():
    print("Anahtar",anahtar,"Deger:",deger)
    #key ile anahtara ulaşırsın
print("***************************************")
for anahtar in sozluk.keys(): print(anahtar)
#value ile değerine
for deger in sozluk.values(): print(deger)
#Not! sözcük elemanları rastgele listelenir bu yüzden her çalıştığında farklı çalışması normaldir
#eleman sayısını bulmak için len kullanılır

print("Sozlugun Eleman Sayısı:",len(sozluk))
#anahtar varlığı kontrol etme
print("orange" in sozluk) #true
print("rat" not in sozluk)#true
#ürün güncelleme
urun={"kalem":2,"defter":4,"makas":5}
yeni={"kalem":25,"defter":41,"makas":123}

urun.update(yeni)
print(yeni)
#sikmek için
urun.clear()
#kopyalamak için idleri aynı oldu
yeni=urun
print(id(urun))
print(id(yeni))
#Not! eğer copy fonksiyonu kullanırsak bellek adresleri eşitlenmez sadece değerin ikinci bir kopyası oluştulur