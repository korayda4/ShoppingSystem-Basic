import colorama
from colorama import Fore
import os
import time

urun = {"mouse":["mouse",50,"PC"],"mousepad":["mousepad",25,"PC"],"kulaklık":["kulaklık",200,"PC"],"klavye":["klavye",100,"PC"],
        "soğutucu":["soğutucu",300,"PC"],"monitör":["monitör",1100,"PC"],"deri mont":["deri mont",500,"TEKSTIL"],"ekran kartı":["ekran kartı",12000,"PC"],"araba":["araba",7512000,"ARABA"],"telefon":["telefon",28000,"TEKNOLOJI"]
        }
urunonly = urun.copy()
alınacak = ""
kategoriler = ["PC","Tekstil","Teknoloji","araba"]
sepet = []

islem = ""

#Tekrar işlem yapılsın mı?
def tekrar():
    islem = input(Fore.YELLOW+"Tekrar işlem yapmak ister misiniz?(E/H)\n-->")
    while  islem.isdigit():
        islem = input(Fore.YELLOW+"Tekrar işlem yapmak ister misiniz?(E/H)")
    if islem == "e" or islem == "E":
        menu()
    elif islem == "h" or islem =="H":
        print("Görüşmek üzere...")
    else:
        print(Fore.RED+"Yanlış işlem seçimi (E/H)")
        tekrar()
        
#Anamenü
def menu():
    
    islem = input(Fore.YELLOW+"Lütfen İşlem seçiniz:\n1.)Mağaza\n2.)Sepetim\n3.)Kategoriler\n-->")
    if islem == "1":
       magaza()

    elif islem == "2":
       sepetim()

    elif islem == "3":
       kategori()
    else:
        print(Fore.RED+"Doğru işlem giriniz")
        menu()
#Mağazadaki tüm ürünleri göster
def magaza():
    j = 1
    for i in urun.values():       
        print(Fore.BLUE+f"{j}.)Ürün:",i[0],f"Fiyatı {i[1]}TL")
        j += 1
    alınacak = input(Fore.GREEN+"Satın almak istediğiniz ürünün ismini girin(Menüye Dön:Q)\n-->")
    if alınacak.upper() == "Q":
        menu()
    while  alınacak.isnumeric():
        alınacak = input(Fore.RED+"Lütfen İSİM girin\n-->")
    while not alınacak in urun:
        if alınacak not in urun:
                alınacak = input(Fore.RED+"Lütfen doğru ürün girin\n-->")
    urun.pop(alınacak)
    sepet.append(alınacak)
    print(Fore.GREEN+f"{alınacak} Başarıyla sepete eklendi.")
    
    tekrar()

#Sepetimizi göster
def sepetim(): 
    j = 1
    toplam = 0
    for i in sepet:
        print(Fore.CYAN+f"{j}.)Ürün:",i,f"Fiyatı {urunonly[i][1]}TL")
        j +=1
        toplam = urunonly[i][1] + toplam
    print(f"Toplam Fiyat:{toplam}TL")
    if not len(sepet) <= 0:
        sepetislem = input(Fore.YELLOW+"Sepet işlemleri:\n1)Sepeti boşalt\n2)Ürün sil\n3)Satın alımı tamamla\n4)Ana menüye dön\n-->")
        while not sepetislem.isdigit():
            sepetislem = input(Fore.RED+"İşlem numarası giriniz:\n1)Sepeti boşalt\n2)Ürün sil\n3)Satın alımı tamamla\n4)Ana menüye dön\n-->")
        if sepetislem == "1":
            for i in sepet:
                urun[i]=urunonly[i]
            sepet.clear()
            print(Fore.GREEN+"Başarıyla Temizlendi")
        elif sepetislem == "2":
            sil = input("Silinecek ürünün ismini giriniz\n-->")
            silici = sepet.index(sil)
            sepet.pop(silici)
            urun[sil]=urunonly[sil]
            print(Fore.GREEN+"Başarıyla Silindi!")
        elif sepetislem == "3":
            read = ""
            for i in Fore.GREEN+"Satın alımınız için teşekkürler...             ":
                read = read+i
                print(read)
                time.sleep(0.08)
                os.system("cls")
                
        elif sepetislem == "4":
            menu()  
            
                               
    tekrar()

#Kategorileri listele
def kategori():
    j = 1
    for i in kategoriler:
        print(Fore.BLUE+f"{j}.) Kategori :",i)
        j += 1
    kategorisecin = input(Fore.YELLOW+"Bir kategori seçin(isim)(Menüye Dön:Q)\n-->")
    while i in urunonly.values():
        if not kategorisecin.upper() == i[2]:
            kategorisecin = input(Fore.RED+"Bir kategori seçin(isim)(Menüye Dön:Q)\n-->")

    if kategorisecin.upper() == "Q":
        menu()
    while  kategorisecin.isdigit():
         kategorisecin = input(Fore.RED+"Lütfen isim olarak girin\n-->")
    j = 1
    work = False
    okay = False
    for i in urunonly.values():        
        if kategorisecin.upper() == i[2]:           
            print(Fore.BLUE+f"{j}.)Ürün:",i[0].capitalize())
            j +=1
            
            okay = True
        
    if okay:
        alınacak = input(Fore.GREEN+"Satın almak istediğiniz ürünün ismini girin\n-->")
        if alınacak == "teknoloji":
            alınacak = "TEKNOLOJİ"
        while  alınacak.isnumeric():
            alınacak = input(Fore.RED+"Lütfen İSİM girin\n-->")
        while not alınacak in urun:
            if alınacak not in urun:
                alınacak = input(Fore.RED+"Lütfen doğru ürün girin\n-->")
        work = True
    if work:
        urun.pop(alınacak)
        sepet.append(alınacak)
        print(Fore.GREEN+f"{alınacak} Başarıyla sepete eklendi.")
        tekrar()
    print(Fore.RED+"Aradığın kategori bulunmuyor!")
    tekrar()
print(Fore.YELLOW+"AcunMedyaAkademi Mağazasına Hoşgeldiniz!\n")
menu()
