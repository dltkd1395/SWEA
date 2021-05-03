# SWEA[테네스의 특별한 소수]

n= 10**6
def set_prime():
  for i in range(n+1):
    if prime[i] == 1:
        for j in range(i*2, n+1, i):
          prime[j] = 0

prime = [1]*(n+ 1)
prime[0], prime[1] = 0, 0
set_prime()

for t in range(int(input())):
  d,a,b = map(int, input().split())
  answer = []
  for i in range(a, b+1):
    if str(d) in str(i) and prime[i]:
      answer.append(i)

  print('#%d %d' %(t+1,len(answer)))

    
