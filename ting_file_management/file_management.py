import sys


def txt_importer(path_file):
    try:
        if not path_file.lower().endswith(".txt"):
            return print("Formato inválido", file=sys.stderr)

        with open(path_file, "r") as file:
            text = file.readlines()
            return [i.replace('\n', '') for i in text]

    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
