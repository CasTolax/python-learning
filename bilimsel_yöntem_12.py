def main():
    baslatma()
    if not problem():
        return
    if not gozlenme():
        return
    if not tutarlılık():
        return
    if not hipotez1():
        return
    kuram()

def baslatma(): # kodun başlangıc yeri
    print("bilimsel yönteme hoşgeldiniz")
    secim1 = input("1:başlamak için 1'e tıklayınız veya 2:çıkmak için 2'e tıklayın")
    if secim1 == "1":
        print("program başlatıldı")
    elif secim1 == "2":
        print("program sonlandırıldı")
    else:
        print("hata:herhangi değer veya farklı değer girildi")

baslatma()

def problem(): #problem tespit
     
     soru1 = input("Problem tespit edildi mi?(e/h): ")
     if soru1 == "e":
        problem1 = input("problemi yazınız lütfen: ")
        print("problem tespit edildi: ",problem1)
     elif soru1 == "h":
           cıkıs2 = input("Problem yok,sistem sonlandırıldı(devam etmek istiyormusunuz?(e/h): ")
     elif cıkıs2 == "e":
            print("sistemi yeniden başlatmanız gereklidir")
     elif cıkıs2 == "h":
              print("sistem sonlandırılıyor..")

problem()

def gozlenme(): #gözlenme veya araştırma bilgisi var mı?
   soru1 = input("Problem gözlenme/araştırma bilgisi var mıdır?(e/h):")
   if soru1 == "e":
       soru2 = input("bilgi varsa yazdırın lütfen: ")
       print("döküman: ",soru2)
   elif soru1 == "h":
       print("öyleyse devam edemezsiniz(lütfen programı yeniden başlatın)")
   else:
       print("o halde devam edilemez")

gozlenme()   

def tutarlılık(): #tutarlımı değil mi? değilse ise başa döndür
    soru1 = input("araştırmalar tutarlımı?(e/h): ")
    if soru1 == "e":
        print("devam edin lütfen")
    elif soru1 == "h":
        print("o halde devam edemezsiniz(sistemi tekrar çalıştırın)")
    else:
        print("hata:değer veya bilgi girişi olamdı(404)")

tutarlılık()

def hipotez1():
    soru1 = input("Hipotezleriniz oluşturuldu mu?(savunma(e/h)): ")
    if soru1 == "e":
    
      ana_dusunce = input("Hipotezin ana düşüncesi: ")
      savunma = input("Savunması: ")
      arastirma = input("Araştırması: ")
      gozlem = input("Gözlemler: ")
      tahmin = input("Tahminler: ")
      tutarlilik = input("Tutarlı mı? (e/h): ")

    elif soru1 == "h":
        print("şuanda devam dahi edemezsiniz(bunları girmeniz gerek,sistemi yeniden başlatın)")
        soru3 = input("1:programı kapatmak için 1'e tıklayınız lütfen")
        print(soru3)
    else:
        print("hata:yanlış değer veya girinti elde edildi(404)")
    
hipotez1()

def kuram():
    soru1 = input("Son aşama:Tüm koşullar tamamlandı mı?(e/h): ")
    if soru1 == "e":
        print("koşullar doğrulandı")
        print("Teori olşturuldu,tebrikler")
        isim = input("Teori ismi nedir?: ")
        print("tebrikler bilime bir şey daha kazanıldı İsim ise: ", isim)
    elif soru1 == "h":
        print("hipotezi büyütmeye devam edin o halde(geri dönün,veya yeniden başlatın.)")
    else:
        print("herhangi bir giriş olmadı veya yanlış girildi(402)")
    
kuram()