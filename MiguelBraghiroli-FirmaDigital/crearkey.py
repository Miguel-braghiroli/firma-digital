#Miguel Braghiroli

from Crypto import Random
from Crypto.PublicKey import RSA

random_generator = Random.new().read
rsa = RSA.generate(1024, random_generator)
PrivateKey = rsa.exportKey()
with open("PrivateKey.txt", "wb") as f:
    f.write(PrivateKey);
PublicKey = rsa.publickey().exportKey()
with open("PublicKey.txt", "wb") as f:
    f.write(PublicKey);
print("Creacion de llaves Exitosa")