from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        search = instance.search(i)
        if search['nome_do_arquivo'] == path_file:
            return

    text_lines = txt_importer(path_file)

    file_dict = {
        'nome_do_arquivo':  path_file,
        'qtd_linhas': len(text_lines),
        'linhas_do_arquivo': text_lines
    }

    instance.enqueue(file_dict)
    print(file_dict, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
