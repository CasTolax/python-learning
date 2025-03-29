not1 = int(input("1.notonuzu giriniz"))
not2 = int(input("2.notonuzu giriniz"))
not3 = int(input("3.notonuzu giriniz"))
not4 = int(input("4.notonuzu giriniz"))
ortalama = (not1+not2+not3+not4)/4
if ortalama >= 85:
    print("Takdir aldınız")
elif ortalama >= 70:
    print("Teşekkür aldınız")
elif ortalama >= 50:
    print("Geçtiniz")
else:
    print("Kaldınız")