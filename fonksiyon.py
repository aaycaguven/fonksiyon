#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım
i = 0
fibonacci = [1 , 1]

while (len(fibonacci) != 20):
       value = fibonacci[i] + fibonacci[i + 1]
       fibonacci.append(value)
       i += 1
       for items in fibonacci:
         print(items)

#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
        
sayi=int(input("Sayi giriniz :"))
x=0
i=1
while i<sayi:
    if (sayi%i==0):
        x=x+i
    i+=1

if (x==sayi):
    print("Mükemmel sayidir.")
else:

    print("Mükemmel sayi değildir. ")
    

#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
    number = int(input("Sayi giriniz: "))
number2 = int(input("Sayi giriniz: "))

def isprime(number):
    i = 2
    if number == 2:
        return True
    while i < number:
        if (number % i == 0):
            return False
        i+=1
    return True

def lcm(number, number2): #ekok
    number_array = []
    x = 1
    i = 2
    while number > 1 or number2 > 1:
        while isprime(i) and (number % i == 0 or number2 % i == 0):
            if number % i == 0 and number2 % i == 0:
                number = number / i
                number2 = number2 / i
            elif number % i == 0:
                number = number / i
            elif number2 % i == 0:
                number2 = number2 / i
            number_array.append(i)
        i += 1
    for i in number_array:
        x *= i
    return x

def gcd(number, number2):  #ebob
    number_array = []
    x = 1
    i = 2
    while number > 1 or number2 > 1:
        while isprime(i) and (number % i == 0 or number2 % i == 0):
            if number % i == 0 and number2 % i == 0:
                number_array.append(i)
                number = number // i
                number2 = number2 // i
            elif number % i == 0:
                number = number // i
            elif number2 % i == 0:
                number2 = number2 // i
        i += 1
    for i in number_array:
        x *= i
    return x

print("ebob:" + str(gcd(number, number2)))
print("ekok:" + str(lcm(number, number2)))


#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi = int(input("Bir sayi giriniz: "))
x=0
i=2 
while i< sayi:
    if(sayi % i == 0):
        x+=1
    i+=1

if x==0:
    print("Sayiniz asaldir")
else :
    print("Sayiniz asal değildir")


#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
    
def asal_carpanlara_ayir(sayi):
    asal_carpanlar = []
    bolen = 2
    while sayi > 1:
        while sayi % bolen == 0:
            asal_carpanlar.append(bolen)
            sayi //= bolen
        bolen += 1
    return asal_carpanlar
 
# Kullanıcıdan sayı alınması
girilen_sayi = int(input("Lütfen asal çarpanlarina ayirmak istediğiniz sayiyi giriniz: "))
asal_carpanlar = asal_carpanlara_ayir(girilen_sayi)
print("Asal Çarpanlar:", asal_carpanlar)
