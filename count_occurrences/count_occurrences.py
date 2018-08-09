def count_occurrences(string):
    dic = {}
    list_word = string.split()
    s = set(string.split())
    for word in list_word:
        if word in s:
            if list_word.count(word) not in dic.keys():
                dic[list_word.count(word)] = [word]
            else:
                dic[list_word.count(word)].append(word)
                dic[list_word.count(word)].sort()
            s.remove(word)
    return dic
