

# Test 3 

print (' Введите два целых числа А и В, чтобы выполнялось условие A ≤ B')
A = int(input(' Введите число А: '))
B = int(input(' Введите число B: '))
while (A>B):
    print (' Должно выполняться условие A ≤ B !!!')
    A = int(input(' Введите число А: '))
    B = int(input(' Введите число B: '))
if (A%2==0):
    for i in range (A, B+1, 2):
       print (i, end = ' ' )
else:
    for i in range (A+1, B+1, 2):
       print (i, end = ' ' )
       


# Test 1

x = int(input('\n\n Введите кол-во вводимых чисел: '))
rn=0
for i in range (x):
    ch=int(input(' Введите число: '))
    if ch==0:
        rn=rn+1
print (rn, ' - столько чисел из введенных равны нулю')



# Test 2

nch=int(input('\n\n Введите натуральное число: '))
kolnat=0
while (nch<=0):
    nch=int(input('Это число не натуральное, введите натуральное число: '))
for i in range(1, nch+1):
    if nch%i==0:
        kolnat +=1
print(' Количество натуральных делителей введенного числа - ', kolnat)