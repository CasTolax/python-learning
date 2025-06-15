def sayılarMenu():
        
        print("başlatmak için 1'e basabilir,çıkmak için ise q'a basabilirsiniz")
        soru = input("--: ")

        if soru == "1":
            print("başlatıldı...")
            print("lütfen istediğiniz sayıyı giriniz.")

            SayıAl = int(input("--: "))

            for i in range(SayıAl):
                print(i)

        elif soru == "q":
            print("program sonlandırıldı")
            
        else:
            print("hata,sadece 2 seçenek vardır 1/q")
            

sayılarMenu()

