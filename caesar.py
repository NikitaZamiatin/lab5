def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char not in 'йцукенгшщзхъфывапролджэячсмитьбю' and char not in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                continue
            if char.islower():
                encrypted_text += chr((ord(char) - ord('а') + shift) % 33 + ord('а'))
            else:
                encrypted_text += chr((ord(char) - ord('А') + shift) % 33 + ord('А'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char not in 'йцукенгшщзхъфывапролджэячсмитьбю' and char not in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                continue
            if char.islower():
                decrypted_text += chr((ord(char) - ord('а') - shift) % 33 + ord('а'))
            else:
                decrypted_text += chr((ord(char) - ord('А') - shift) % 33 + ord('А'))
        else:
            decrypted_text += char
    return decrypted_text

text = input("Введите текст на русском языке, все буквы иных алфавитов будут отсутствовать в ответе: ")
shift = int(input("Введите шаг сдвига: "))

encrypted_text = caesar_encrypt(text, shift)
print("Результат зашифровки:", encrypted_text)

decrypted_text = caesar_decrypt(text, shift)
print("Результат расшифровки:", decrypted_text)