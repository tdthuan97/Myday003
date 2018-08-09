def merge_dict(dictionaries):
    result = {}
    for dic in dictionaries:
        for arr_word in list(dic.keys()):
            for w in arr_word:
                if w not in result.keys():
                    result.setdefault(w, [])
    for word in list(result.keys()):
        for dic in dictionaries:
            for w in dic.keys():
                if word == w:
                    result[w].append(dic[w])
    return result
