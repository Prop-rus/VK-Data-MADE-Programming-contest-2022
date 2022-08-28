import sys
import math


def find_best(a):
    
    def nearest(lst, target):
        return min(lst, key=lambda x: abs(x-target))
    
    n = max(a)
    if n % 2 != 0:
        k = nearest(a, n//2+1)
    else:
        k = nearest(a, n//2)
    print(n, k)
    
    
def main():
    
    m = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    
    find_best(a)


if __name__ == "__main__":
    main()