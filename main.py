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
    valid = True
    tup = []

    for i in sentence.split():
        for o in order:
            for w in grammar[o]["word"]:
                    if i == w:
                        tup.append((o,i))
                    elif i.lower() == w:
                        tup.append((o,i))

        if tup[-1][-1] != i:
            valid = False


    if valid:
        return valid, tup
    else:
        return valid, []

def parse_valid(grammar, valid):
    construct = []
    sentence = None

    for i in valid:
        print(i[0])
        for w in grammar[o]["tag"]:
            if i == w:
                tup.append((i,w))
            elif i.lower() == w:
                tup.append((i,w))


###################################################

cfg = read_file("Simple_CFG.txt")
cfg_dic = cfg_to_dict(cfg)

# print(cfg_dic)

test = "The man saw a dog in the park with a telescope"

real, parse = valid_sentence(cfg_dic, test)

parse_valid(cfg_dic, parse)