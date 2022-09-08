#Miguel Braghiroli

from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

def verify(mensaje, signature):
    with open("PublicKey.txt") as f:
        key = f.read()
        rsakey = RSA.importKey(key);
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(mensaje)
        print("Calculando Hash de documento recibido ", digest.hexdigest())
        print("Desencriptamos la firma, para obtener el Hash original")
        is_verify = verifier.verify(digest, base64.b64decode(signature))
    if is_verify:
        print("Los Hash coinciden entre ellos")
        print("Documento no alterado")
    else:
        print("Los Hash no coinciden")
        print("Documento alterado")
with open("datos.txt", "r") as f1:
    mensaje = f1.read()
with open("firma.txt", "r") as f2:
    signature = f2.read()
mensaje = mensaje.encode()
verify(mensaje, signature)