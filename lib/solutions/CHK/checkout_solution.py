# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    map = {'A':50, 'B':30, 'C':20, 'D':15}

    return sum([map[x] for x in list(skus)])

    if list(skus).count('A') % 3 == 0:
        



