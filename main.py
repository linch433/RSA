def is_prime(a):
    if a == 2:
        return True
    elif (a < 2) or ((a % 2) == 0):
        return False
    elif a > 2:
        for i in range(2, a):
            if not (a % i):
                return False
    return True


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def coprime(a, b):
    return gcd(a, b) == 1


def extended_gcd(x, y):
    if y == 0:
        return x, 1, 0
    d, a, b = extended_gcd(y, x % y)
    return d, b, a - (x // y) * b


def encrypt(message, public_key):
    key, n = public_key
    numbers = []
    for letter in message:
        number = ord(letter) - 96
        numbers.append(number)
    int_cipher = []
    for digits in numbers:
        c = pow(digits, key, n)
        int_cipher.append(c)
    return int_cipher


def decrypt(encrypt_mes, private_key):
    key, n = private_key
    int_cipher = []
    for digits in encrypt_mes:
        c = pow(digits, key, n)
        int_cipher.append(c)
    return int_cipher


def el_sign(hash, main_key):
    key, n = main_key
    el_sign = pow(hash, key, n)
    return el_sign

# main
p = int(input("Enter p: "))
q = int(input("Enter q: "))

check_p = is_prime(p)
check_q = is_prime(q)

while (check_p == False) or (check_q == False):
        p = int(input("Enter a prime number for p: "))
        q = int(input("Enter a prime number for q: "))
        check_p = is_prime(p)
        check_q = is_prime(q)


n = p * q
print("n = p * q: ", n)
phi = (p - 1) * (q - 1)
print("phi = (p - 1) * (q - 1): ", phi)
E = int(input("Enter open key E: "))

while not coprime(E, phi):
    print("Your E not gcd for phi = (p - 1) * (q - 1)")
    E = int(input("Enter open key E: "))

public_key = (E, n)
_, D, _ = extended_gcd(E, phi)
if D < 0:
    D = D + phi
private_key = (D, n)
print("Your private D:", D)

with open("message") as file:
    message = file.read()
    print("Your message: ", message)

numbers = []
for letter in message:
  number = ord(letter) - 96
  numbers.append(number)


print("Indexes from alphabet: ", numbers)
hashing = 0
for num in numbers:
    hashing = hashing + num


hashing1 = 0
hashing1 = hashing % n
print("Hash function: ", hashing1)
electronic_signature = el_sign(hashing1, private_key)
print("Electronic signature: ", electronic_signature)

signature_message = (message, electronic_signature)


encrypt_msg = encrypt(message, public_key)
f = open('crypted', 'wt')
for i in encrypt_msg:
    em = str(i)
    f.write(em + ' ')


f.close()
print("Encrypt message:", encrypt_msg)

verify_electronic_signature = el_sign(electronic_signature, public_key)
print("Verify electronic signature: ", verify_electronic_signature)

decrypt_msg = decrypt(encrypt_msg, private_key)
print("Decrypt message:", decrypt_msg)

decrypt_msg_ascii1 = []
for i in decrypt_msg:
  number = i + 96
  decrypt_msg_ascii1.append(number)


print("Your decrypted message: ", ''.join(map(chr, decrypt_msg_ascii1)))



