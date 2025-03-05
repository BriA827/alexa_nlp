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
                
        for t in i.split("|"):
            if "\"" not in t:
                start = 0
                end = -1
                if ">" in t:
                    start = t.index(">") + 2
                if "\\" in t:
                    end = t.index("\\") 
                if t[start] == " ":
                    start += 1
                dic[line[0]]["tag"].append(t[start:end])

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
    order = [i for i in grammar.keys()]
    order.reverse()
    tags = []
    types = []
    val = ""
    construct = []
    sentence = None

    for o in order:
        for w in grammar[o]['tag']:
            tags.append(w)
            types.append(o)

    for i in valid:
        val = val + (i[0]) + " "
    
    
    for i in tags:
        if i in val:
            val = val.replace(i, types[tags.index(i)])

    if val == "S ":
        return True
    else:
        return False

###################################################

cfg = read_file("Simple_CFG.txt")
cfg_dic = cfg_to_dict(cfg)

# print(cfg_dic)

test = "The man saw a dog in the park with a telescope"

real, parse = valid_sentence(cfg_dic, test)
# print(real, parse)

final = parse_valid(cfg_dic, parse)
print(final)