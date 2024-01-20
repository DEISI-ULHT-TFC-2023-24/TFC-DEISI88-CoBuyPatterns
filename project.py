# limpeza de dados e produçao do datagram
import csv
from collections import Counter
import pandas as pd

study_groups = {'Music', 'Book', 'DVD'}
dict = {}
dfs = []
dfs_cats = []
dfs_similars = []


def read_archive():
    archives = "amazon-meta.txt"

    file = open(archives, "r", encoding="UTF-8")
    lines = file.readlines()
    asin = None
    similarities = []
    group = None
    list_similarities = []
    title = []
    customer_ids = []
    cats_list = []
    most_frequent_categories = ""

    for line in lines:
        study_line = line.strip()
        # obter o grupo
        if study_line.startswith("group: "):
            group = study_line.split(":")[1].strip()

        # obter id do produto
        if study_line.startswith("ASIN: "):
            asin = study_line.split(":")[1]
            similarities = []

        # obter titulo do produto
        if study_line.strip().startswith("title"):
            current_title = line.split(":", 1)[1].strip()
            # Append the title to the array
            title.append(current_title)

        # obter lista de produtos semelhantes
        if study_line.startswith("similar: ") and (group in study_groups):
            similarities = [sim[0:] for sim in study_line.split()[2:]]
            similarities.extend(similarities)
            list_similarities.extend([(asin, sim) for sim in similarities])

        # obter categorias - 1º retiramos o espaço, 2º retiramos o '|', 3º retiramos os numero identificador da categoria
        if study_line.strip().startswith("|") and (group in study_groups):
            try:
                # obtermos a categoria na posiçao 3 (colocamos 3 no array porque contamos com o espaço)
                word_in_cats_list = study_line.strip().split('|')[3]
                word_in_cats_list = word_in_cats_list.split("[")[0]
            except:
                word_in_cats_list = ""

            cats_list.append(word_in_cats_list)

        # obter user id e rating de utilizadores que efetuaram avaliaçoes ao produto
        if study_line.strip() and study_line[0].isdigit() and (group in study_groups):
            parts = line.split()
            user_id = parts[2]
            rating = parts[4]
            customer_ids.append(f"{user_id} - {rating}")

        # quando chegamos ao fim da  informaçao de um dado produto, vamos agregar toda a informaçao ena lista-> organized_lines
        if not study_line and (group in study_groups):
            # começamos por verificar qual a catefgoria que é mais frequente
            categories = [categorie for categorie in cats_list]
            categories_count = Counter(categories)
            if categories_count:
                most_frequent_categories = categories_count.most_common(1)[0][0]
            else:
                most_frequent_categories = ""

            # colocamos a informaçao do produto na lista
            organized_lines = [asin, group, title, similarities, most_frequent_categories, customer_ids]

            customer_ids = []
            title = []
            categories = []
            cats_list = []
            group = None

            data_dict = {
                'id': organized_lines[0],
                'group': organized_lines[1].strip("[]").replace("'", ""),
                'title': organized_lines[2],
                'similarities': organized_lines[3],
                'categories': organized_lines[4],
                'reviews': organized_lines[5]
            }
            dfs.append(data_dict)

            data_dict = {
                'id': organized_lines[0],
                'categories': organized_lines[4]
            }
            dfs_cats.append(data_dict)

            data_dict = {
                'id': organized_lines[0],
                'similarities': organized_lines[3]
            }

            dfs_similars.append(data_dict)

    file.close()


read_archive()
full_dataSet_datagram = pd.DataFrame(dfs)
catsDatagram = pd.DataFrame(dfs_cats)
similarsDatagram = pd.DataFrame(dfs_similars)

full_dataSet_datagram
catsDatagram

dvd = full_dataSet_datagram[full_dataSet_datagram.group == 'DVD']
dvd

book = full_dataSet_datagram[full_dataSet_datagram.group == 'Book']
book

music = full_dataSet_datagram[full_dataSet_datagram.group == 'Music']
music

df_exploded = similarsDatagram.explode('similarities')
df_exploded


#obter as 10 categorias mais frequentes
y = full_dataSet_datagram[full_dataSet_datagram.tipo == 'DVD'].copy()
study_categories = y[['categories','id']].groupby('categories').count().sort_values(by='id', ascending =False).head(5).index.to_list()
study_categories

#criar um datagram com toda a informaçao, mas somente das 10 categorias mais frequentes de um dado tipo de produto
z = y[y.categories.isin(study_categories)]
z.explode('similarities')[['id','similarities']].to_csv('test2.csv', index=False)
z