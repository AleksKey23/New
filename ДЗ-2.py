
#Zadanie 1

print(' Vvedite odnu iz storon pryamougolnika: ')
st1=float(input ())
print(' Vvedite vtoruyu storonu pryamougolnika: ')
st2=float(input ())
P=2*(st1+st2)
S=st1*st2

if st1==st2:
 print('Eto kvadrat!')
print(' Perimetr =  ', P, ', Ploshyad = ', S)



#Zadanie 2

print('\n\n Vvedite 5-znachnoe chislo:')
dt,t,s,d,e = map(float, input())
print('Otvet = ', (d**e)*s/(dt-t) )