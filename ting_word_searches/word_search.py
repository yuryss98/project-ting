def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        result_dict = {
                    "palavra": word,
                    "arquivo": instance.search(i)['nome_do_arquivo'],
                    "ocorrencias": []
                }

        for j in range(len(instance.search(i)['linhas_do_arquivo'])):
            row = instance.search(i)['linhas_do_arquivo'][j]
            if word.lower() in row.lower():
                result_dict['ocorrencias'].append({"linha": j + 1})

        if len(result_dict['ocorrencias']):
            result.append(result_dict)

    return result


def search_by_word(word, instance):
    result = []

    for i in range(len(instance)):
        result_dict = {
                    "palavra": word,
                    "arquivo": instance.search(i)['nome_do_arquivo'],
                    "ocorrencias": []
                }

        for j in range(len(instance.search(i)['linhas_do_arquivo'])):
            row = instance.search(i)['linhas_do_arquivo'][j]
            if word.lower() in row.lower():
                result_dict['ocorrencias'].append({
                    "linha": j + 1,
                    'conteudo': row
                })

        if len(result_dict['ocorrencias']):
            result.append(result_dict)

    return result
