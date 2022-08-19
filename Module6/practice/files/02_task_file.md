## "Обработка файла <Лимерики>"

### Задание

Дан файл [data/limericks.txt](data/limericks.txt) с лимериками(короткими стихотворениями)

Выведите содержимое файла в новый файл **limericks_clean.txt**, удалив все символы точки из исходного файла

### Формат входных данных

Дан текстовый файл

### Формат выходных данных

Вывести содержимое исходного файла в новый, удалив все символы точек.

### Решение задачи

```python
lst =[]
with open('data/limericks.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.replace('.', '')
        lst.append(line)

with open('data/limericks_clean.txt.txt', 'w', encoding='UTF-8') as f:
    for i in range(len(lst)):
        f.write(lst[i])
    ...
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Для начала, выведите содержимое файла в консоль(терминал), чтобы убедиться что все работает без ошибок.
</details>

<details>
<summary>Подсказка-2</summary>
Работайте с файлом построчно:

Прочитали строку --> Удалили из нее символы точек --> Записали в новый файл
</details>

<details>
<summary>Подсказка-3</summary>
Для удаления символов из строки воспользуйтесь строковым методом .replace(".", "")
</details>
