alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plaintext: str,key):
    plaintext = plaintext.lower()
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i] in alfabeto:
            p = alfabeto.index(plaintext[i])
            k = alfabeto.index(key[i % len(key)])
            c = (p + k) % 26
            ciphertext += alfabeto[c]
        else:
            ciphertext += plaintext[i]

    return ciphertext

def decrypt(ciphertext,key):
    plaintext = ''

    for i in range(len(ciphertext)):
        if ciphertext[i] in alfabeto:
            p = alfabeto.index(ciphertext[i])
            k = alfabeto.index(key[i % len(key)])
            c = (p - k) % 26
            plaintext += alfabeto[c]
        else:
            plaintext += ciphertext[i]
    return plaintext


print('1 negoceia 2 desnegoceia')
opcao = input()
if opcao == '1':
    plainetxt = input()
    key = input()
    ciphertext = encrypt(plainetxt, key)
    print(ciphertext)

elif opcao == '2':
    ciphertext = input()
    key = input()
    plaintext = decrypt(ciphertext, key)
    print(plaintext)


def find_key_size(ciphertext):
    found = False
    period = 0
    iocs = []
    for i in range(30):
        period += 1
        slices = [''] * period
        for i in range(len(ciphertext)):
            slices[i % period] += ciphertext[i]
        sum = 0
        for i in range(period):
            sum += index_of_coincidence(slices[i])
        ioc = sum / period
        iocs.append(ioc)
