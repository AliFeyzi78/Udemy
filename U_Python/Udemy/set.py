#kümelerde elemanlar sadece 1 defa bulunur. 

kume1={1,2,3,7,7,8,8,1,2,2,2}  
print(kume1)
print(len(kume1)) # sadece 1 defasayar

#değişen bir veri tipi (listeler, sözlükler,..) küme içinde saklanamaz. çünkü kümeler değiştirilemez. yani "tuple" koyabiliriz.

liste=[1,2]
sozluk={}
demet=(1,3,5)
#kume={sozluk}  #kabul etmez 
kume={demet}

print(kume)