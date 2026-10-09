def plural(noun):
    if noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'
    elif noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    else:
        return noun + 's'

words = ['cat', 'bus', 'box', 'baby', 'book']

for word in words:
    print(word, "->", plural(word))