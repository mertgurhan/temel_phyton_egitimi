#fonksiyon tanımlama
def mesajyaz():
    print("merhaba")

def topla(a,b):
    sonuc=a+b
    print(sonuc)

topla(2,5)
mesajyaz()
#birden fazla değer döndürme
def Ikiliislem(a,b):
    toplam=a+b
    carpim=a*b
    return toplam,carpim

a1,a2=Ikiliislem(3,5)
print(a1,"-",a2)
#varsayilan değerli parametreler
def Mesajyaz(mesaj,adet=1):
    for i in range(adet):
        print(mesaj)

Mesajyaz("selamlar",4)

#ilk değerli parametreli

def Mesajyaz(mesaj="merhaba",adet=6):
    for i in range(adet):
        print(mesaj,6)