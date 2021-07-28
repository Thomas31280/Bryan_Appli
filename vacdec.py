#!/usr/bin/env python

import sys
import zlib
import pprint

import PIL.Image
import pyzbar.pyzbar
import base45
import cbor2

data = pyzbar.pyzbar.decode(PIL.Image.open("QR_utf.png"))

print('data :', data)

cert = data[0].data.decode()

print('data [0] :', data[0])
print()

b45data = cert.replace("HC1:", "")

zlibdata = base45.b45decode(b45data)

cbordata = zlib.decompress(zlibdata)

decoded = cbor2.loads(cbordata)          # On définit une variable qui correspond à la valeur décodée de cbordata. Il faut donc unload cette variable pour retourner à cbordata.

print('decoded :', decoded)
print()
print('decode_value', decoded.value)
print()
print('decoded_Value_[2] :', decoded.value[2])

pprint.pprint(cbor2.loads(decoded.value[2]))

# print("Step 1 (cert) : ", cert)
# print("Step 2 (b45data) : ", b45data)
# print("Step 3 (zlibdata) : ", zlibdata)
# print("Step 4 (cbordata) : ", cbordata)
# print("Step 5 (decoded) : ", decoded)