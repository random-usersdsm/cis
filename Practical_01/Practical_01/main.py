def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def rail_fence_encrypt(text):
    # Implements the odd/even-position transposition shown in the journal.
    return text[::2] + text[1::2]

def rail_fence_decrypt(cipher):
    half = (len(cipher) + 1) // 2
    first, second = cipher[:half], cipher[half:]
    return ''.join(
        first[i // 2] if i % 2 == 0 else second[i // 2]
        for i in range(len(cipher))
    )

def main():
    print("1. Caesar substitution cipher")
    print("2. Rail-fence-style transposition (odd/even positions)")
    choice = input("Choose 1 or 2: ").strip()
    message = input("Enter message: ")
    if choice == "1":
        shift = int(input("Enter shift (default 3): ") or "3")
        encrypted = caesar_cipher(message, shift)
        decrypted = caesar_cipher(encrypted, -shift)
    elif choice == "2":
        encrypted = rail_fence_encrypt(message)
        decrypted = rail_fence_decrypt(encrypted)
    else:
        print("Invalid choice.")
        return
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
