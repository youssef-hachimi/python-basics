# print("################# chiffre de Cesar #########")
# message= input("Entrer le messqge a chiffre : ")
# key= int(input("Entrer le key a chiffre "))#(doit etre enter 1-26):
# # Letters = []
# letters = 'abcdefghijklmnopqrstuvwxyz'
# def chiffre(message,key):
#     chphertext = ""
#     for letter in message:
#         letter = letter.lower()
#         if not letter == '':
#             index = letters.find(letter)
#             if index == -1:
#              chphertext += letter
#             else:
#                 new_index = index + key
#                 if new_index > 26:
#                     new_index -= 26
#                 chphertext+= letters[new_index]
#                 return chphertext
# chiphertext = chiffre(message,key)
# print(chiphertext)
#


print("########## Chiffre de César ##########")

message = input("Entrer le message à chiffrer : ")
key = int(input("Entrer la clé (1-26) : "))

letters = 'abcdefghijklmnopqrstuvwxyz'

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
            ciphertext += letter  # caractères non alphabétiques inchangés
    return ciphertext

ciphertext = chiffre(message, key)
print("Message chiffré :", ciphertext)

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
