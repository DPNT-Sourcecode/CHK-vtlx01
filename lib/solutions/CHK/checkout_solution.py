

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    lst2 = ['A', 'B', 'C', 'D', 'E']
    dic = {}
    for i in skus:
        if i not in lst2:
            return -1
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    val = 0
    b = 0
    for k, v in dic.items():
        if k == 'A':
            val += v//5 * 200
            v = v%5
            val += v//3 * 130 + v%3 * 50
        elif k == 'E':
            val += v*40
            b = v//2
        elif k == 'C':
            val += v*20
        elif k == 'D':
            val += v*15
        else:
            if v-b>2:
                val += (v-b)//2*45 + (v-b)%2*30
            else:
                val += (v-b)*30
    return val
    
        

