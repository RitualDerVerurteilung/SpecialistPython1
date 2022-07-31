## "Шахматы: слон"

### Задание

Требуется определить, бьет ли слон, стоящий на клетке с указанными координатами (номер строки и номер столбца), фигуру, стоящую на другой указанной клетке.

### Формат входных данных

Даны четыре числа целые числа в диапазоне [1, 8], координаты слона и координаты другой фигуры

### Формат выходных данных

Вывести "Да", если слон бьет фигуру или "Нет", если не бьет.

### Решение задачи

xf = int(input())
yf = int(input())
xs = int(input())
ys = int(input())
if xs == ys and xf == yf:
    print("Да")
elif ys - 1 == yf and (xs + 1 or xs - 1) == xf:
    print("Да")
elif ys - 2 == yf and (xs + 2 or xs - 2) == xf:
    print("Да")
elif ys - 3 == yf and (xs + 3 or xs - 3) == xf:
    print("Да")
elif ys - 4 == yf and (xs + 4 or xs - 4) == xf:
    print("Да")
elif ys + 1 == yf and (xs + 1 or xs - 1) == xf:
    print("Да")
elif ys + 2 == yf and (xs + 2 or xs - 2) == xf:
    print("Да")
elif ys + 3 == yf and (xs + 3 or xs - 3) == xf:
    print("Да")
elif ys + 4 == yf and (xs + 4 or xs - 4) == xf:
    print("Да")
else:
    print("Нет")
