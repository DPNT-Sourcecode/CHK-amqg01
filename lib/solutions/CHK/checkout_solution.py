# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus:
        if skus.isupper():
            skus = (list(skus))
            A = skus.count('A')
            map = {'A':50,'B':30,'C':20,'D':15,'E':40,'Z':130,'Y':45, 'X':200}
            if skus.count('A') % 5 == 0 and skus.count('A')
            [x, y, what, the] = [(skus.count('A') // 3), (skus.count('A') % 3), (skus.count('A') // 5), (skus.count('A') % 5)]
            [i, j] = [(skus.count('B') // 2), (skus.count('B') % 2)]
            [c, d] = [skus.count('C'), skus.count('D')]
            skus = (x*'Z'+y*'A'+i*'Y'+j*'B'+c*'C'+d*'D'+what*'X'+the*'A')
            return(sum([map[x] for x in list(skus)]))
        else:
            return(-1)
    else:
        return 0

