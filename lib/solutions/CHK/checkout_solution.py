# noinspection PyUnusedLocal
# skus = unicode string
def remove_letters(letter, list):
    for i in list:
	    if(i==letter):
		    list.remove(i)

def checkout(skus):

        [x, y] = [(list(skus).count('A') // 3), (list(skus).count('A') % 3)]
        [i, j] = [(list(skus).count('B') // 2), (list(skus).count('B') % 2)]
        total = (x*130 + y*50) + (i*45 + y*30)
        try:
            remove_letters('A', list(skus))
        except:
            pass
        try:
            remove_letters('B', list(skus))
        except:
            pass
        map = {'C':20, 'D':15}
        total += sum([map[x] for x in list(skus)])
        return total




