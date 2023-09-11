

# Test 1

sl = input(' Введите слово: ')
resl = sl[::-1]
if resl==sl:
    print (' Это палиндром.')
else:
    print (' Это не палиндром.')
    


# Test 2 

print ('\n\n Введите строку для редактирования: ')
stroka = input()
sbp = stroka.split()
print (' '.join(sbp))

