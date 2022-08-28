import sys
from collections import OrderedDict




def get_kth(n, m, k, a, p):
    dict_num = {}
    for i in a:
        if i not in dict_num:
            dict_num[i] = 1
        else:
            dict_num[i] += 1
            
    for i in range(len(p)):
        if p[i][1] not in dict_num:
            dict_num[p[i][1]] = p[i][0]
        else:
            dict_num[p[i][1]] += p[i][0]
            
    d_sort = OrderedDict(sorted(dict_num.items()))
    sum_narast = 0
    for i in d_sort.items():
        if k <= i[1]+sum_narast:
            print(i[0])
            break
        else:
            sum_narast += i[1]
    

def main():
    
    input_string1 = list(map(int, sys.stdin.readline().split()))
    n = input_string1[0]
    
    m = input_string1[1]
    k = input_string1[2]
    
    a = list(map(int, sys.stdin.readline().split()))

    p = [0] * m    
    for row in range(m):
        
        p[row] = list(map(int, sys.stdin.readline().split()))
    
    get_kth(n, m, k, a, p)
    



if __name__ == "__main__":
    main()
