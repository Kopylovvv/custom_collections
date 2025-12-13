# Симуляция с пользовательсĸими ĸоллеĸциями и псевдослучайной моделью

Библиотека, поддерживающая интерактивную работу с книгами через командную строку

CLI через typer и click_shell и запуск через uv.

ввод команд в одной и той же программе. библиотека сохраняет все действия пока не завершится прорамма, симуляция использует ту же библиотеку что и пользователь

## команды

добавить книгу
```commandline
add
```

убрать книгу
```commandline
rm <isbn>
```

показать книги в библиотеке
```commandline
ls
```

найти книгу по isbn, году, жанру или автору
```commandline
find <param> [-y|-g|-a]
```

запустить симуляцию
```commandline
simulate
```



## установка и запуск
1. Клонировать репозиторий и перейти в папку проекта
```commandline
git clone https://github.com/Kopylovvv/custom_coolections.git
cd custom_collectioons
```
2. Создать и активировать окружение `uv`
```commandline
uv venv
source .venv/bin/activate
```
3. Установить зависимости
```commandline
uv sync
```
4. Вызов команд
```commandline
python -m main 
```
5. Запуск тестов
```commandline
uv run pytest
```
