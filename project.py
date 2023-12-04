import csv

dict = {}
study_groups = {'Music', 'Book', 'DVD'}


def read_archive():
    #archives = "teste.txt"
    archives = "amazon-meta.txt"

    file = open(archives, "r", encoding="UTF-8")
    lines = file.readlines()
    i = 0

    current_asin = None
    current_similarities = []
    current_group = None
    list_similarities = []
    no_similarities = 0
    categories_dict = {}
    customer_ids = {}

    for line in lines:
        study_line = line.strip()
        #searching for every type of object that exists in the dataset
        if study_line.startswith("group: "):
            current_group = study_line.split(":")[1].strip()
            #group exist in dictionary
            if study_line.split(":")[1].strip() in dict:
                dict[study_line.split(":")[1].strip()] += 1
            else:
                #group doesn't exist in dictionary
                dict[study_line.split(":")[1].strip()] = 1

        if study_line.startswith("ASIN: "):
            current_asin = study_line.split(":")[1]
            current_similarities = []

        if study_line.startswith("similar: 0") and (current_group in study_groups):
            no_similarities += 1

        elif study_line.startswith("similar: ") and (current_group in study_groups):
            similarities = [sim[0:] for sim in study_line.split()[2:]]
            current_similarities.extend(similarities)
            list_similarities.extend([(current_asin, sim) for sim in current_similarities])

        if study_line.startswith("|") and (current_group in study_groups):
            # Extracting the category and its number
            ###print(current_group)
            category_info = [line.strip() for line in study_line.split("\n") if line.startswith("|")]
            #category_info = [category.strip() for category in study_line.split("|")[1:-1]]

            for category in category_info:
                if category not in categories_dict:
                    categories_dict[category] = 1
                else:
                    categories_dict[category] += 1
            # ao ver uma categoria posso meter o numero à frente, ou seja A cat enters = 1, in another group i see her again, 2 and so on

        if study_line.strip() and study_line[0].isdigit() and (current_group in study_groups):
            customer_id = line.split()[2]
            # Check if the customer ID is already in the array
            if customer_id not in customer_ids:
                customer_ids[customer_id] = 1
            else:
                customer_ids[customer_id] += 1

    file.close()
    print("How many products are in the dataset?", dict)
    print("How many products with no co-purchases?", no_similarities)
    print("How many users are making reviews?", len(customer_ids))

    # with open("similarities.txt", "w", encoding="UTF-8") as output_file:
    # for asin, similar_object in list_similarities:
    # output_file.write(f"{asin} - {similar_object}\n")

    # Escrever no arquivo CSV
    with open("similarities.csv", "w", encoding="UTF-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=':')
        for asin, similar_object in list_similarities:
            csv_writer.writerow([asin, similar_object])

    with open("categories_output.txt", "w", encoding="UTF-8") as output_file:
        for category, id_category in categories_dict.items():
            output_file.write(f"{category}: {id_category}\n")

    with open("reviews.txt", "w", encoding="UTF-8") as output_file:
        for review, qnt_review in customer_ids.items():
            output_file.write(f"{review}: {qnt_review}\n")


read_archive()


# How many products are in the dataset? - DONE
# How many products with no co-purchases? (meaning the product does not have “similar products”) - DONE
# How many products per product type (book, movie or music)? - DONE
# How many product categories? - DONE
# How many products per category? -
# How many users are making reviews? - DONE
# How many reviews per user? - DONE
