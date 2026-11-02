import hashlib
import hmac

def main():
    # MD5 digest demonstration as shown in the journal.
    for name in ("Priya", "Rajak"):
        digest = hashlib.md5(name.encode("utf-8")).digest()
        print(f"The byte equivalent of hash({name}):", digest)

    # SHA-1 hexadecimal digest demonstration as shown in the journal.
    text = input("\nEnter value to encode with SHA-1: ")
    print("The Hexadecimal Equivalent of SHA1 is:")
    print(hashlib.sha1(text.encode("utf-8")).hexdigest())

    # Actual message authentication code (MAC) demonstration using HMAC-SHA256.
    message = input("\nEnter message for HMAC: ").encode("utf-8")
    key = input("Enter shared secret key: ").encode("utf-8")
    tag = hmac.new(key, message, hashlib.sha256).hexdigest()
    print("HMAC-SHA256:", tag)
    check = hmac.new(key, message, hashlib.sha256).hexdigest()
    print("MAC verification:", "VALID" if hmac.compare_digest(tag, check) else "INVALID")

if __name__ == "__main__":
    main()
