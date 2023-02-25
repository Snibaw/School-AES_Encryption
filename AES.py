from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

texte = "QnJhdm8gISBWb3VzIGV0ZXMgcGFydmVudSBhIGRlY29kZXIgdW4gbWVzc2FnZSBlbiBiYXNlNjQgISAgICAgIA=="
double_cpyher = "I2vizvsCLxYmTQOW/+swdmf1/0V1lDWgx989YPW5H3qL4PycVyFFsV8DfOvZIQti0t+zSWVtaoFBOkA8vJmySw=="
secret_cipher = "dwfuRvQvBc32b5KZbtf3gfL0yNMpR/cr1VudpW9V+YohPnjt6WLrMLo4EfMHGSjbQDieLFTsDq2ECRZBhI+7Nh9W0RVg3hDF3jC04L/tJUvIrFw94veCWuRXNisuTtmg"
taille = 2**24

message_dict = {}


def creerCle(i):
    cle = [0]*32
    j = int(i / 2**16)
    cle[-3] = j
    k = int(i/2**8)-j*2**8
    cle[-2] = k
    l = i-j*2**16-k*2**8
    cle[-1] = l
    return cle


texte2 = base64.b64decode(texte)
trouve = 0
double_cypher_2 = base64.b64decode(double_cpyher)
for i in range(taille):
    cle_1 = creerCle(i)
    cle_1 = bytes(cle_1)
    cipher = AES.new(cle_1, AES.MODE_ECB).encrypt(texte2)
    message_dict[cipher] = cle_1
    if i % 100000 == 0:
        print(i)
for j in range(taille):
    cle_2 = creerCle(j)
    cle_2 = bytes(cle_2)
    cipher2 = AES.new(cle_2, AES.MODE_ECB).decrypt(double_cypher_2)
    if cipher2 in message_dict:
        print(cle_2, message_dict[cipher2])
        break
    if j % 100000 == 0:
        print(j)

cle__1 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9a\xe8\x07'
cle__2 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff?E'
secret_cipher_64 = base64.b64decode(secret_cipher)
x = AES.new(cle__2, AES.MODE_ECB).decrypt(secret_cipher_64)
y = AES.new(cle__1, AES.MODE_ECB).decrypt(x)
print(y)
