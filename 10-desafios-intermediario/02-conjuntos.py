T = int(input())

for i in range(T):
    T -= 1
    N, K = input().split()
    N = int(N)
    K = int(K)
    valor_total = int(int(N % K) + int(N / K))
   
    print(valor_total)
