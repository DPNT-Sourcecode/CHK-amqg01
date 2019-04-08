# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    try:
        [x, y] = [(list(skus).count('A') // 3), (list(skus).count('A') % 3)]
        [i, j] = [(list(skus).count('B') // 2), (list(skus).count('B') % 2)]
        total = (x*130 + y*50) + (i*45 + y*30)
        skus.remove('A')
        skus.remove('B')
        map = {'C':20, 'D':15}
        total += sum([map[x] for x in list(skus)])

        return total
    except:
        -1


