# Eğer meyve sepette değilse, "Biraz alabilirim" deyin.
# Aksi takdirde, "Zaten var" deyin.

basket = ['apple', 'peach', 'blackberry']
fruit = 'apple'

#! ============ cevap 1 ============
for i in basket:
    if i == fruit:
        print("Zaten var")
        break
    else:
        print(f" {i}`dan Biraz alabilirim")




total = 149
country = "FR"

if country == "FR":
    if total <= 50:
        print("Shipping Cost is  €30")
    elif total <= 100:
        print("Shipping Cost is €15")

    elif total <= 150:
        print("Shipping Costs €10")
    else:
        print("Free Shipping")
if country == "DE": 
    if total <= 50:
        print("Shipping Cost is  €25")
    else:
        print("Free Shipping")
        #! ============ cevap 2 ============
        #! 10 olacak
# Yukarıdaki programa göre kargo ücreti ne kadar?


# Aşağıda verilen koşulları sağlayan bir program yazınız. 
# Değişkenin adını olarak tanımlayın number.
# 10'a eşit number veya 10'dan büyükse, şunu yazdırın: 'Sayı 10'a eşit veya 10'dan büyük',
# 10'dan küçükse number, şunu yazdırın: 'Sayı 10'dan küçük'.

        #! ============ cevap 3 ============

number = 15
result  = "Sayi 10'a esit veya 10'dan buyuk" if number >= 10 else "Sayi 10'dan kucuk"
print(result)


# Tom adında 13 yaşında bir çocuk, PlayStation-4 oynamak istiyor. 
# Ancak ona maddi gücü yetmediği için PS4'ün fiyatına ulaşmak için para biriktirmeye başladı (ps4_price değişkeni). 
# Tom'a ne kadar zaman kaldığını söyleyen bir program yazalım. Kaydedilen tutara (saved_amount değişkeni) göre aşağıdaki üç seçenekten birini yazdıran basit bir kod yazın:

# Eğer kaydedilen tutar ps4_price'in yarısından az veya eşitse, "Daha fazla biriktirmelisin, biriktirmeye devam et!" yazdırın.
# Eğer kaydedilen tutar ps4_price'in yarısından büyükse, "Yarısından fazlasını biriktirdin, biriktirmeye devam et!" yazdırın.
# Eğer kaydedilen tutar ps4_price'tan büyükse, "Yippee! PS4'ünü satın alabilirsin." yazdırın.
        #! ============ cevap 4 ============

ps4_price = 3000 # PlayStation-4'ün fiyatı 3000 lira olsun
saved_amount = 1600

if saved_amount < ps4_price / 2  : 
    print("Daha fazla biriktirmelisin, biriktirmeye devam et!")
elif saved_amount <= ps4_price / 2 :
    print("Yarisindan fazlasini biriktirdin, biriktirmeye devam et!")
else : 
    print("Yippee! PS4'unu satin alabilirsin.")




# Aşağıdaki listenin tüm öğelerini aşağıdaki gibi ayrı satırlara yazdıran programı yazdırın:
# Not: whileDöngü kullanın.
# Örnek çıktı:
# Rose
# Orchid
# Tulip
        #! ============ cevap 5 ============
flowers = ['Rose', 'Orchid', 'Tulip']
i = 0
while i < len(flowers):
  print(flowers[i])
  i += 1

        #! ============ cevap 6 ============
# Aşağıdaki listedeki her bir sayının karesini ayrı satırlara yazdıran bir program yazınız .
iterable = [1, 2, 3, 4]
for i in iterable:
    print(i**2)

        #! ============ cevap 7 ============
# Aşağıdaki tuple'ın tüm öğelerini örnek çıktıdaki gibi ayrı satırlara yazdıran programı yazdırın:
# Not: for Döngü kullanın.
# Örnek çıktı:
# Elma 
# Muz 
# Portakal
meyveler = ('Elma' ,'Muz' ,'Portakal')

for meyve in meyveler:
    print(meyve)

#! ============ cevap 8 ============
# Bayan Brown bir Matematik öğretmenidir. 
# Öğrencilerinin sayısal notlarını alan, bunları math_mark değişkenine atayan ve aşağıda tanımlanan harf tabanlı notlar olarak yazdıran bir program yazmak istiyor:
# 85-100 ➔ A (Mükemmel)
# 70-84 ➔ B (İyi)
# 60-69 ➔ C (Orta)
# 45-59 ➔ D (Fena Değil)
# 0-44 ➔ F (Başarısız)
# if, elif ve else deyimlerini kullanarak programınızı yazınız.

math_mark = 65

if math_mark >= 85:
    print("A")
elif math_mark > 70 and math_mark < 85:
    print("B")
elif math_mark > 60 and math_mark < 70 :
    print("C")
elif math_mark > 45 and math_mark < 60 :
    print("D")
elif math_mark > 0 and math_mark < 45 :
    print("F")



