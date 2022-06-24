

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    lst = ['A', 'B', 'C', 'D']
    dic = {}
    for i in skus:
        if i not in lst:
            return -1
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    val = 0
    for k, v in dic.items():
        if k == 'A':
            val += v//3 * 130 + v%3 * 50
        elif k == 'B':
            val += v//2 * 45 + v%2 * 30
        elif k == 'C':
            val += v*20
        else:
            val += v*15
    return val
    
        
