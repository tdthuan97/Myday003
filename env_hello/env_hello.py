

def env_hello():
    from os import environ
    s = str(environ)
    p = s.find('LANGUAGE')
    if p == -1:
        p = s.find('LANG')
        p += 8
    else:
        pos += 12
    if s[p: p + 5] == 'fr_FR':
        return 'Bonjour!'
    return 'Hello!'
