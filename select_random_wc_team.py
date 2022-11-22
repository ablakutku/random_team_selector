import random

grupA = ["Katar" , "Ekvador" , "Senegal" , "Hollanda"]
grupB = ["İngiltere" , "Iran" , "ABD" , "Galler"]
grupC = ["Arjantin" , "Suudi Arabistan" , "Meksika" , "Polonya"]
grupD = ["Fransa" , "Avustralya" , "Tunus" , "Danimarka"]
grupE = ["İspanya" , "Kosta Rika", "Almanya" , "Japonya"]
grupF = ["Belçika" , "Kanada" , "Fas" , "Hırvatistan"]
grupG = ["Sırbistan" , "Kamerun" , "Brezilya" , "İsviçre"]
grupH = ["Portekiz" , "Gana" , "Uruguay" , "Kore Cumhuriyeti"]

gruplar = [grupA, grupB, grupC, grupD, grupE, grupF, grupG, grupH]
rastgele_takım = random.choice(gruplar)

print("Takımınız: " + random.choice(rastgele_takım))