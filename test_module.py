import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['main.py', 'readme.md']


def test_program():
    for file in files_list:
        assert file in dir_files, f'Файл `{file}` не найден в корне папки'
