# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus:
        if skus.isupper():
            map = {'A':50,'B':30,'C':20,'D':15,'E':40,'Z':130,'Y':45}
            [x, y, what, the] = [(list(skus).count('A') // 3), (list(skus).count('A') % 3), (list(skus).count('A') // 5), (list(skus).count('A') % 5)]
            [i, j] = [(list(skus).count('B') // 2), (list(skus).count('B') % 2)]
            [c, d] = [list(skus).count('C'), list(skus).count('D')]
            skus = (x*'Z'+y*'A'+i*'Y'+j*'B'+c*'C'+d*'D'+what*'X'+the*'A')
            return(sum([map[x] for x in list(skus)]))
        else:
            return(-1)
    else:
        return 0




