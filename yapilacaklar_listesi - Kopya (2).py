def menu():
    print("\n yapılacaklar listesi")
    print("1- görev ekle")
    print("2- görevleri listele")
    print("3- görev sil")
    print("4- çıkış")

while True:
    menu()
    choice = input("seçiminizi yapınız: ")

    if choice == "4":
        print("çıkış yapılıyor")
        break
    else:
        print("geçerli bir seçenek giriniz.")