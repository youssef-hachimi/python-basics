print("########## Chiffre de César ##########")

letters = 'abcdefghijklmnopqrstuvwxyz'


# --- Fonction de CHIFFREMENT ---
def chiffre(message, key):
    ciphertext = ""
    for letter in message:
        letter_lower = letter.lower()

        if letter_lower in letters:
            index = letters.find(letter_lower)
            new_index = (index + key) % 26
            new_letter = letters[new_index]

            if letter.isupper():
                new_letter = new_letter.upper()

            ciphertext += new_letter
        else:
            ciphertext += letter
    return ciphertext


# --- Fonction de DÉCHIFFREMENT ---
def dechiffre(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter_lower = letter.lower()

        if letter_lower in letters:
            index = letters.find(letter_lower)
            new_index = (index - key) % 26
            new_letter = letters[new_index]

            if letter.isupper():
                new_letter = new_letter.upper()

            plaintext += new_letter
        else:
            plaintext += letter
    return plaintext


# menu
print("Que voulez-vous faire ?")
print("1 - Chiffrer un message")
print("2 - Déchiffrer un message")

choice = input("Votre choix (1/2) : ")

message = input("Entrer le message : ")
key = int(input("Entrer la clé (1-26) : "))

if choice == "1":
    result = chiffre(message, key)
    print("\n Message chiffré :", result)

elif choice == "2":
    result = dechiffre(message, key)
    print("\n Message déchiffré :", result)

else:
    print("\n Choix invalide.")
