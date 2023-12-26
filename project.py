import csv
from collections import Counter

dict = {}
study_groups = {'Music', 'Book', 'DVD'}

#para cada objeto quero: id, grupo, categorias, {'user_x' : comment}


def read_archive():
    #archives = "teste.txt"
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

    for line in lines:
        study_line = line.strip()
        #searching for every type of object that exists in the dataset
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


        #filtered_categories = {category: frequency for category, frequency in result.items() if frequency > 2}

        # file -> ASIN - GROUP(CURRENT GROUP) - SIMIL - CATEGORY - COMENTARIOS
        # ao ver uma categoria posso meter o numero à frente, ou seja A cat enters = 1, in another group i see her again, 2 and so on

        if study_line.strip() and study_line[0].isdigit() and (current_group in study_groups):
            parts = line.split()
            user_id = parts[2]
            rating = parts[4]
            customer_ids.append(f"{user_id} - {rating}")

        if not study_line and (current_group in study_groups):
            palavras = [palavra for sublista in estrutura_final for palavra in sublista]
            contagem_palavras = Counter(palavras)
            palavras_mais_frequentes = [palavra for palavra, frequencia in contagem_palavras.most_common()]

            organized_lines = [current_asin, current_group, current_title, current_similarities,
                               palavras_mais_frequentes, customer_ids]

            with open(organized_file, mode='a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(organized_lines)

            customer_ids = []
            current_title = []
            result = []
            palavras = []
            estrutura_final = []

    file.close()
    # with open("similarities.txt", "w", encoding="UTF-8") as output_file:
    # for asin, similar_object in list_similarities:
    # output_file.write(f"{asin} - {similar_object}\n")
    with open('output.txt', mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)


read_archive()


# How many products are in the dataset? - DONE
# How many products with no co-purchases? (meaning the product does not have “similar products”) - DONE
# How many products per product type (book, movie or music)? - DONE
# How many product categories? - DONE
# How many products per category? - DONE
# How many users are making reviews? - DONE
# How many reviews per user? - DONE
