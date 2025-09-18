#MODÜLLER İŞLEMİ FONKSİYON HALİNE GETİRİYOR
import os #işletim sistemi için
import time #zaman içim
import calendar #takvim için

import os
os.name

import random as rastgele #random modülüne rastgele ismini verdik
x=rastgele.randint(1,50)
print(x)
from os import name #sadece name özelliğğini aldı bu yüzden ek yük getirmiyor
import math #import içerisindeki fonksiyonları gösteriyor
icerik=dir(math)
print(icerik)

import time
print(time.time())

#local zaman
currenttime=time.localtime()
print(currenttime)

print(currenttime[6])
#FORMATLI ZAMAN GÜNCEL
formatlizaman=time.asctime()
print(formatlizaman)

formatlizaman=time.strftime("%d %m %y %H:%M:%S")
print(formatlizaman)

import calendar
takvim=calendar.calendar(2025)
print(takvim)

takvim=calendar.month(2002,11)
print(takvim)
