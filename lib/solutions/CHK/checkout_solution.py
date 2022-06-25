

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    dic = {}
    for i in skus:
        if not i.isupper():
            return -1
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    val = 0
    b = 0
    m = 0
    q = 0
    pack = [0, 0, 0, 0, 0]
    price = [21, 20, 20, 20, 17]
    for k, v in sorted(dic.items(), reverse=True):
        if k == 'A':
            val += v//5 * 200
            v = v%5
            val += v//3 * 130 + v%3 * 50
        elif k== 'V':
            val += v//3* 130
            v = v%3
            val += v//2* 90+ v%2* 50
        elif k == 'H':
            val += v//10 * 80
            v = v%10
            val += v//5 * 45 + v%5 * 10
        elif k == 'E':
            val += v*40
            b = v//2
        elif k == 'I':
            val += v*35
        elif k == 'J':
            val += v*60
        elif k == 'C' or  k == 'G' or  k == 'W':
           val += v*20
        elif k == 'D':
            val += v*15
        elif k == 'N':
            val += v*40
            m = v//3
        elif k == 'L':
            val += v*90
        elif k == 'R':
            val += v*50
            q = v//3
        elif k == 'J' or  k == 'Z':
            val += v*50
        elif k == 'Y':
            val += v*10
        elif k == 'X':
            val += v*90
        elif k == 'O':
            val += v*10
        elif k == 'B':
            val += (v-b)//2*45 + (v-b)%2*30
        elif k == 'Q':
            val +=(v-q)//3*80 +(v-q)%3*30
        elif k == 'M':
             val += (v-m)*15
        elif k == 'F':
            val += v//3*20 + v%3 * 10
        elif k == 'K':
            val += v//2*150 + v%2*80
        elif k == 'P':
            val += v//5*200 +v%5*50
        elif k == 'U':
            val += v//4*120+v%4*40
        elif k == 'Z':
            pack[0] = v
        elif k == 'Y':
            pack[1] = v
        elif k == 'X':
            pack[4] = v
        elif k == 'S':
            pack[3] = v
        elif k == 'T':
            pack[2] = v
        pack_sum = sum(pack)
        val += pack_sum//3*45
        pack_sum = pack_sum//3*3
        for i in range(len(pack)):
            if pack[i] < pack_sum:
                pack[i] = 0
                pack_sum -= pack[i]
            else:
                pack[i] -= pack_sum
                pack_sum = 0
                break
                    
        import numpy as np
        val += int(sum(np.array(pack)*np.array(price)))
    return val
    
        



