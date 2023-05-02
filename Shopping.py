import colorama
from colorama import Fore
import os
import time

urun = {"mouse":["mouse",50,"PC",5,0],"mousepad":["mousepad",25,"PC",13,0],"kulaklık":["kulaklık",200,"PC",10,0],"klavye":["klavye",100,"PC",10,0],
        "soğutucu":["soğutucu",300,"PC",15,0],"monitör":["monitör",1100,"PC",14,0],"deri mont":["deri mont",500,"TEKSTIL",12,0],"ekran kartı":["ekran kartı",12000,"PC",1,0],"araba":["araba",7512000,"ARABA",1,0],"telefon":["telefon",28000,"TEKNOLOJI",10,0],"Nisantası Universitesi":["Nisantası Universitesi",1000000000000000000000000,"UNIVERSITE",1,0]
        }

urunonly = urun.copy()
alınacak = ""
kategoriler = ["PC","TEKSTIL","TEKNOLOJI","ARABA"]
sepet = []

islem = ""

#Ürün oluştur
def urunolustur():
    global yeniurun
    sifre = input(Fore.RED+"Personel Şifresini giriniz(Menüye Dön:Q)\n-->")
    if sifre.upper() == "Q":
        os.system("cls")
        print("Menüye Aktarılıyorsunuz")
        time.sleep(1)
        menu()
    if sifre == "123456":
        os.system("cls")
        yeniurun = input(Fore.GREEN+"Yeni ürün ismini girin\n-->")
        for i in urun.values():
                while yeniurun == i[0]:
                    yeniurun = input(Fore.RED+"Böyle bir ürün bulunuyor , Tekrar deneyin\n-->").upper()
        while yeniurun.isdigit():
            yeniurun = input(Fore.RED+"Lütfen isim girin!\n-->")
            
        yeniücret = input(Fore.GREEN+"Ücreti girin!\n-->")
        while not yeniücret.isdigit():
            yeniücret = input(Fore.RED+"Lütfen sayı girin!\n-->")
            
        yenikategori = input(Fore.GREEN+"Kategorisini girin\n-->").upper()
        for i in kategoriler:
                while yenikategori.upper() == i:
                    yenikategori = input(Fore.RED+"Böyle bir kategori bulunuyor , Tekrar deneyin\n-->").upper()

        while not yenikategori.isalpha():
            yenikategori = input(Fore.RED+"Lütfen kategori girin!\n-->").upper()
        yeniadet = 1   
        print(f"{yeniurun}; Fiyatı:{yeniücret}TL,Kategorisi:{yenikategori} ve stok adedi:{yeniadet} olarak kaydedildi.") 
        urun[yeniurun]= [yeniurun,yeniücret,yenikategori,yeniadet]
        urunonly[yeniurun]=[yeniurun,yeniücret,yenikategori,yeniadet]
        kategoriler.append(yenikategori.upper())
        tekrar()
    else:
        urunolustur() 

#Tekrar işlem yapılsın mı?
def tekrar():
    islem = input(Fore.YELLOW+"Tekrar işlem yapmak ister misiniz?(E/H)\n-->")
    while  islem.isdigit():
        islem = input(Fore.YELLOW+"Tekrar işlem yapmak ister misiniz?(E/H)")
    if islem == "e" or islem == "E":
        os.system("cls")
        menu()
    elif islem == "h" or islem =="H":
        os.system("cls")
        read = ""
        for i in "Görüşmek üzere...        ":
            read = read+i
            print(read)
            time.sleep(0.05)
            os.system("cls")
    else:
        print(Fore.RED+"Yanlış işlem seçimi (E/H)")
        tekrar()
        
#Anamenü
def menu():
                        
    print(Fore.YELLOW+"Lütfen İşlem Seçiniz:")
    time.sleep(0.15)
    print(Fore.YELLOW+"1)Mağaza")
    time.sleep(0.15)
    print(Fore.YELLOW+"2)Sepetim")
    time.sleep(0.15)
    print(Fore.YELLOW+"3)Kategoriler")
    time.sleep(0.15)
    print(Fore.YELLOW+"4)Ürün oluştur")
    
    islem = input("-->")
    if islem == "1":
       os.system("cls")
       magaza()

    elif islem == "2":
       os.system("cls")
       sepetim()

    elif islem == "3":
       os.system("cls")
       kategori()
    elif islem == "4":
        os.system("cls")
        urunolustur()
    else:
        os.system("cls")
        print(Fore.RED+"Yanlış İşlem girildi.Lütfen dikkat edin!")
        time.sleep(1.5)
        os.system("cls")
        menu()
        
#Mağazadaki tüm ürünleri göster
def magaza():
    max_isim = max(len(i[0]) for i in urun.values())
    max_fiyat = max(len(str(i[1])) for i in urun.values())
    max_kategori = max(len(i[2]) for i in urun.values())
    max_stok = max(len(str(i[3])) for i in urun.values())

    j = 1
    for i in urun.values():
        isim_padding = ' ' * (max_isim - len(i[0]))
        fiyat_padding = ' ' * (max_fiyat - len(str(i[1])) + 2)
        kategori_padding = ' ' * (max_kategori - len(i[2]))
        stok_padding = ' ' * (max_stok - len(str(i[3])))
        if j < 10:
            print(Fore.BLUE + f" {j}.) Ürün: {i[0]}{isim_padding} | Fiyatı:{fiyat_padding}{i[1]}TL | Kategori: {i[2]}{kategori_padding} | Stok Adeti: {i[3]}{stok_padding}")
        else:
            print(Fore.BLUE + f"{j}.) Ürün: {i[0]}{isim_padding} | Fiyatı:{fiyat_padding}{i[1]}TL | Kategori: {i[2]}{kategori_padding} | Stok Adeti: {i[3]}{stok_padding}")
        j += 1



    alınacak = input(Fore.GREEN+"Satın almak istediğiniz ürünün ismini girin(Menüye Dön:Q)\n-->")
    if alınacak.upper() == "Q":
        os.system("cls")
        menu()

    while  alınacak.isnumeric():
        alınacak = input(Fore.RED+"Lütfen İSİM girin\n-->")
    while not alınacak in urun:
        if alınacak not in urun:
                alınacak = input(Fore.RED+"Lütfen doğru ürün girin\n-->")
    
    urun[alınacak][3]= urun[alınacak][3] - 1
    urun[alınacak][4]= urun[alınacak][4] + 1
    if urun[alınacak][3] == 0:
        urun.pop(alınacak)



    sepet.append(alınacak)
    print(Fore.GREEN+f"{alınacak} Başarıyla sepete eklendi.")
    
    tekrar()

#Sepetimizi göster
def sepetim(): 
    j = 1
    toplam = 0
    for i in sepet:
        print(Fore.CYAN+f"{j}.)Ürün:",i,f"Fiyatı {urunonly[i][1]}TL Adeti:{urunonly[i][4]}")
        j +=1
        toplam = int(urunonly[i][1]) + toplam
    
    if not len(sepet) <= 0:
        print(f"Toplam Fiyat:{toplam}TL")
        sepetislem = input(Fore.YELLOW+"Sepet işlemleri:\n1)Sepeti boşalt\n2)Ürün sil\n3)Satın alımı tamamla\n4)Ana menüye dön\n-->")
        while not sepetislem.isdigit():
            sepetislem = input(Fore.RED+"İşlem numarası giriniz:\n1)Sepeti boşalt\n2)Ürün sil\n3)Satın alımı tamamla\n4)Ana menüye dön\n-->")

        if sepetislem == "1":
            for i in sepet:
                if not i in urun:
                    urun[i]=urunonly[i]

                urun[i][3]= urunonly[i][3] + 1
                urun[i][4]= urunonly[i][4] - 1

                
            sepet.clear()
            print(Fore.GREEN+"Başarıyla Temizlendi")

        elif sepetislem == "2":
            sil = input("Silinecek ürünün ismini giriniz\n-->")
            silici = sepet.index(sil)
            sepet.pop(silici)
            
            if not sil in urun:
                urun[sil]=urunonly[sil]

            urun[sil][3]= urunonly[sil][3] + 1
            
            print(Fore.GREEN+"Başarıyla Silindi!")

        elif sepetislem == "3":
            read = ""
            for i in Fore.GREEN+"Satın alımınız için teşekkürler...             ":
                read = read+i
                print(read)
                time.sleep(0.08)
                os.system("cls")
                sepet.clear()
                
                
        elif sepetislem == "4":
            os.system("cls")
            menu()  
    else:
        print(Fore.RED+"Sepette ürün bulunmuyor!")       
                               
    tekrar()

#Kategorileri listele
def kategori():
    j = 1
    for i in kategoriler:
        print(Fore.BLUE+f"{j}.) Kategori :",i)
        j += 1
    kategorisecin = input(Fore.YELLOW+"Bir kategori seçin(isim)(Menüye Dön:Q)\n-->")
    while i in urun.values():
        print(i[2])
        if not kategorisecin.upper() == i[2]:
            kategorisecin = input(Fore.RED+"Bir kategori seçin(isim)(Menüye Dön:Q)\n-->")

    if kategorisecin.upper() == "Q":
        os.system("cls")
        menu()
    while  kategorisecin.isdigit():
         kategorisecin = input(Fore.RED+"Lütfen isim olarak girin\n-->")
    j = 1
    work = False
    okay = False
    for i in urun.values():        
        if kategorisecin.upper() == i[2]:           
            print(Fore.BLUE+f"{j}.)Ürün:",i[0],f"Adeti:{i[3]}")
            j +=1
            
            okay = True
        
    if okay:
        alınacak = input(Fore.GREEN+"Satın almak istediğiniz ürünün ismini girin\n-->")
        while  alınacak.isnumeric():
            alınacak = input(Fore.RED+"Lütfen İSİM girin\n-->")
        for i in urun.values():
            if i[0] == alınacak.lower():
                work = True
        
    if work:
        urun[alınacak.lower()][3]= urun[alınacak.lower()][3] - 1
        urun[alınacak.lower()][4]= urun[alınacak.lower()][4] + 1
        if urun[alınacak.lower()][3] == 0:
            urun.pop(alınacak)
        sepet.append(alınacak.lower())
        print(Fore.GREEN+f"{alınacak} Başarıyla sepete eklendi.")
        tekrar()
    else:
        print(Fore.RED+"Aradığın kategori bulunmuyor!")
        tekrar()

text = ""
for i in "AcunMedyaAkademi Mağazasına hoşgeldin!              ":
    text = text+i
    print(Fore.CYAN+text)
    time.sleep(0.05)
    os.system("cls")

menu()

