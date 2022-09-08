import base64
#Miguel Braghiroli

from hmac import digest
from inspect import signature
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

def firmar(mensaje):
    with open("PrivateKey.txt") as f:
        key = f.read()
        rsakey = RSA.importKey(key);
        signer = Signature_pkcs1_v1_5.new(rsakey);
        digest = SHA.new();
        mensaje = input("\n Ingrese los datos que desea almacenar: ")
        with open("datos.txt", "a", encoding="utf-8") as f:
            f.write(mensaje + "\n")
        print("Contenido de la Documentacion: ", mensaje);
        print("HASH generado: ", digest.hexdigest());
        sign = signer.sign(digest);
        signature = base64.b64encode(sign);
    with open('firma.txt', 'wb') as pf1:
        pf1.write(signature);
        pf1.close();
    print("La firma que desea crear es:", signature);
    print("Su Firma Fue Guardada En El Archivo firma.txt");
    return signature;
with open('datos.txt', "r") as f1:
    mensaje = f1.read();
mensaje =  mensaje.encode();
signature = firmar(mensaje);