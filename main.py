alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(len(alphabet))

def encrypt(original_text , shift_amount ):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print(encrypted_text)
def decrypt(original_text , shift_amount ):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
    print(decrypted_text)

print("welcome")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode".lower():
    encrypt(text,shift)
if direction == "decode".lower():
    decrypt(text, shift)




