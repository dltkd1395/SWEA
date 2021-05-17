# SWEA[회문2]
def check(s):

  for i in range(len(s)//2):
    if s[i]!=s[-1-i]:
      return False
  return True


for t in range(10):
  n=int(input())

  data=[list(input()) for _ in range(100)]
  data2=list(zip(*data))
  data_lst=[]
  max_val=1
  
  for length in range(100,1,-1):
    if max_val>=length:
      break
    
    for idx in range(100-length+1):
      if max_val==length:
        break

      for lst,lst2 in zip(data,data2):
        if check(lst[idx:idx+length]) or check(lst2[idx:idx+length]):
          max_val=length
          break
  
  print('#%d %d' %(t+1,max_val))
      
  



