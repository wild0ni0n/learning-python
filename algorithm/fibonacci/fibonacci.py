import sys

fibonacci_list = {}

def culc_fibonacci_memo(n):
    global fibonacci_list
    if n == 1:
        return 1
    elif n == 0:
        return 0
    if not n in fibonacci_list:
        fibonacci_list[n] = culc_fibonacci_memo(n-1) + culc_fibonacci_memo(n-2)
    return fibonacci_list[n]

if __name__ == "__main__":
    for n in range(10):
        fibonacci_n = culc_fibonacci_memo(n)
        print(fibonacci_n, end='')
        if not n == 9:
            print('.', end='')
    print('\n')
    print(fibonacci_list)