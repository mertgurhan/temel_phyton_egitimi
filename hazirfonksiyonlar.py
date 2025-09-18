#hazir fonksiyonlar
#matematik için
import math
from dataclasses import replace

from döngüler import enbuyuk

#mutlak değeer alma
a=math.fabs(-12)
print(a)
# ya da
a=abs(-14)
print(a)
#sayiyi yukarı yuvarlama
a=math.ceil(2.105)
print(a)
#aşşagı yuvarlama

a=math.floor(2.105)
print(a)

#üs alma
a=math.pow(2,3)
print(a)
#karekök alma
a=math.sqrt(25)
print(a)
#log işlemlerinde
a=math.log(1000,10)
print(a)

#sin cos tan hesabo
aci=math.radians(30)
a=math.sin(aci)
a=math.cos(aci)
a=math.tan(aci)

#max min bulmak
sayilar=[43,123,54,12,22,56,771,11]
enbuyuk=max(sayilar)
enkucuk=min(sayilar)
print("Sayi dizisinin en büyül sayisi=",enbuyuk,"enkucuk sayisi=",enkucuk)
#toplam fonksiyonu

sayilar=[12,32,54,12]
toplam=sum(sayilar)
print(toplam)
#bir sayinin başka bir sayiya bölündükten sonraki kalan ve bölümünü verdiren fonksiyon
print(divmod(12,7))
#binary dönüştürme fonksiyonu
sonuc=bin(5)
print(sonuc)

#karakterleri değiştiren fonksiyon
replace("Değiştirelecek karakter grubu","yeni karakter grubu")
str="phyton güclü bir programlama dilidiir"
yenideger=str.replace("p","P")
print(yenideger)
#P ler değişecek
str="phyton güclü bir programlama dilidiir"
yenideger=str.replace("p","P",2)
print(yenideger) #dersej sadece 2 p degeri değişecek

#büyük harf yapma
str="çiçek"
buyuk=str.upper()
print(buyuk)
#lower kucuk harf yapma
str="çiçek"
kucuk=str.lower()
print(kucuk)
#CAPİTALİZE sadece ilk harfini bbüyüük yapmaya yarıyor

str="PHYTON PROGRAMLAMA DİLİ"
sonuc=str.capitalize()
print(sonuc) #sadece phytonda p büyülk kalır

#title ise her kelimenimn ilk harfini büyük yapar
str="pHYTON pROGRAMLAMA dİLİ"
sonuc=str.title()
print(sonuc)
#SWAP CASE büyüğü küçük küçükü büyük
str="aYvA"
SONUC=str.swapcase()
print(sonuc)
#format fonkisoynu

a=int(input("Birinci sayiyi giriniz:"))
b=int(input("İkinci sayiyi giriniz:"))

sonuc=str(a)+"+"+str(b)+"="+str(a+b)
