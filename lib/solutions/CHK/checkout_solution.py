# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus:
        if skus.isupper():
            skus = (list(skus))
            A = skus.count('A')
            map = {'A':50,'B':30,'C':20,'D':15,'E':40,'Z':130,'Y':45, 'X':200}
            if A % 5 == 0 and A > 0:
                [five_a , y] = [A // 5, A % 5]
            else:
                [x, y] = [A // 3, A % 3]
            [i, j] = [(skus.count('B') // 2), (skus.count('B') % 2)]
            [c, d] = [skus.count('C'), skus.count('D')]
            skus = (x*'Z'+y*'A'+i*'Y'+j*'B'+c*'C'+d*'D'+five_a*'X')
            return(sum([map[x] for x in list(skus)]))
        else:
            return(-1)
    else:
        return 0


