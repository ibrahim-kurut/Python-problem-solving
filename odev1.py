import math
# 1- Verilen bir listenin elemanlarını sondan başa doğru yazdırın.
liste = [1, 2, 3, 4, 5]
#! =========== cevap 1 ===========
resutl_1 = liste[::-1]
print(resutl_1)

# 2- Bir metnin içinde belirli bir kelimeyi arayarak, kelimenin kaç kez geçtiğini sayan bir program yazın.
metin = "Bu bir örnek metindir. Bu metin içinde kaç tane 'bir' kelimesi geçiyor acaba?"
kelime = "bir"
#! =========== cevap 2 ===========
resutl_2 = metin.count(kelime)
print("aranan kelime sayisi = ",resutl_2)


# 3- Verilen bir liste içindeki en büyük iki sayının toplamını hesaplayan bir program yazın.
liste = [4, 2, 8, 1, 9, 5, 6, 3, 7]
#! =========== cevap 3 ===========
#? Listeyi büyükten küçüğe sırala
sirali_liste = sorted(liste, reverse=True)
#? En büyük iki sayiyi almak
en_buyuk = sirali_liste[0]
ikinci_en_buyuk = sirali_liste[1]
toplama = en_buyuk + ikinci_en_buyuk
print("en buyuk iki sayinin toplamasi = ",toplama)

# 4- Verilen bir metindeki harflerin sayısını hesaplayan bir program yazın.
metin = "Bu bir örnek metindir."
#! =========== cevap 4 ===========
print("metindeki harf sayisi = ",len(metin))


# 5- Verilen bir sayının karesini hesaplayan bir program yazın.
sayi = 5
#! =========== cevap 5 ===========
print("sayinin karesi  = ",math.pow(sayi,2))
#? yada 
print("sayinin karesi  = ",(sayi*sayi))


# 6- Verilen bir dizi sayının ortalamasını hesaplayan bir program yazın.
numbers = [2, 4, 6, 8, 10]
#! =========== cevap 6 ===========
resutl_3 = sum(numbers) / len(numbers)
print(resutl_3)


# 7- İki sayının toplamını, farkını, çarpımını ve bölümünü hesaplayan bir program yazın.
num1 = 18
num2 = 21
#! =========== cevap 7 ===========
toplama = num1 + num2
fark = num1 - num2
carpi = num1 * num2
bolme = num1 / num2
print("toplama=",toplama, "fark=",fark, "carpi=",carpi , "bolme=",bolme)


# 8- Verilen bir string içindeki tüm boşlukları kaldıran bir program yazın.
string  = "Merhaba dunya, nasilsiniz?"
#! =========== cevap 8 ===========
resutl_4 = string.replace(" ","")
print(resutl_4)



# 9- İlk alt listenin ikinci elemanına erişmek için
# İkinci alt listenin üçüncü elemanına erişmek için
# Son alt listenin ilk elemanına erişmek için
# ilk alt listenin ilk elemanını 0 ile değiştirmek
# ikinci alt listenin ikinci elemanını 10 ile değiştirmek
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#! =========== cevap 9 ===========
print("ilk alt listenin ikinci elemani =",matrix[0][1])
print("ikinci alt listenin ucuncu elemani =",matrix[1][2])
print("ikinci alt listenin ucuncu elemani =",matrix[2][0])
x=matrix[0][0]=0
y=matrix[1][1]=10
print("ikinci alt listenin ilk elemani degistiktend sonra =",x)
print("ikinci alt listenin ilk elemani degistiktend sonra =", y)


# 10- Verilen koddaki hatayı düzeltin
#! =========== cevap 10 ===========
string_1 = "Bugün hayatımın en güzel günü. Hayalini kurduğum meslek olan "'.... Developer'" olmaya her geçen gün dahada yaklaşıyorum, elimden gelenin fazlasını yapıyorum. Başarımın meyvesini alacağıma çok eminim Cosmios Yazılım Akademi en büyük yardımcım."

# print(string_1)


# 11- Aşağıda verilen kodun çıktısı ne olur ? Lütfen çalıştırmadan önce tahmin ediniz ve cevabınızı tahmin ettiğiniz çıktıyı yazınız.
a = 15
b = 3

#! =========== cevap 11 ===========
'''
#? a_mod_b = 0 olduguma gore ne ile carptigimizda sonuc 0 olacaktir
'''
a_mod_b = a % b 
a_pow_b = a ** b 
# print(a_mod_b * a_pow_b)


# 12- Aşağıda verilen kodun çıktısı ne olur ? Lütfen çalıştırmadan önce tahmin ediniz ve cevabınızı tahmin ettiğiniz çıktıyı yazınız.
# x = 12
# y = 21

# y = x
# x += y
# y *= y
# x /= y

#! =========== cevap 12 ===========
#? x = 0.12 // tahmin
#? y = 144 // tahmin
# print(x) 
# print(y) 


# # 13- Adınızı ve soydınızı giriniz. 
# # Adınızın ilk 3 karakteri parçalayıp soyadınızın son 3 karakterini parçalayıp elde ettiğiniz verileri tek bir kelime haline getirip bir değişkene atayınız.
ad = "ibrahim"
soyad = "kurut"
#! =========== cevap 13 ===========
ad_ilk_3_karek = ad[:3]
soyad_son_3_karek = soyad[-3:]
resutl_5 = ad_ilk_3_karek + soyad_son_3_karek
print(resutl_5)



# # 14- Aşağıda verilen kodun çıktısı ne olur ? Lütfen çalıştırmadan önce tahmin ediniz ve cevabınızı tahmin ettiğiniz çıktıyı yazınız.
example = "Ben basarili bir insanim."
#! =========== cevap 14 ===========
#? bas
#print("{}".format(example[4:7])) 



# # 15- Aşağıda verilen kodun çıktısı ne olur ? Lütfen çalıştırmadan önce tahmin ediniz ve cevabınızı tahmin ettiğiniz çıktıyı yazınız.
#! =========== cevap 15 ===========
#? 11
L1 = []
L1.append([1, [2, 3], 4])
L1.extend([7, 8, 9])
# print(L1[0][1][1] + L1[2])

# 16- Aşağıda verilen tuple veri türünün kaç elemanlı olduğunu
# 5 numaralı indeks numaralı elemanın ne olduğunu bulunuz
# [1, "2"] elemanını silip onun yerine "her geçen gün python'u daha iyi öğreniyorum" ifadesini ekleyiniz.
tuple_1 = ("1", 2, [1, "2"], {"set": "Setler sirasiz bir yapiya sahiptir"})
#! =========== cevap 16 ===========
#?  convert tuple to list
myList = list(tuple_1)
#? change in list 
myList[2] = {"set": "her gecen gun python'u daha iyi ogreniyorum"}
#?  convert list to tuple  
tuple_1= tuple(myList)
print(tuple_1)

