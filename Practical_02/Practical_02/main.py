import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def main():
    # 2048-bit key is used for a safer modern demonstration.
    key_pair = RSA.generate(2048)
    public_key = key_pair.publickey()
    private_key = key_pair

    print("Public key generated.")
    print(public_key.export_key().decode("ascii"))
    print("Private key generated (keep this secret).")

    message = input("Enter message to encrypt: ").encode("utf-8")
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(message)
    print("Encrypted (hex):", binascii.hexlify(encrypted).decode("ascii"))

    decryptor = PKCS1_OAEP.new(private_key)
    decrypted = decryptor.decrypt(encrypted)
    print("Decrypted:", decrypted.decode("utf-8"))

if __name__ == "__main__":
    main()
