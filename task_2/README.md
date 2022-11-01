### Заполните файл settings.py
#### Обязательно заполнить

- BASE_URL - путь расположения файла index.html

##### Примеры для UNIX:
```
BASE_URL = "file:///home/anton/tosters/task_2/site/index.html"
```
##### Примеры для WINDOWS(любой из вариантов):
```
BASE_URL = "C:/Projects/tosters/task_2/site/index.html"
или
BASE_URL = "file:///C:/Projects/tosters/task_2/site/index.html"
```

#### По желанию заполнить(по умолчанию цвета уже заполнены)

- DEFAULT_COLOR - цвет, который используется в header.css
- PATH_FILES_SITE - относительный путь до файлов сайта

### Установка зависимостей

UNIX:
- sudo apt install python3-pip
- pip install -r requirements.txt (запустить из папки выгруженной из репозитория)

WINDOWS:
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py
- pip install -r requirements.txt (запустить из папки выгруженной из репозитория)

### Запуск теста

```
pytest tests/test_base_page.py
```


