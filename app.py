# yazi = "TMBM"

# print(*yazi)

# def sayilariTopla (*degerler):
#      toplam=0
#      for deger in degerler:
#           toplam+=deger

#      return toplam

#  print(sayilariTopla(1,2,3))


# sayilar = [x for x in range(1,1001)]
# print(sayilar)


# ogrenciler = ['a','b','c','d']

# print(len(ogrenciler))

# for ogrenci in ogrenciler:
#      print(ogrenci)


# ogrenciler.remove("a")
# print(ogrenciler)
# print(len(ogrenciler))

# liste = [1,2,3]
# liste  = liste * 3

# print(liste)

# kullanicilar = ['ali', 'samir', 'ay']
# sifre = ['1','2','3']

# users = [kullanicilar,sifre]

# print(users[0][1])

# sozluk = {}
# print(type(sozluk))

# kisiler = {
#      'melis': 20,
#      'samir': 19,
#      'ayan': 18,
#      'eli': 10
# }

# print(kisiler['eli'])

# ***********************************************************
# uyeler = {
#      'uye':['samir', 'ali', 'samira'],
#      'yonetici': ['gunel', 'nicat', 'togrul']
#      }

# while True:
#      islem = int(input("\n1-kisi kadir\n2-kisi ekle\n3-sistemden cik\nyapmak istediginiz islemi secin:"))
#      if islem == 1:
#           yetki = input("yetkiyi yaziniz(uye,yonetici)")
#           if yetki == "uye":
#                print(uyeler['uye'])
#                isim =input("kaldirmak istedigin uyenin adini girin: ")
#                uyeler['uye'].remove(isim)
#           if yetki == "yonetici":
#                print(uyeler['yonetici'])
#                isim =input("kaldirmak istedigin yoneticinin adini girin: ")
#                uyeler['yonetici'].remove(isim)
#                print(uyeler)
#      elif islem == 2:
#           yetki = input("yetkiyi yaziniz(uye,yonetici)")
#           if yetki == "uye":
#                print(uyeler['uye'])
#                isim =input("eklemek istedigin uyenin adini girin: ")
#                uyeler['uye'].append(isim)
#           if yetki == "yonetici":
#                print(uyeler['yonetici'])
#                isim =input("eklemek istedigin yoneticinin adini girin: ")
#                uyeler['yonetici'].append(isim)
#                print(uyeler)
#      else:
#           break
#      print(uyeler)


# def kareAl(a):
#      return a**2

# sayi = int(input("bir sayi girin: "))
# print(kareAl(sayi))


# print("""
# ***hesap makinesi***
# """)

# ***********************************************************
# def kareAlA (a):
#      return a**2

# def kareAlB (b):
#      return b**2

# while True:
#       sayiA = int(input("a sayisini giriniz: "))
#       print(kareAlA(sayiA))
#       sayiB = int(input("b sayisini giriniz: "))
#       print(kareAlB(sayiB))
#       sayilariTopla = kareAlA(sayiA) + kareAlB(sayiB)
#       print(sayilariTopla)


# ingilisce oyrendiyin sozleri list e topla(samirden sorus)
# ********************************************
# while True:
#     kelimeniGir = input("oyrendiyim kelime: ")
#     kelimeler = []
#     kelimeler += kelimeniGir
#     print(kelimeler)


# ***********************************************************
# ogrenci = input("Isminizi ve Soyisminizi giriniz: ")
# vize = int(input("vize puanini giriniz: "))
# final = int(input("final puanini giriniz: "))

# sonuc = ((vize * 40)/100 + (final * 60)/100)

# print(sonuc)
# harf_notu = ""

# ***********************************************************
# if sonuc>=85 and sonuc<=100:
#     harf_notu = "AA"
# elif sonuc>=70 and sonuc<=85:
#     harf_notu = "BA"
# elif sonuc>=60 and sonuc<=70:
#     harf_notu = "BB"
# elif sonuc>=50 and sonuc<=60:
#     harf_notu = "CA"
# elif sonuc>=40 and sonuc<=50:
#    harf_notu = "CC"
# elif sonuc>=0 and sonuc<=40:
#     harf_notu = "FF"
# else:
#     print("lutfen dogru rakami giriniz")

# print("{} adli ogrencinin bu dersde elde etdigi harf notu: {}".format(ogrenci,harf_notu))

# with open("notlar.txt", "a") as dosya:
#     dosya.writelines("{} adli ogrencinin bu dersde elde etdigi basari notu: {} ve harf notu: {}\n".format(ogrenci,sonuc,harf_notu))


# *****************************
# import random
# yaziGelen = 0
# turaGelen = 0

# ParaYuzeyi = ["yazi", "tura"]

# atilacakPara = int(input("kac kere parayi atmak istiyorsunuz: "))

# while atilacakPara > 0:
#    paraUstu = random.choice(ParaYuzeyi)
# if paraUstu == "tura":
#      turaGelen+=1
#      print("tura geldi")
# else:
#     yaziGelen+=1
#     print("yazi geldi")

# atilacakPara -= 1
# print("tura sayisi: {}n\yazi sayisi: {}".format(yaziGelen,turaGelen))


# *****************************
# sayi = 0
# while sayi<=10000:
#     print(sayi)
#     sayi+=1


# *****************************
# for sayi in range(20):
#     print(sayi)

# *****************************
# for sayi in range(20,50):
#     print(sayi)

# ***********************************************************
# for sayi in range(100,200,5):
#     print(sayi)


# ***********************************************************
# sayi = int(input("sayiyi giriniz: "))
# sayiListi = []

# while sayi <= 10:
#     sayiListi.append(sayi)
#     if sayi%2 ==0:
#         sayiListi.remove(sayi)
#         break


# ***********************************************************
# sayilar = []

# for i in range(1,100):
#     if i%2==0 and i%3==0:
#         sayilar.append(i)

#         print(sayilar)

# ***********************************************************
# sayilar = [x for x in range(1,100) if x%2==0 and x%3==0]
# print(sayilar)


# ***********************************************************  FAKTORIAL  *********
# num = int(input("Enter a number: "))
# factorial = 1
# if num < 0:
#    print(" Factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i

# print("{}!= ".format(num) + str(factorial))

# ********************************************************************
# def sirala():
#   for i in range(20):
#     print("samira")

# sirala()

# ********************************************************************
# from audioop import reverse


# def sirala (sayi, yazi):
#   for i in range(sayi):
#     print(yazi)


# sirala(10, "samira")


# *****************************EBOB***************************************
# def ebob (a,b):
#   kucukSayi = min(a,b)
#   ortakBolenler = []
#   for i in range(1, kucukSayi+1):
#     if a%i==0 and b%i==0:
#       ortakBolenler.append(i)
#   ortakBolenler.sort(reverse=True)
#   return ortakBolenler[0]

# print(ebob(50,70))

# basa dusmedim????
# def ebob (a,b):
#   kucukSayi = min(a,b)
#   enbuyukOrtakBolen = 1
#   for i in range(1,kucukSayi+1):
#     if a % i == 0 and b % i == 0:
#       enbuyukOrtakBolen = i

#   print(f"{a} ve {b}'nin en buyuk ortal boleni: {enbuyukOrtakBolen}'dir.")

# ebob(50,70)


# *****************************RETURN**************************************
# def tekseDondur_cutseCik(sayi):
#   if sayi % 2 == 1:
#     return sayi

#   toplam = 0
#   for i in range(1,sayi+1):
#     toplam+=i

#   return toplam

# print(tekseDondur_cutseCik(19))
# print(tekseDondur_cutseCik(10))


# *****************************Parametr**************************************
# def topla (*sayilar):
#   toplam = 0
#   for sayi in sayilar:
#     toplam+=sayi
#   return toplam

# print(topla(1,2,3,4,5,6,7,8,))

# **********************
# def topla (*sayilar):
#  return sum(sayilar)

# print(topla(1,2,3,4,5,6,7,8,))


# *****************************TAPSIRIQ**************************************


# sayi = int(input("bir sayi giriniz: "))


# def TamSayiBolenler (sayi):
#   list = []
#   for i in range(1,sayi+1):
#     if sayi % i == 0:
#        list.append(i)
#        if i == sayi:
#          return list


# print(TamSayiBolenler(sayi))


# *****************************EKOB**************************************
# def ekob(a,b):
#   list = []
#   enBuyukSayi = a*b
#   if a>b:
#     baslangicSayi = a
#   elif b>a:
#     baslangicSayi = b
#   for i in range(baslangicSayi,enBuyukSayi+1):
#     if i%a ==0 and i%b==0:
#       list.append(i)
#   list.sort
#   return list[0]

# print(ekob(40,60))

# ************************************************************************

# import random
# print(random.randint(1,10))

# ********************************RANDOM****************************************
# ***sef****
# texminEt = int(input("aglinizda olan sayini giriniz: "))
# import random
# random.randint(1,5)

# def texmin():
#     for i in range(1,5):
#         if texminEt>i:
#             print("dogru sayi asagida")
#         elif texminEt<i:
#             print("dogru sayi asagida")
#         elif texminEt==i:
#             print("tebrikler dogru texmin etdiniz")


# texmin()

#***************************

# from random import randint

# oyunDurumu = True

# while oyunDurumu:
#     rastgeleSayi = randint(1, 10)
#     hak = 7
#     while True:
#         if hak > 0:
#             tahmin = int(input("sizce sayi kac (1-10): "))
#         else:
#             print("sayiyi tahmin edemediniz :( Sayi : {}".format(rastgeleSayi))
#             break
#         if tahmin != rastgeleSayi:
#             hak -= 1
#             if tahmin > rastgeleSayi:
#                 print("sayi asagida! kalan tahmin hakkiniz : {}".format(hak))
#             else:
#                 print("sayi yukarida! kalan tahmin hakkiniz : {}".format(hak))
#         else:
#             print("tebrikler sayiyi buldunuz")
#             break
#     kontrol = input("oyuna devam etmek istiyosunuzmu?(E/H)")
#     if kontrol == "E":
#         oyunDurumu = True
#     else:
#         oyunDurumu = False

#*****************************OOP***************************************
# students = []
# class Student:
#     def __init__(self,_ad,_soyad,_email):
#         self.name = _ad
#         self.surname = _soyad
#         self.email = _email
#         students.append(self)
        

# while True:
#     emr = input("yeni telebe qeydiyyati aparilsinmi: (Y/N)")
#     if emr == "Y":
#         ad = input("Ad: ")
#         soyad = input("soyad: ")
#         email = input("email: ")
#         student=Student(ad,soyad,email)
#     elif emr == 1:
#         for student in students:
#             print(f"(student.name) | (student.surname) | (student.email)")
#     else:
#         break
#********************************

# class Araba():
#     def __init__(self,marka,model,fiyat,renk):
#         self.gelenMarka = marka
#         self.gelenModel = model
#         self.gelenFiyat = fiyat
#         self.gelenRenk = renk

#     def BilgileriYazdir(self):
#         print(self.gelenMarka,self.gelenModel,self.gelenFiyat,self.gelenRenk)

#     def renkDegistir(self,renk):
#         self.gelenRenk = renk



# araba1 = Araba("Renault", "Clio", "40000", "Mavi")

# araba1.BilgileriYazdir()
# araba1.renkDegistir("yesil")
# araba1.BilgileriYazdir()

#****************************** OOP ile sirket otomosyonu *************

class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True

    def program(self):
        secim = self.menuSecim()

        if secim == 1:
            self.calisanEkle()
        if secim == 2:
            self.calisanCikar()
        if secim == 3:
            self.VerilecekMaasGoster()
        if secim == 4:
            self.maaslariVer()
        if secim == 5:
            self.masrafGir()
        if secim == 6:
            self.gelirGir()

    def menuSecim(self):
        secim = int(input("**** {} otomosyonuna hos geldiniz ****\n\n1-Calisan ekle\n2-Calisan cikar\n3-Verilecek maas goster\n4-Maaslari ver\n5-Masraf gir\n6-Gelir gir\n\nSeciminizi giriniz: ".format(self.ad)))
        while secim < 1 or secim > 6:
            secim = int(input("Lutfen 1-6 arasindaki seceneklerden birini giriniz: "))
        return secim

    def calisanEkle(self):
        pass

    def calisanCikar(self):
        pass

    def VerilecekMaasGoster(self,hesap="a"):
        """ hesap: a ise aylik, y ise yillik hesap"""
        pass

    def maaslariVer(self):
        pass

    def masrafGir(self):
        pass

    def gelirGir(self):
        pass


sirket = Sirket("Socar")

while sirket.calisma:
    sirket.program()



