def is_duplicate(data, key, value):
    for c in data.keys():
        if c != key:
            return 'Everything fine'
        else:
            print 'Duplicate value exists. Reassignment done.'
    return data


res = is_duplicate({'one': 'a', 'two': 'b', 'three': 'c'}, 'four', 'five')
print(res)
res2 = is_duplicate({'one': 'a', 'two': 'b', 'three': 'c'}, 'three', 'five')
print(res2)