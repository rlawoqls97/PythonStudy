while True:
    encrypted_secret_codes = input("Encrypted secret codes: ")
    # print(encrypted_secret_codes)
    pw = input('\nPassword to secret codes: ')

    key2codes = 0
    encrypted_secret_codes = encrypted_secret_codes.replace("{", "").replace("}", "").replace(":", "").replace(",", "").split(" ")
    for p in pw:
        key2codes += ord(p)

    key =[]
    value = []
    for i in range(len(encrypted_secret_codes)):
        encrypted_secret_codes[i] = int((encrypted_secret_codes[i])) - key2codes
        if i % 2 != 0:
            value.append(encrypted_secret_codes[i])
        else:
            key.append(chr(encrypted_secret_codes[i]))

    print("Secret codes (key-value reversed)")
    secret_code = dict(zip(value, key))
    print(secret_code)

    decrypt = input("Text to decrypt: ")
    dec_l = decrypt.split(",")

    coded_text = ''
    for c in dec_l:
        if c != '':
            coded_text += str(secret_code[int(c)])

    print(coded_text)

    more = input("\nDo you want to proceed to the next text decryption? (y) ")
    if more != 'y':
        break