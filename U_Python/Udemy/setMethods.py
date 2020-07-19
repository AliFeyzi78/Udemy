# sebzeler={"marol", "elma" , "pırasa"}
# print("mevcut sebzeler:"+ str(sebzeler))
# sebzeler.add("Maydonoz")


# sebzeler.update({"karpuz", "armut"})
# sebzeler.remove("marol")
# sebzeler.discard("erik")  #discard ile bir eleman silinebirlir. eğer o eleman kümede yoksa tepki(hata) vermez..
# print(sebzeler)

# gozlukluler={"ali", "ahmet", "veli", "ayşe"}

# erkekler={"tarık","kadir", "mustafa", "celil", "ali", "ahmet", "veli"}

# kadınlar={"ayşe", "aliye", "feyza", "leyla"}

# print(gozlukluler&erkekler)   #kesişim kümesi

# bilesimKumesi=gozlukluler| erkekler | kadınlar

# print(bilesimKumesi)

# farkKumesi=gozlukluler-erkekler
# print(farkKumesi)


#### bütün metotlar kümeye çevrilebilir..
#### set(), dict(), list() kullanılarak birbirine dönüşüm sağlanabilir#######
liste=[1,2,3,4,5]
demet=(1,2,3,4,5)
sozluk={"a":1,"b":2}

print(set(liste))
print(set(demet))
print(set(sozluk))

liste=[1,2,3,4,5]
print(liste)
print(*liste)   ### * koyarak elemanlar dışarı çıkarılabilir..

