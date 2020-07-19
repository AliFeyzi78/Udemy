# tuple da içerik değişikliği yapılamaz

# a=(1,2,3,4 ,5, 6)
# print(a)

# b=("s",) # normalde tek elemanlı bir tuple oluşturulamaz. ama , ile bunu yapabilirsin...
# print(b)

# a += b    # iki tuple birleştirilebilir..
# print(a)

# a += (7,8,9)
# print(a)

# c=10,11,12,13,11,10,10     #tuple oluşturmak için () gerek yoktur...
# print(type(c))

# print(c.count(10))

d=("ayşe","Veli","Ahmet")
print(d)

# print(d[0][0].upper())
# print(d)

#d=d[0][0].upper()

print(d.index("Veli"))

isim="FatihKaya"
print(list(isim))
print(tuple(isim))
