class HarfSayaci: #class Harfsayacı
    def __init__(self):
        self.sesli_harfler = "aeıioöuü" #sesli harfler
        self.sayac = 0

    def kelime_sor(self):
        return input("Bir kelime girin: ").lower() #kullanıcıdan alınacak 

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def artir(self): #eğer sesli harf var ise 
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac += 1
        return self.sayac

    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} sesli harf var."
        sesli_harf_sayisi = self.artir()
        print(mesaj.format(self.kelime, sesli_harf_sayisi))

    def calistir(self): #baslatır
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.calistir()
