# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

        [x, y] = [(list(skus).count('A') // 3), (list(skus).count('A') % 3)]
        [i, j] = [(list(skus).count('B') // 2), (list(skus).count('B') % 2)]
        total = (x*130 + y*50) + (i*45 + y*30)
        map = {'C':20, 'D':15}
        print(list(skus))
        total += sum([map[x] for x in skus])
        return total





