from döngüler import enbuyuk

liste=[30,412,53]
print(liste)

#liste eleman sayısı bulma len
liste=[12,34,65,43]
print(len(liste))

liste=[12,34,65,43]
for i in range(len(liste)):
    print(liste[i])

#liste parçalama 2 şer 2 şer atlıyor
liste2=[50,60,70,80,90,100]
print(liste2[1:5:2])
#liste eleman değiştirme 70 değeri 1 oluır
liste=[50,60,70,80,90,100]
liste[2]=1
print(liste)
#liste birleştirme
yeniliste=liste+liste2
print(yeniliste)
#listeden eleman silme
yeniliste.remove(100)
print(yeniliste)
#true veya false döndürür
liste=[10,20,30]
sonuc=10 in liste
print(sonuc)
#///////////////
liste=[10,20,30]
sonuc=10 not in liste
print(sonuc)
#indis numarasını bulma
liste=[10,20,30,54,20,54]
sonuc=liste.index(20) #eğer (20,2) yaparsak 2.indisten başlayacak ve çıkan indis değeri 4 çıkacak çünkü diğer 20 yi görücek
print(sonuc)
#liste kopyalama
liste=[32,432,541,123,54]
liste2=[12,32,553,123,543]
liste2=liste
print(liste2)
#aynı idde saklanması yani aynı bellekte saklanmasını göstermek için id kullanırız
print(id(liste))
print(id(liste2))

#liste sıralamak için hazır fonksiyon kullanılabilir sort
liste=[12,34,654,132]
liste.sort()
print(liste)
#büyükten küçüğe sıralar ayrıca harfleri a dan z göre sıralar
#tersten sıralar
liste=[12,34,654,132]
liste.reverse()
print(liste)
#tekrar eden sayıyı bulmak için count kullanır 2 nin kaç kez tekrar ettiğini bulur
liste=[12,34,654,132,14,12,12,1233]
k=liste.count(12)
print(k)
#liste üretme
liste=[ a for a  in range(5)]
print(liste)
#TUPLE (DEMETLER) NOT!LİSTEDEN TEK FARKI EKLEME ÇIKARMA YAPILAMAMASI
demet=()
demet=tuple()
demet=tuple([1,2,3])
demet=("elma","kiraz","armut")
demet=("elma","kiraz","armut",2.25,2)
print(demet)
demet=(1,2,4)
a=demet[1]
print(a)
uzunluk=len(demet)
print(uzunluk)
#demetleri ekrana yazdırma
demet=(1,2,3,56,312)
for i in demet:
    print(i)
#demet parçalama
demet=(421,43543,645,35,423,231,4232341)
print(demet[1:4])
#var yok kontrol etme
print(421 in demet) #true
print(150 not in demet) #true
print(demet.index(35))#35 kaçıncı indiste
#kaç kez tekrar ettiğini gösteriyor
demet=(43,123,43,123,76576,765,43)
k=demet.count(43)
print(k)
#max min bulma
demet=(234,5432,6534,3214,54)
b=max(demet)
c=min(demet)
print("En büyük:",b,"en kucuk",c)
#ya da
enbuyuk=demet[0]
enkucuk=demet[0]
for sayi in demet:
    if sayi>enbuyuk:
        enbuyuk=sayi
    if sayi<enkucuk:
        enkucuk=sayi
print("en buyuk:",enbuyuk,"enkucuk:",enkucuk)

#demetteki sayıları toplama
toplam=0

for sayi in demet:
    toplam+=sayi
print(toplam)