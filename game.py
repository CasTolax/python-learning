import time
import random
import sys

class Oyuncu():
    def __init__(self, isim, can=5, enerji=100):
        self.isim = isim
        self.darbe = 0
        self.can = can
        self.enerji = enerji

    def mevcut_durum(self):
        print(f"{self.isim} durumu:")
        print("  Darbe: ", self.darbe)
        print("  Can: ", self.can)
        print("  Enerji: ", self.enerji)

    def saldır(self, rakip):
        print("\nBir saldırı gerçekleştirdiniz.")
        print("Saldırı sürüyor... Bekleyin.")

        for i in range(10):
            time.sleep(0.2)
            print(".", end="", flush=True)

        sonuc = self.saldır_sonucunu_hesapla()

        if sonuc == 0:
            print("\nSonuç: Kazanan taraf yok.")
        elif sonuc == 1:
            print("\nSonuç: Rakibinizi darbelediniz.")
            self.darbele(rakip)
        elif sonuc == 2:
            print("\nSonuç: Rakibinizden hasar aldınız.")
            rakip.darbele(self)

    def saldır_sonucunu_hesapla(self):
        return random.randint(0, 2)

    def kac(self):
        print("\nKaçılıyor...")

        for i in range(5):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print("\nRakibiniz sizi yakaladı!")

    def darbele(self, darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -= 1
        if darbelenen.darbe % 5 == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print(f"\nOyun bitti! Kazanan: {self.isim}")
            self.oyundan_cik()

    def oyundan_cik(self):
        print("Oyun sonlandırılıyor...")
        sys.exit()

# Oyuncular
sen = Oyuncu("Can")
rakip = Oyuncu("Mehmet")

# Oyun Başlangıcı
while True:
    print("\nŞu anda rakibinizle karşı karşıyasınız.")
    print("Yapmak istediğiniz hamle:")
    print("  Saldır: s")
    print("  Kaç   : k")
    print("  Çık   : q")
    
    hamle = input("\nHamleniz: ").lower()

    if hamle == "s":
        sen.saldır(rakip)
    elif hamle == "k":
        sen.kac()
    elif hamle == "q":
        sen.oyundan_cik()
    else:
        print("Geçersiz hamle. Lütfen 's', 'k' veya 'q' girin.")

    print("\nDurumlar:")
    sen.mevcut_durum()
    rakip.mevcut_durum()


