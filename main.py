
file_lists = {}


def get_search_inputs(search_input):
    record__ = False
    current_text = ""
    search_inputs = []
    for x in search_input:
        if record__ is True:
            if x == ">":
                record__ = False
                search_inputs.append(current_text)
                current_text = ""
            else:
                current_text += x
        elif x == "<":
            record__ = True
    return search_inputs


def search_files(files, link_codes, search_inputs):
    results = []
    results_holder = []
    results_to_add = []
    for t in files:
        with open(t) as file:
            for line, i in enumerate(file):
                results_to_add.append((line, t, i, link_codes[i]))
            for x in search_inputs:
                for y in results_to_add:
                    if x not in y[0]:
                        results_holder.append(results_to_add.pop(results_to_add.index(y)))
    for x in results_holder:
        if x[3] == 1:
            with open(x[1] + "_links") as file:
                results.append((x[0], file_lists[file][x[2]]))



print(get_search_inputs("<hi bro> <asher is cool>"))
