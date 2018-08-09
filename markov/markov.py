def generate_table(s):
    result = {}
    list_word = list(s.split(" "))
    for word in list_word:
        result.setdefault(word, {})
    for word in result.keys():
        check_word = list(s.split(" "))
        temp = {}
        while True:

            next = list_word.index(word) + 1
            print(next)
            if next == len(list_word):
                break
            temp.setdefault(list_word[next], list_word.count(list_word[next]))
            check_word[next - 1] = ""
            if word not in check_word:
                break

        print(temp)
        result.setdefault(word, temp)
    return result

print(generate_table('i am daniel i am french i like jiu-jitsu'))
