#Scrie un program care preia două numere ca intrare și efectuează următoarele operații:
#
#    Adună cele două numere și afișează rezultatul.
#    Scade al doilea număr din primul număr și afișează rezultatul.
#    Înmulțește cele două numere și afișează rezultatul.
#    Împarte primul număr la al doilea număr și afișează rezultatul.

a=input()
b=input()
print('Valoarea initiala a lui a este',int(a))
print('Valoarea initiala a lui b este',int(b))
suma=int(a)+int(b)
diferenta=int(b)-int(a)
produs=int(a)*int(b)
divid=int(a)/int(b)
print('suma numerelor', a ,'si', b ,'este', suma)
print('Diferenta numerelor', b ,'si', a ,'este', diferenta)
print('Produsul numerelor', a ,'si', b ,'este', produs)
print('Impartirea numerelor', a ,'si', b ,'este', divid)