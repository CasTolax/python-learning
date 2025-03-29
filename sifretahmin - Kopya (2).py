import os
from random import randint

pas = input("şifreyi girin ")

keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
        "u", "v", "w", "x", "y", "z"]

pwg = ""
while pwg != pas:
    pwg = ""
    for i in range(len(pas)):
        guessPass = keys[randint(0, 4)]
        pwg = str(guessPass) + str(pwg)
        print(pwg)
        print("şifre saldırsı yapılıyor bekleyin lütfen")
        os.system("cls")

print(f"The pass is: {pwg}")