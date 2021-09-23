# Study python because of Coding test
# Algorithm with python
# 코딩테스트를 파이썬으로 치루기 위한 공부



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
#     for i in range(0, n - 1):
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
#         for j in range(i + 1, n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]
                
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

# def name_age_belong(a, b, c):
#     print("당신의 이름은", a)
#     print(b, "에 소속되어 있으시군요")
#     print("당신의 나이는", 2017 - c, "세, 맞죠?")
    
    
# name = input("당신의 이름을 입력하세요 ")
# belong = input("당신의 소속 기관을 입력하세요 ")
# birthday = int(input("당신이 출생년도를 입력하세요 "))
# name_age_belong(name, belong, birthday)

# def sel_sort_inverse(a):
#     n = len(a)
#     for i in range(0, n - 1):
#         max_idx = i
#         for j in range(i + 1, n):
#             if a[j] > a[max_idx]:
#                 max_idx = j
#         a[i], a[max_idx] = a[max_idx], a[i]
                
# l = [3, 5, 6, 1, 2, 7, 12, 11]
# sel_sort_inverse(l)
# print(l)

# def find_ins_idx(r, v):
#     for i in range(0, len(r)):
#         if v < r[i]:
#             return i
#     return len(r)

# def ins_sort(a):
#     result =[]
#     while a:
#         value = a.pop(0)
#         ins_idx = find_ins_idx(result, value)
#         result.insert(ins_idx, value)
#         print(a, result)
#     return result

# d = [2, 4, 5, 1, 3]
# print(ins_sort(d))

# def ins_sort(a):
#     l = len(a)
#     for i in range(1, l):
#         key = a[i]
#         j = i - 1
#         while j >= 0 and a[j] > key:
#             a[j + 1] = a[j]
#             j -= 1
#         a[j + 1] = key

# d = [2, 4, 5, 1, 3, 6, 8, 7]
# ins_sort(d)
# print(d)

# def ins_sort(a):
#     l = len(a)
#     for end in range(1, l):
#         i = end
#         while i > 0 and a[i - 1] > a[i]:
#             a[i - 1], a[i] = a[i], a[i - 1]
#             i -= 1
            
# d = [2, 4, 5, 1, 3]
# ins_sort(d)
# print(d)

# def ins_sort_rev(a):
#     l = len(a)
#     for end in range(1, l):
#         i = end
#         while i > 0 and a[i - 1] < a[i]:
#             a[i - 1], a[i] = a[i], a[i - 1]
#             i -= 1
            
# d = [2, 4, 5, 1, 3]
# ins_sort_rev(d)
# print(d)

# def merge_sort(a):
#     n = len(a)
#     if n <= 1:
#         return a
#     mid = n // 2
#     g1 = merge_sort(a[:mid])
#     g2 = merge_sort(a[mid:])
#     result = []
#     while g1 and g2:
#         if g1[0] < g2[0]:
#             result.append(g1.pop(0))
#         else:
#             result.append(g2.pop(0))
            
#     while g1:
#         result.append(g1.pop(0))
#     while g2:
#         result.append(g2.pop(0))
    
#     return result
# d = [1, 3, 5, 7, 6, 2, 4, 8, 9, 11, 10, 12]
# print(merge_sort(d))

# def merge_sort(a):
#     n = len(a)
#     if n <= 1:
#         return
#     mid = n // 2
#     g1 = a[:mid]
#     g2 = a[mid:]
#     merge_sort(g1)
#     merge_sort(g2)
#     i1 = 0
#     i2 = 0
#     ia = 0
#     while i1 < len(g1) and i2 < len(g2):
#         if g1[i1] < g2[i2]:
#             a[ia] = g1[i1]
#             i1 += 1
#             ia += 1
#         else:
#             a[ia] = g2[i2]
#             i2 += 1
#             ia += 1
        
#     while i1 < len(g1):
#         a[ia] = g1[i1]
#         i1 += 1
#         ia += 1
#     while i2 < len(g2):
#         a[ia] = g2[i2]
#         i2 += 1
#         ia += 1

# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# merge_sort(d)
# print(d)

# def merge_sort_re(a):
#     n = len(a)
#     if n <= 1:
#         return
#     mid = n // 2
#     g1 = a[:mid]
#     g2 = a[mid:]
#     merge_sort_re(g1)
#     merge_sort_re(g2)
#     i1 = 0
#     i2 = 0
#     ia = 0
#     while i1 < len(g1) and i2 < len(g2):
#         if g1[i1] > g2[i2]:
#             a[ia] = g1[i1]
#             i1 += 1
#             ia += 1
#         else:
#             a[ia] = g2[i2]
#             i2 += 1
#             ia += 1
        
#     while i1 < len(g1):
#         a[ia] = g1[i1]
#         i1 += 1
#         ia += 1
#     while i2 < len(g2):
#         a[ia] = g2[i2]
#         i2 += 1
#         ia += 1

# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# merge_sort_re(d)
# print(d)

# kor = float(input("국어성적 입력: "))
# eng = float(input("영어성적 입력: "))
# math = float(input("수학성적 입력: "))
# avg = (kor + eng + math) / 3

# if avg > 60 and kor >= 50 and eng >= 50 and math >= 50:
#     print("성적평균은", avg, "이미, 과락 과목도 없기 때문에 합격입니다")
# else:
#     if avg >= 60:
#         print("성적평균은", avg, "이지만 50점 미만 과목이 있어서 불합격 입니다.")
#     else:
#         print("성적평균은", avg, "이며 불합격입니다.")

# height = float(input("키를 m 단위로 입력해 주세요: "))
# weight = float(input("몸무게를 kg단위로 입력해 주세요: "))
# bmi = weight / (height * height)

# if bmi < 18.5:
#     print("BMI지수는", bmi, "이며 저체중 상태입니다.")
# elif bmi < 23:
#     print("BMI지수는", bmi, "이며 정상 상태입니다.")
# elif bmi < 25:
#     print("BMI지수는", bmi, "이며 과체중 상태입니다.")
# elif bmi < 30:
#     print("BMI지수는", bmi, "이며 비만1 상태입니다.")
# elif bmi < 40:
#     print("BMI지수는", bmi, "이며 비만2 상태입니다.")
# else:
#     print("BMI지수는", bmi, "이며 심각한 비만3 상태입니다.")

# kor = float(input("국어성적 입력: "))
# eng = float(input("영어성적 입력: "))
# math = float(input("수학성적 입력: "))
# avg = (kor + eng + math) / 3

# if kor < 50 or eng < 50 or math < 50:
#     print("과락")
# elif avg >= 60:
#     print("합격")
# else:
#     print("불합격")

# mon = int(input("월을 입력하세요: "))
# if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
#     print("31일 까지")
# elif mon == 2:
#     print("28일 또는 29일 까지")
# elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
#     print("30일 까지")
# else:
#     print("오류")