import random
import string

def parola_olustur(uzunluk = 21):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    parola = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return parola

print("oluşturulan parola: ", parola_olustur(21))
