# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    map = {'A':50,'B':30,'C':20,'D':10,'E':150,'F':45}
    [x, y] = [(list(skus).count('A') // 3), (list(skus).count('A') % 3)]
    [i, j] = [(list(skus).count('B') // 2), (list(skus).count('B') % 2)]
    [c, d] = [list(skus).count('C'), list(skus).count('D')]
    skus = (x*'E'+y*'A'+i*'F'+j*'B'+c*'C'+d*'D')
    return(sum([map[x] for x in list(skus)]))




