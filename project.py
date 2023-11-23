dict = {}

def ler_arquivo():
    arquivo = "amazon-meta.txt"
    f = open(arquivo, "r", encoding="UTF-8")
    lines = f.readlines()

    for line in lines:
        if "group: " in line.strip():
            if line.split(":")[1].strip() in dict:
                dict[line.split(":")[1].strip()] += 1
            else:
                dict[line.split(":")[1].strip()] = 1

    f.close()
    print(dict )

ler_arquivo()