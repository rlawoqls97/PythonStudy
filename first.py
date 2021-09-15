import math

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)

# print(gcd(81, 30))

# def fibo(k):
#     if k <= 1:
#         return k
#     return fibo(k - 2) + fibo(k - 1)

# print(fibo(7))

# def hanoi(n, from_, to_, temp_):
#     if n == 1:
#         print(from_, "->", to_)
#         return
#     hanoi(n - 1, from_, temp_, to_)
#     print(from_, "->", to_)
#     hanoi(n - 1, temp_, to_, from_)
    
# print("n = 1")
# hanoi(1, 1, 3, 2)
# print("n = 2")
# hanoi(2, 1, 3, 2)

# def search(a, x):
#     n = len(a)
#     for i in range(0, n):
#         if x == a[i]:
#             return i
#     return -1

# list = [3, 100, 27, 9, 7, 6, 5]
# print(search(list, 7))

# def searchMany(a, x):
#     n = len(a)
#     b = []
#     for i in range(0, n):
#         if x == a[i]:
#             b.append(i)
#     return b
            
# list = [1, 3, 5, 7, 9, 11, 3]
# print(searchMany(list, 2))

# def fin_min(a):
#     n = len(a)
#     min_idx = 0;
#     for i in range(1, n):
#         if a[i] < a[min_idx]:
#             min_idx = i
#     return min_idx

# def sel_sort(a):
#     result =[]
#     while(a):
#         min_idx = fin_min(a)
#         value = a.pop(min_idx)
#         result.append(value)
#     return result

# d = [3, 2, 5, 1, 4, 6, 8, 7, 9, 11, 10]
# print(sel_sort(d))

# def sel_sort(a):
#     n = len(a)
#     for i in range(0, n - 1):
#         min_idx = i
#         for j in range(i, n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#                 a[i], a[min_idx] = a[min_idx], a[i]
                
# l = [3, 5, 6, 1, 2, 7, 12, 11]
# sel_sort(l)
# print(l)

# def avg(a, b, c):
#     avg_p = (a + b + c) / 3
#     return avg_p

# kor = input("당신의 국어 성적은? ")
# kor = float(kor)
# eng = input("당신의 영어 성적은? ")
# eng = float(eng)
# math = input("당신의 수학 성적은? ")
# math = float(math)
# avg_p = avg(kor, eng, math)
# print("3개의 성적의 평균은", avg_p, "입니다.")

# def name_3(a):
#     print(name[0] * 5)
#     print(name[1] * 5)
#     print(name[2] * 5)
#     return 
# name = input("이름 3 글자를 입력하세요 ")
# print(name_3(name))

def name_age_belong(a, b, c):
    print("당신의 이름은", a)
    print(b, "에 소속되어 있으시군요")
    print("당신의 나이는", 2017 - c, "세, 맞죠?")
    
    
name = input("당신의 이름을 입력하세요 ")
belong = input("당신의 소속 기관을 입력하세요 ")
birthday = int(input("당신이 출생년도를 입력하세요 "))
name_age_belong(name, belong, birthday)