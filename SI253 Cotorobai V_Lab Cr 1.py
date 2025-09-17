englez = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
    "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
    "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
    "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
    "Y": 24, "Z": 25
}
n = len(englez)


def code(pt, k):
    cipher = ''
    for i in pt:
        if i not in englez:
            continue
        else:
            for key, value in englez.items():
                if value == ((englez.get(i) + k) % n):
                    cipher += key
    return cipher


def decode(cipher, k):
    plaintext = ''
    for i in cipher:
        if i not in englez:
            continue
        else:
            for key, value in englez.items():
                if value == ((englez.get(i) - k) % n):
                    plaintext += key
    return plaintext


def code_two_keys(pt, k1, k2):
    cipher = ''
    k2 = k2.upper()
    n = len(englez)
    j = 0
    for ch in pt.upper():
        if ch not in englez:
            continue
        shift = k1 + englez[k2[j % len(k2)]]
        new_val = (englez[ch] + shift) % n
        for key, value in englez.items():
            if value == new_val:
                cipher += key
                break
        j += 1
    return cipher


def decode_two_keys(cipher, k1, k2):
    plaintext = ''
    k2 = k2.upper()
    n = len(englez)
    j = 0
    for ch in cipher.upper():
        if ch not in englez:
            continue
        shift = k1 + englez[k2[j % len(k2)]]
        new_val = (englez[ch] - shift) % n
        for key, value in englez.items():
            if value == new_val:
                plaintext += key
                break
        j += 1
    return plaintext


print("Pentru Cezar cu o cheie, tasteaza 1."
      "\nPentru Cezar cu doua chei, tasteaza 2."
      "\nPentru a renunta, tasteaza 0.")
tip = int(input())

while tip != 0:
    print("Pentru a cripta, tasteaza 1."
          "\nPentru a decripta, tasteaza 2."
          "\nPentru a renunta, tasteaza 0.")
    ans = int(input())

    if ans == 0:
        break

    if tip == 1:
        cheie = int(input("Introdu cheia (1-25): "))
        if cheie < 1 or cheie > 25:
            print("Valoarea cheiei trebuie sa fie intre 1 si 25.")
            continue

        if ans == 1:
            text = input("Introdu textul: ").upper()
            print(f"Mesajul criptat este: {code(text, cheie)}")
        elif ans == 2:
            cifru = input("Introdu cifrul: ").upper()
            print(f"Mesajul decriptat este: {decode(cifru, cheie)}")

    elif tip == 2:
        cheie1 = int(input("Introdu cheia numerică (1-25): "))
        if cheie1 < 1 or cheie1 > 25:
            print("Valoarea cheiei trebuie sa fie intre 1 si 25.")
            continue

        cheie2 = input("Introdu cheia alfabetică (min 7 litere): ").upper()
        if not cheie2.isalpha() or len(cheie2) < 7:
            print("Cheia alfabetică trebuie să conțină doar litere și să aibă cel puțin 7 caractere.")
            continue

        if ans == 1:
            text = input("Introdu textul: ").upper()
            print(f"Mesajul criptat este: {code_two_keys(text, cheie1, cheie2)}")
        elif ans == 2:
            cifru = input("Introdu cifrul: ").upper()
            print(f"Mesajul decriptat este: {decode_two_keys(cifru, cheie1, cheie2)}")

    print("\nPentru Cezar cu o cheie, tasteaza 1."
          "\nPentru Cezar cu doua chei, tasteaza 2."
          "\nPentru a renunta, tasteaza 0.")
    tip = int(input())
