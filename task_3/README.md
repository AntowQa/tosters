### Заполните файл settings.py
#### Обязательно заполнить

- BASE_URL - адрес главной страницы сайта

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
### Запуск теста в docker контейнере

- make build-tests
- make run-tests
