# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        [x, y] = [(list(skus).count('A') // 3), (list(skus).count('A') % 3)]
        [i, j] = [(list(skus).count('B') // 2), (list(skus).count('B') % 2)]
        [c, d] = [list(skus).count('C'), list(skus).count('D')]
        total = (x*130 + y*50) + (i*45 + y*30) + (c*20 + d*15)
        print(total)
    except:
        -1







