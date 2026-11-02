from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def main():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    original_document = input("Enter document/message to sign: ").encode("utf-8")
    modified_document = input("Enter document/message to verify (same text for valid result): ").encode("utf-8")

    original_hash = SHA256.new(original_document)
    modified_hash = SHA256.new(modified_document)

    signature = pkcs1_15.new(private_key).sign(original_hash)
    print("Digital signature (hex):", signature.hex())

    try:
        pkcs1_15.new(public_key).verify(modified_hash, signature)
        print("Signature is valid.")
    except (ValueError, TypeError):
        print("Signature is invalid.")

if __name__ == "__main__":
    main()
