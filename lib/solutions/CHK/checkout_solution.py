# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus:
        if skus.isupper():
            skus = (list(skus))
            A, C, D, E, F = skus.count('A'), skus.count('C'), skus.count('D'), skus.count('E'), skus.count('F')
            prices = {'A':50,'B':30,'C':20,'D':15,'E':40,'F':10,'Z':130,'Y':45, 'X':200}

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

            #E LOGIC
            if 'B' in skus:
                for n in range(E // 2):
                    skus.remove('B')
            else:
                pass

            #B LOGIC
            B = skus.count('B')
            [i, j] = [B // 2, B % 2]
            print(B)
            #F Logic
            if 'F' in skus:
                for n in range(F // 3):
                    skus.remove('F')
            print(skus)
            F = skus.count('F')
            print(F,x,y,i,j,C,D,five_a,E)
            #Calculate Total
            skus = (x*'Z'+y*'A'+i*'Y'+j*'B'+C*'C'+D*'D'+five_a*'X'+E*'E'+F*'F')
            return(sum([prices[x] for x in list(skus)]))
        else:
            return(-1)
    else:
        return 0


