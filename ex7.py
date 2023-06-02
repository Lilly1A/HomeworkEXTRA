# Scrie un program care preia suma principală, rata dobânzii și timpul (în ani) ca intrare.
# Calculează și afișează dobânda simplă folosind formula:
# dobândă = (suma principală * rată dobândă * timp) / 100.

sumaprincipala=int(input('Introduceti suma principala '))
rata=int(input('introduceti rata dobanzii '))
timp=int(input('introduceti timpul '))
dobanda=int((sumaprincipala * rata * timp) / 100)
print('dobanda calculata este ', dobanda)