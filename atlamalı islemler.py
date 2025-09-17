toplam=0
while True:
    sayi=input("Sayi giriniz:")
    if sayi<0:
        break
    toplam+=sayi
print("Toplam:",toplam)
#küçükten büyüğe sıralama
smallest=None
print('Before')
for value in [1,43,54,123,54,654,5,7,3]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
        print(smallest,value)
print("After",smallest)