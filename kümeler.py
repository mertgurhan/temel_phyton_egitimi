#KÜMELERİN DEMETLERDEN FARKI DEĞİŞTİRME EKLEME YAPIŞABİLMESİDİR

kume=set() #boş küme oluşturmak için mutlaka yoksa dic ile karıştırılır kume={}
kume={1,2,3,4,6,7}
print(kume)

sayilar=set(kume)
print(sayilar)
#ekleme
sayilar.add(13)
print(sayilar)
#cikarma
sayilar.remove(13)
print(sayilar)
#iki kume farkı
kume1={"a","b","c"}
kume2={"a,b,c,d,e,f,g","a"}
fark=kume2.difference(kume1)
print(fark)
#ya da
fark=kume2-kume1

karakter="abcdefghiklmnoprstuvyz"
isim=input("Adınızı giriniz:")
if set(karakter) & set(isim):
    print("Girdiginz harfler alfabeden karakterler içeriyor")

else: print("naneyi yedin!")
