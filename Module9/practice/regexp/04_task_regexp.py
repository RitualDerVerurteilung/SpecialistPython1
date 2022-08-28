# Дан текст:
text = "World War II began on Sep 1939 and ended on Sep 1945. Victory Day has been celebrated since 1945."
# Найдите и выведите все года, которым предшествует месяц.
# Уточнение: вывести ТОЛЬКО года, но те, ПЕРЕД которыми стоит месяц!

import re

text = "World War II began on Sep 1939 and ended on Sep 1945. Victory Day has been celebrated since 1945."
result1_0 = re.findall('[A-Z][a-z]{2}\s[0-9]{4}', text)
result1_1 = []
for el in result1_0:
    result1_1.append(el[-4:])
print(result1_1)
