def Chiffrage(texte,cle):
    resultat = ""
    for lettre in texte:
        if lettre.isalpha():
            base = 'a' if lettre.islower() else'A'
            resultat += chr((ord(lettre) - ord(base) + cle) % 26 + ord(base))
        else:
            resultat += lettre
    return resultat
texte = input("Texte :")
cle = int(input("Clé :"))
print("Chiffré :", Chiffrage(texte,cle))
print("Déchiffré :", Chiffrage(Chiffrage(texte,cle), -cle))