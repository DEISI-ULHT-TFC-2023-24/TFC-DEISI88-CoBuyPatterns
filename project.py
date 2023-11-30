dict = {}
study_groups = {'Music', 'Book', 'DVD'}

def read_archive():
    archives = "teste.txt"

    #archives = "amazon-meta.txt"

    file = open(archives, "r", encoding="UTF-8")
    lines = file.readlines()
    i = 0

    current_asin = None
    current_similarities = []
    current_group = None
    list_similarities = []
    no_similarities = 0
    categories_dict = {}

    for line in lines:
        test = line.strip()
        #searching for every type of object that exists in the dataset
        if test.startswith("group: "):
            #group exist in dictionary
            if test.split(":")[1].strip() in dict:
                dict[test.split(":")[1].strip()] += 1
                current_group = test.split(":")[1].strip()

            else:
                #group doesn't exist in dictionary
                dict[test.split(":")[1].strip()] = 1
                current_group = test.split(":")[1].strip()

        if test.startswith("similar: 0"):
            no_similarities += 1

        elif test.startswith("similar: "):
            similarities = [sim[0:] for sim in test.split()[2:]]
            current_similarities.extend(similarities)

        # Check if the line is empty, indicating the end
        elif not test:
            # Add ASIN and its similarities to the list
            list_similarities.extend([(current_asin, sim) for sim in current_similarities])

        if test.startswith("ASIN: "):
            current_asin = test.split(":")[1].strip()
            current_similarities = []

        if test.startswith("|") and (current_group in study_groups):
            # Extracting the category and its number
            ###print(current_group)
            category_info = [category.strip() for category in test.split("|")[1:-1]]

            for category in category_info:
                if category not in categories_dict:
                    categories_dict[category] = ''

    file.close()
    print(dict)
    print(no_similarities)

    with open("similarities.txt", "w", encoding="UTF-8") as output_file:
        for asin, similar_object in list_similarities:
            output_file.write(f"{asin} - {similar_object}\n")

    # Write the categories to a file
    with open("categories_output.txt", "w", encoding="UTF-8") as output_file:
        for category, id_category in categories_dict.items():
            output_file.write(f"{category}: {id_category}\n")


read_archive()


# How many products are in the dataset? - DONE
# How many products with no co-purchases? (meaning the product does not have “similar products”) - DONE
# How many products per product type (book, movie or music)? - DONE
# How many product categories? - DONE
# How many products per category? -
# How many users are making reviews? -
# How many reviews per user? -
