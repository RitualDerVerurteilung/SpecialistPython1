# Проверить, является ли заданная строка доменным именем для протоколов http или https, с необязательным слешем в конце.
# Специальные символы не используются.
# Примеры:
# http://example.com/ — Да(является)
# example.com — Нет
# https://кремль.рф — Да

import re

domain = str(input())
result1 = re.search(r'http|https ://w+[.]w+', domain)
if not result1 == None:
    print('Yes')
else:
    print('No')
