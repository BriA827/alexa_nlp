def read_file(file):
    file = open(file, "r")
    file = file.readlines()
    return file

def cfg_to_dict(list):
    dic = {}

    for i in list:
        line = i.split()
        dic[line[0]] = {"word": [], "tag":[]}
        for l in line[2:]:
            if l == "|":
                pass
            elif "\"" in l:
                dic[line[0]]["word"].append(l[1:-1])
            else:
                dic[line[0]]["tag"].append(l)

    return dic

def valid_sentence(grammar, sentence):
    order = [i for i in grammar.keys()]
    order.reverse()
    
    for i in sentence.split():
        print(i.lower())

###################################################

cfg = read_file("Simple_CFG.txt")
cfg_dic = cfg_to_dict(cfg)

# print(cfg_dic)

test = "The man saw a dog in the park with a telescope"

valid_sentence(cfg_dic, test)