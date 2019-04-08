# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus:
        if skus.isupper():
            skus = (list(skus))
            A = skus.count('A')
            map = {'A':50,'B':30,'C':20,'D':15,'E':40,'Z':130,'Y':45, 'X':200}
            five_a, x, y = 0, 0, 0
            if A > 0 and A >= 5:
                [five_a , y] = [A // 5, A % 5]
            else:
                if y == 0:
                    [x, y] = [A // 3, A % 3]
                else:
                    [x, y] = [y // 3, y % 3]
            [i, j] = [(skus.count('B') // 2), (skus.count('B') % 2)]
            [c, d, e] = [skus.count('C'), skus.count('D'), skus.count('E')]
            skus = (x*'Z'+y*'A'+i*'Y'+j*'B'+c*'C'+d*'D'+five_a*'X'+e*'E')
            return(sum([map[x] for x in list(skus)]))
        else:
            return(-1)
    else:
        return 0




