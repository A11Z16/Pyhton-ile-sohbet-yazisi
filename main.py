ali = "Ali"                # Burda Ali ismini tanımladım
ahmet = "Ahmet"             #Burda Ahmet ismini tanımladım
s = "sen"                   #Sen kelimesini çok kullandığımız için kısalttım.
n = "ne"                   #Burda ne kelimesini kısaltım.

(bir, iki, uc, dort, bes, alti, yedi, sekiz, dokuz) = (1, 2, 3, 4, 5, 6, 7, 8, 9)   #Burda sayılara bir değişken ekledim.
cumle1 = "Merhaba {dayı}, nasılsın?".format(dayı=ali) #Burda 1.cümlemi yazdım.
print(cumle1)                                         #Burda 1.cümlemin ekrana yazmasını sağladım
cumle2 = "İyiyim {a}, sen nasılsın?".format(a=ahmet)
print(cumle2)
cumle3 = "Bende iyiyim,{n} yapıyorsun?" .format(n=n)
print(cumle3)
cumle4 = "Oyun oynuyorum,{s} {n} yapıyorsun?" .format(s=s,n=n)
print(cumle4)
cumle5 = "Kod yazıyorum"
print(cumle5)
bitis = "sohbet bitmistir."         #Burda sohbetin bittiğini haber veren yazıyı ayarladım.
print(bitis.upper())                 #Burda sohbetin bittiğini haber veren yazının tamamının büyük olarak ekrana yazılmasını sağladım.
