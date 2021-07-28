import pyqrcode
import base45
import cbor2
import zlib
import png

from dict_type import data

# UPDATE : On essaye maintenant de partir de data modifiées :
data = data.CODED_DATA
print(data)
# Ici, on part d'une valeur de départ, qui correspond à la valeur de la variable decoded de vacdec.py
Data = cbor2.CBORTag(18, data)

# On remonte à cbordata
cbordata = cbor2.dumps(Data)

# On passe ensuite à zlibdata. Ici, problème avec le xda ( premier élément du string ). 
# On définit donc le compression level à 9, car c'est le niveau par défaut du module decompress...
zlibdata = zlib.compress(cbordata, 9)

# On remonte encore à b45data. On doit donc, à ce stade, avoir nos données encodées en base 45.
# Ici, on rencontre une "erreur" ( b'sting' ), dû au fait qu'on encode en utf-8 et que l'élément
# en sortie de b45encode est de type bytes... Si cela pose problème pour la suite, il faudra envisager
# un fix...
b45data = base45.b45encode(zlibdata)

# Pour remonter à cert, on doit simplement ajouter "HC1:" au début de la string ( qui est de type bytes !! )
# A ce stade, on est bien remonté. On a un objet bytes par contre. J'ignore si c'est le bon type de donnée
# pour continuer. Là encore, en cas de soucis, envisager un fix !!!
cert = b'HC1:'+b45data

# On test une création de QR code
file_utf = 'QR_utf.png'
qr_utf = pyqrcode.create(cert, encoding = 'utf-8') # Creates qr code using utf-8 encoding
qr_utf.png(file_utf, scale = 8)


