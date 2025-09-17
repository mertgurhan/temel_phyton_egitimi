#Bir geri döndürmeli fonksiyon yapıcaz

def Faktoriyel(sayi):
    carpim=1
    for i in range(sayi,1,-1):
        carpim*=i
    return carpim
print(Faktoriyel(5))