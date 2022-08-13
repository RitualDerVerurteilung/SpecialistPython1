# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tupl1 = (1, 2, 3, 4)
tupl2 = (4, 1, 2, 8)
tupl3 = (-2, 2, 7, 1)

itog = 0
i = 0
e = 0
f = 0

while True:
    if len(tupl1) == i:
        break
    if tupl1[i] == tupl2[e] == tupl3[f]:
        itog += 1
        i += 1
        e = 0
        f = 0
    e += 1
    if len(tupl3) - 1 == f and len(tupl2) == e:
        i += 1
        e = 0
        f = 0
    if len(tupl2) == e:
        e = 0
        f += 1
print(itog)
