# SWEA[스도쿠 검증]

for t in range(int(input())):
    my_map = [list(map(int, input().split())) for _ in range(9)]
    nums = set((1, 2, 3, 4, 5, 6, 7, 8, 9))

    result = 1
    
    for r in range(9):
        if set(my_map[r]) != nums:
            result = 0
            break
    else:  
        for c in range(9):  
            temp = set()
            for r in range(9):
                temp.add(my_map[r][c])
            if temp != nums:
                result = 0
                break
        else:  
            for r in range(0, 9, 3):
                if not result:
                    break
                else:
                    for c in range(0, 9, 3):
                        temp = set()
                        for dr in range(3):
                            for dc in range(3):
                                temp.add(my_map[r + dr][c + dc])
                        if temp != nums:
                            result = 0
                            break

    print('#%d %d' %(t+1, result))
