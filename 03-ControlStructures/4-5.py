plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_code = ord(char)
    if 'a' <= char <= 'z':
        new_code = ord('a') + (char_code - ord('a') + 1) % 26
        encrypted_char = chr(new_code)
    elif 'A' <= char <= 'Z':
        new_code = ord('A') + (char_code - ord('A') + 1) % 26
        encrypted_char = chr(new_code)
    else:
        encrypted_char = char

    encrypted_text += encrypted_char

print(plain_text)
print(encrypted_text)