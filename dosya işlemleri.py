#r kullanmak istemiyorsak "/" kullanırız "\" yerine
# open(r"C:\Users\user\Desktop\phytondenemedosyası\deneme1.txt", #mod #r,w,a bunlardan biri olmalı))

dosya=open("deneme1.txt",mode="w")
dosya.write("merhaba\n")
dosya.write("selamlar\n")
dosya.write("ben\n")
dosya.write("phyton ögreniyorum\n")
dosya.close()
#w mevcut içeriği silip üzerine yazar fakat a kullanmak dosyayıy klaan verilerden üzerinden veri ekleyebilirsin

dosya=open("deneme1.txt",mode="a")
dosya.write("merhaba hayat\n")
dosya.close()
#dosya okuma
dosya=open(r"C:\Users\user\Desktop\phytondenemedosyası\deneme1.txt",mode="r")
print(dosya.read())
dosya.close()
#satır satır okuma dersek
dosya=open(r"C:\Users\user\Desktop\phytondenemedosyası\deneme1.txt",mode="r")
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
print(dosya.readline())
dosya.close()
dosya=open(r"C:\Users\user\Desktop\phytondenemedosyası\deneme1.txt",mode="r")
satir=dosya.readlines()
for s in satir:
    print(s)