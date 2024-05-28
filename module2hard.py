import random
list_1 = list(range(3, 21))
list_2 = list(range(1, 21))
n = random.choice(list_1)


def unical_par():
    list_unpar = []
    for i in (list_2):
        for j in range(i, len(list_2)):
            unic_par = [i, j]
            list_unpar.append(unic_par)
    return list_unpar


list_u_p = unical_par()
result = []
for i in list_u_p:
    if n % sum(i) == 0:
        result.append(i)

print('n =', n)
print('Пароль: ', result)