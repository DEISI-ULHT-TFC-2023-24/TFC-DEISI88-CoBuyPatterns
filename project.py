import csv

dict = {}
study_groups = {'Music', 'Book', 'DVD'}

#para cada objeto quero: id, grupo, categorias, {'user_x' : comment}


def read_archive():
    #archives = "teste.txt"
    archives = "amazon-meta.txt"

    file = open(archives, "r", encoding="UTF-8")
    lines = file.readlines()

    organized_file = open('output.txt', 'w')
    current_asin = None
    current_similarities = []
    current_group = None
    list_similarities = []
    no_similarities = 0
    category_info = []
    customer_ids = []
    category_list = []
    unique_third_positions = set()

    for line in lines:
        study_line = line.strip()
        #searching for every type of object that exists in the dataset
        if study_line.startswith("group: "):
            current_group = study_line.split(":")[1].strip()

        if study_line.startswith("ASIN: "):
            current_asin = study_line.split(":")[1]
            current_similarities = []

        elif study_line.startswith("similar: ") and (current_group in study_groups):
            similarities = [sim[0:] for sim in study_line.split()[2:]]
            current_similarities.extend(similarities)
            list_similarities.extend([(current_asin, sim) for sim in current_similarities])

        if study_line.startswith("|") and (current_group in study_groups):
            lines = [line.strip() for line in study_line.split('\n') if line.startswith('|')]
            result = []
            for line in lines:
                parts = line.split('|')[1:-1]
                position = parts[2].split('[')[0].strip() if len(parts) > 2 else None
                result.append(position)
            # file -> ASIN - GROUP(CURRENT GROUP) - SIMIL - CATEGORY - COMENTARIOS
            # ao ver uma categoria posso meter o numero à frente, ou seja A cat enters = 1, in another group i see her again, 2 and so on

        if study_line.strip() and study_line[0].isdigit() and (current_group in study_groups):
            parts = line.split()
            user_id = parts[2]
            rating = parts[4]
            if len(customer_ids) < 5:
                customer_ids.append(f"{user_id} - {rating}")

        if not study_line and (current_group in study_groups):
            organized_file.write(f"{current_asin} , {current_group} , {current_similarities} , {result} , "
                                 f"{customer_ids}\n")
            customer_ids = []

    file.close()
    # with open("similarities.txt", "w", encoding="UTF-8") as output_file:
    # for asin, similar_object in list_similarities:
    # output_file.write(f"{asin} - {similar_object}\n")
    # Escrever no arquivo CSV
    with open('output.txt', 'r') as organized_file:
          conteudo = organized_file.read()


read_archive()


# How many products are in the dataset? - DONE
# How many products with no co-purchases? (meaning the product does not have “similar products”) - DONE
# How many products per product type (book, movie or music)? - DONE
# How many product categories? - DONE
# How many products per category? -
# How many users are making reviews? - DONE
# How many reviews per user? - DONE
