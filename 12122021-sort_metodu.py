liste=[1,8,25,2,6,156,212,45]
isimler=["ali","veli","ayşe","fatma"]
print(liste)
liste.sort() #küçükten büyüğe doğru, a dan z ye doğru sıralama yapar(artan sıralama)
print(liste)
isimler.sort()
print(isimler)
isimler.sort(reverse=True) #z den a ya doğru, büyükten küçüğe doğru sıralama yapar
print(isimler)
liste.sort(reverse=True)
print(liste)

#Ödev: 2 basamaklı sayıların okunuşunu yapan python programını yazınız.
#Örnek: kullanıcı 12 girdi --> oniki
#Örnek: kullanıcı 85 girdi --> seksenbeş
#birlik=["bir","iki" ... ]
#onluk=["on" ...] bunlar gibi
#85//10= 8 // = tam bölme
#85%10=5 10 a bölümünden kalanı verir