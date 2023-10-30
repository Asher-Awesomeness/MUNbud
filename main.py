
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
    results_holder = []
    for t, i in enumerate(files):
        


print(get_search_inputs("<hi bro> <asher is cool>"))
