import hashlib

def main():
    clave = input("Ingresa el Hash: " )
    clave = clave.encode()

    md5 = hashlib.md5(clave).hexdigest()
    print("Hash MD5: " + md5)

    sha1 = hashlib.sha1(clave).hexdigest()
    print("Hash SHA1: " + sha1)

    sha224 = hashlib.sha224(clave).hexdigest()
    print("Hash SHA224: " + sha224)

    sha256 = hashlib.sha256(clave).hexdigest()
    print("Hash SHA256: " + sha256)

    sha384 = hashlib.sha384(clave).hexdigest()
    print("Hash SHA384: " + sha384)

    sha512 = hashlib.sha512(clave).hexdigest()
    print("Hash SHA512: " + sha512)


if __name__ == '__main__':
    main()