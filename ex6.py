# Scrie un program care preia numărul de minute ca intrare și îl convertește în ore și minute.
# Afișează orele și minutele convertite.

minute=int(input('Introdu numarul de minute '))
ore=int(minute/60)
minute1=minute-(ore*60)
print(minute,'= cu', ore ,'ore si',minute1 ,'minute')