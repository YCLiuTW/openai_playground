import os


def check_file_exist(file_):
    if not os.path.isfile(file_):
        raise FileExistsError(f"File {file_} is not exist!")


def check_folder_exist(folder_):
    if not os.path.isdir(folder_):
        raise FileExistsError(f"Folder {folder_} is not exist!")
