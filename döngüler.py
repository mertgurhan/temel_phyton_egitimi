sicaklik=12
if sicaklik>30:
    print("hava sicak")
elif sicaklik>=12 & sicaklik<30:
    print("hava ılık")
else:
    print("hava soğuk")

#while
while True:
    islem=input("işlem secin")
    if islem == "+":
        print("toplam")
    elif islem=="-":
        print("cıkarma")
    elif islem=="*":
        print("carpma")

#for döngüsü

harfler="abcd";
for h in harfler:
    print(h)
#range fonksiyonu 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i)

    for i in range(8,21,4):
        print(i)

#en büyük sayıyı bulma
sayilar=[43,143,54,32,11]
enbuyuk=sayilar[0]
for sayi in sayilar:
    if sayi>enbuyuk:
        enbuyuk=sayi
print("En buyuk sayi",enbuyuk)