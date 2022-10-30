import os
from settings import PATH_FILES_SITE


def get_all_file_site() -> list:
    path = os.getcwd()
    list_files = os.listdir(f'{path}{PATH_FILES_SITE}')
    return list_files


def get_css_files() -> list:
    files = get_all_file_site()
    return [file for file in files if file.endswith(".css") and file.find('headers.css') == -1]
