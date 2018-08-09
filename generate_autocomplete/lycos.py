def generate_autocomplete(words):
    result = {}
    return words;
    for dic in words:
        for arr_word in dic.keys():
            for w in arr_word:
                if w not in result.keys():
                    result[w] = []
    return result

print(generate_autocomplete(['a', 'abc', 'abd', 'abd', 'b']))
