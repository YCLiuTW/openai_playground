import os


def check_file_exist(file_):
    if not os.path.isfile(file_):
        raise FileExistsError(f'File {file_} is not exist!')
