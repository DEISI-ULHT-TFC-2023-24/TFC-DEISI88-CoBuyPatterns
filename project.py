import csv
from collections import Counter
import pandas as pd

dict = {}
study_groups = {'Music', 'Book', 'DVD'}
dfs = []


def read_archive():
    # archives = "teste.txt"
    archives = "amazon-meta.txt"

    file = open(archives, "r", encoding="UTF-8")
    lines = file.readlines()

    organized_file = 'output.csv'
    current_asin = None
    current_similarities = []
    current_group = None
    list_similarities = []
    current_title = []
    result = {}
    customer_ids = []
    estrutura_final = []
    palavras_mais_frequentes = ""

    for line in lines:
        study_line = line.strip()
        # searching for every type of object that exists in the dataset
        if study_line.startswith("group: "):
            current_group = study_line.split(":")[1].strip()

        if study_line.startswith("ASIN: "):
            current_asin = study_line.split(":")[1]
            current_similarities = []

        if study_line.strip().startswith("title"):
            title = line.split(":", 1)[1].strip()
            # Append the title to the array
            current_title.append(title)

        elif study_line.startswith("similar: ") and (current_group in study_groups):
            similarities = [sim[0:] for sim in study_line.split()[2:]]
            current_similarities.extend(similarities)
            list_similarities.extend([(current_asin, sim) for sim in current_similarities])

        if study_line.strip().startswith("|") and (current_group in study_groups):
            split_items = study_line.strip().split("|")[1:]

            # Step 2: Exclude the first two elements from the split result, and split each remaining item by "["
            split_items = split_items[2:]
            parts = [item.split("[")[0] for item in split_items]
            estrutura_final.append(parts)

        if study_line.strip() and study_line[0].isdigit() and (current_group in study_groups):
            parts = line.split()
            user_id = parts[2]
            rating = parts[4]
            customer_ids.append(f"{user_id} - {rating}")

        if not study_line and (current_group in study_groups):
            palavras = [palavra for sublista in estrutura_final for palavra in sublista]
            contagem_palavras = Counter(palavras)
            if contagem_palavras:
                palavra_mais_frequente = contagem_palavras.most_common(1)[0][0]
            else:
                palavra_mais_frequente = ""

            organized_lines = [current_asin, current_group, current_title, current_similarities,
                               palavras_mais_frequentes, customer_ids]

            customer_ids = []
            current_title = []
            result = []
            palavras = []
            estrutura_final = []
            current_group = None

            columns = ['id', 'tipo', 'titulo', 'categorias', 'reviews', 'similaridades']
            # Iterar sobre cada linha

            id = organized_lines[0]
            tipo = organized_lines[1]
            titulo = organized_lines[2]
            similaridades = organized_lines[3]
            categoria = organized_lines[4]
            customer_ids = organized_lines[5]

            # Convert lists to strings
            titulo = str(titulo).strip("[]").replace("'", "")
            similaridades = str(similaridades).strip("[]").replace("'", "")

            data_dict = {
                'id': id,
                'tipo': tipo,
                'titulo': titulo,
                'categorias': categorias,
                'reviews': customer_ids,
                'similaridades': similaridades
            }

            dfs.append(data_dict)

    file.close()


read_archive()
x = pd.DataFrame(dfs)
x