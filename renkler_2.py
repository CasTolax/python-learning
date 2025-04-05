renkler = {
    1: {
        "açık renkler": [
            "kırmızı",
            "yeşil",
            "sarı"
        ]
    },
    2: {
    "koyu renkler": [
        "lacivert",
        "bordo",
        "zümrüt yeşili"
    ]
    }
}

def renkler_yazdır():
    secim = input("renkler 1:açık renkler 2:koyu renkler (1/2): ").strip().upper()
    
    if secim == "1":
        print("Açık renkler:", renkler[1]["açık renkler"])
        for renk in renkler[1]["açık renkler"]:
            print(renk)
    elif secim == "2":
        print("koyu renkler:", renkler[2]["koyu renkler"])
        for renk in renkler[2]:
            print(renk)
    
            
    

renkler_yazdır()