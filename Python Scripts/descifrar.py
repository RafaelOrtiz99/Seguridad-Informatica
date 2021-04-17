import hashlib

def main():
    resolverHash = input("Hash a descifrar: ")
    resolverHash = resolverHash.encode()

    resolvedor = open("diccionario.txt", 'r')

    for x in resolvedor.readlines():
        a = x.strip("\n")
        a = a.encode()
        a = hashlib.sha1(a).hexdigest()
    
        if a == resolverHash: 
            print("Password: {} Este Hash fue el resuelto {}".format(x,a))

if __name__ == '__main__':
    main()