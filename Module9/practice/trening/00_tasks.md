## Практические задания на regExp

Ресурс для проверки регулярок: [тут](https://regex101.com/).

### Задание-0 “Разминка”

#### Часть-1:

Даны строки: **cats. 8967. ?=+!. abcd1**

Напишите шаблон, который будет соответствовать первым трем строкам, но не соответствовать последней.

Соответствовать: <font color="green">cats. </font>

Соответствовать: <font color="green">8967. </font>

Соответствовать: <font color="green">?=+!. </font>

Пропустить:		<font color="red">abcd1</font>
import re
test = 'cats. 8967. ?=+!. abcd1'
result = re.findall(r'[0-9A-Za-z\W]{4}[.]', test)
print(result)


#### Часть-2:
Даны строки: **can man fan dan**

Напишите шаблон, который будет соответствовать первым трем строкам, но не соответствовать трем последним.\

Соответствовать	<font color="green">can</font>

Соответствовать	<font color="green">man</font>

Соответствовать	<font color="green">fan</font>

Пропустить		<font color="red">dan</font>

Пропустить		<font color="red">ran</font>

Пропустить		<font color="red">pan</font>
import re
test = 'can man fan dan ran pan'
result = re.findall(r'[cmf]an', test)
print(result)


#### Часть-3:

Для строк ниже напишите выражение, которое будет соответствовать как полной дате, так и только годам.

Точно известно: название месяца начинается с большой буквы и состоит из трех букв. \
А год состоит из четырех цифр.

| Дано                          | Извлечь-1         | Извлечь-2 |
| -----------------             | -----------       |----------- |
| Date Jan 1987                 | Jan 1987          |1987
| In May 1969                   | May 1969          |1969
| The war ended on 8 May 1945   | May 1945          |1945

import re
test = 'Date Jan 1987'
result1 = re.findall(r'[A-Z][a-z]{2}\s[0-9]{4}', test)
print(result1)
result2 = re.findall(r'[0-9]{4}', test)
print(result2)
