def bdmi(dic):
    result = {}
    list_actor = []
    for arrs in dic.values():
        for arr in arrs:
            if arr not in list_actor:
                list_actor.append(arr)
    for actor in list_actor:
        for movie in dic.keys():
            if actor in dic[movie]:
                result.setdefault(actor, []).append(movie)
    return result
