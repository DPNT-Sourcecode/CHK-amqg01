# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    map = {'A':50, 'B':30, 'C':20, 'D':15}

    return sum([map[x] for x in list(skus)])

    [x, y] = [(list(skus).count('A') // 3), (list(skus).count('A') % 3)]
    [i, j] = [(list(skus).count('B') // 2), (list(skus).count('B') % 2)]




