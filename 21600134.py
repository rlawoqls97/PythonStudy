answer = 0
arr = [5, 2, -16, 4]
b = []
s = []
b_n = 0
s_n = 0
cnt = 0
for i in range(0, len(arr)):
    if arr[i] > 0:
        b_n = b_n + arr[i]
        b.append(b_n)
        s.append(s_n)
    elif arr[i] < 0:
        s_n = s_n + abs(arr[i])
        s.append(s_n)
        b.append(b_n)
print(b, s)
for i in range(0, len(arr)):
    if b[i] > s[i]:
        cnt = cnt + 1

print(cnt)
        
    
