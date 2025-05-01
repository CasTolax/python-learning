import os

kullanıcı_adiDosya = "kullanıcı_dosyası.txt"
kullanıcı_sifreDosya = "kullanıcıSifre_dosyası.txt"

def DosyaYonet():
    while True:
        print("\n -- Oyuncu Adı Ve Şifre Yöneticisi --")
        print("Seçeneklerden birisini seçin: ")
        print("1: Oyuncu Adları dosyasını aç")
        print("2: Oyuncu Şifrelerini dosyasını aç")
        print("3: Oyun Adı sil/ekle")
        print("4: Oyun Şifre sil/ekle")
        print("5: Bilgi al")
        print("6: Çıkış")

        secim = input("Seçim yapınız (1/2/3/4/5/6): ")

        if secim == "1":
            if os.path.exists(kullanıcı_adiDosya):
                with open(kullanıcı_adiDosya, "r", encoding="utf-8") as dosya:
                    satirlar = dosya.readlines()
                    for satir in satirlar:
                        print(satir.strip())
            else:
                print("Kullanıcı Adı dosyası bulunamadı.")

        elif secim == "2":
            if os.path.exists(kullanıcı_sifreDosya):
                with open(kullanıcı_sifreDosya, "r", encoding="utf-8") as dosya:
                    satirlar = dosya.readlines()
                    for satir in satirlar:
                        print(satir.strip())
            else:
                print("Kullanıcı Şifreleri dosyası bulunamadı.")

        elif secim == "3":
            sor = input("Silmek mi istiyorsunuz, eklemek mi? (1: Sil / 2: Ekle): ")

            if sor == "1":
                kadi_silinecek = input("Silmek istediğiniz kullanıcı adını girin: ")
                with open(kullanıcı_adiDosya, "r", encoding="utf-8") as dosya:
                    satirlar = dosya.readlines()
                with open(kullanıcı_adiDosya, "w", encoding="utf-8") as dosya:
                    for satir in satirlar:
                        if satir.strip() != kadi_silinecek:
                            dosya.write(satir)
                print(f"{kadi_silinecek} kullanıcı adı silindi.")
            elif sor == "2":
                ekleKullanci = input("Lütfen kullanıcı adı girin: ")
                with open(kullanıcı_adiDosya, "a", encoding="utf-8") as dosya:
                    dosya.write(ekleKullanci + "\n")
                    print(f"{ekleKullanci} kullanıcı ismi kaydedildi.")

        elif secim == "4":
            sor1 = input("Silmek mi istiyorsunuz, eklemek mi? (1: Sil / 2: Ekle): ")

            if sor1 == "1":
                sifre_silinecek = input("Silmek istediğiniz şifreyi girin: ")
                with open(kullanıcı_sifreDosya, "r", encoding="utf-8") as dosya:
                    satirlar = dosya.readlines()
                with open(kullanıcı_sifreDosya, "w", encoding="utf-8") as dosya:
                    for satir in satirlar:
                        if satir.strip() != sifre_silinecek:
                            dosya.write(satir)
                print(f"{sifre_silinecek} şifresi silindi.")
            elif sor1 == "2":
                ekleSifre = input("Eklemek istediğiniz şifreyi giriniz: ")
                with open(kullanıcı_sifreDosya, "a", encoding="utf-8") as dosya:
                    dosya.write(ekleSifre + "\n")
                    print(f"{ekleSifre} şifresi kaydedildi.")

        elif secim == "5":
            print("""Bu basit ve sade bir dosya yöneticisidir.
Oyun içi kullanıcı adı ve şifre kayıtları için kullanılabilir.""")

        elif secim == "6":
            print("Programdan çıkılıyor...")
            break

DosyaYonet()
