# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus:
        if skus.isupper():
            skus = (list(skus))
            A, C, D, E  = skus.count('A'), skus.count('C'), skus.count('D'), skus.count('E')
            map = {'A':50,'B':30,'C':20,'D':15,'E':40,'Z':130,'Y':45, 'X':200}

            #A LOGIC
            five_a, x, y = 0, 0, 0
            if A > 0 and A >= 5:
                [five_a , y] = [A // 5, A % 5]
                [x, y] = [y // 3, y % 3]
            else:
                if y == 0:
                    [x, y] = [A // 3, A % 3]
                else:
                    [x, y] = [y // 3, y % 3]

            #EE LOGIC
            if 'B' in skus:
                for i in range(E // 2):
                    skus.remove('B')
            else:
                pass

            #B LOGIC
            B = skus.count('B')
            [i, j] = [B // 2, B % 2]

            #Calculate Total
            skus = (x*'Z'+y*'A'+i*'Y'+j*'B'+C*'C'+D*'D'+five_a*'X'+E*'E')
            return(sum([map[x] for x in list(skus)]))
        else:
            return(-1)
    else:
        return 0

