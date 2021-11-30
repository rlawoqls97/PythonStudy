# ====================================== #
# Study python because of Coding test
# Algorithm with python
# 코딩테스트를 파이썬으로 치루기 위한 공부
# ====================================== #


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

# def quick_sort(a):
#     n = len(a)
#     if n <= 1:
#         return a
#     piv = a[-1]
#     g1 = []
#     g2 = []
#     for i in range(0, n - 1):
#         if a[i] < piv:
#             g1.append(a[i])
#         else:
#             g2.append(a[i])
#     return quick_sort(g1) + [piv] + quick_sort(g2)

# l = [3, 7, 2, 5, 6, 1, 10, 19, 22, 35, 4]
# print(quick_sort(l))

# def quick_sort_sub(a, start, end):
#     if end - start <= 0:
#         return 
#     pivot = a[end]
#     i = start
#     for j in range(start, end):
#         if a[j] < pivot:
#             a[i], a[j] = a[j], a[i]
#             i += 1
#     a[i], a[end] = a[end], a[i]
    
#     quick_sort_sub(a, start, i - 1)
#     quick_sort_sub(a, i + 1, end)
# def quick_sort(a):
#     quick_sort_sub(a, 0, len(a) - 1)
# l = [3, 2, 7, 8, 10, 11, 21, 1, 2, 5, 4]
# quick_sort(l)
# print(l)

# def bubble_sort_failed(a):
#     n = len(a)
#     g = []
#     if n <= 1:
#         return a
#     for i in range(0, n - 1):
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
#             g.append(a[i])
#     return bubble_sort_failed(g)
# l = [1, 3, 54, 6, 2, 4, 7]
# print(bubble_sort_failed(l))

# def bubble_sort(a):
#     n = len(a)
#     while True:
#         changed = False
#         for i  in range(0, n - 1):
#             if a[i] > a[i + 1]:
#                 a[i], a[i + 1] = a[i + 1], a[i]
#                 changed = True
#         if changed == False:
#             return

# l = [2, 4, 5, 1, 3]
# bubble_sort(l)
# print(l)

# def binary_search(a, x):
#     start = 0
#     end = len(a) - 1
    
#     while start <= end:
#         mid = (start + end) // 2
#         if x == a[mid]:
#             return mid
#         elif x > a[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
            
#     return -1

# l = [1, 2, 4, 5, 7, 9, 11, 13, 14, 17, 19, 20]
# print(binary_search(l, 4))
# print(binary_search(l, 3))

# def binary_search_sub(a, x, start, end):
#     if start > end:
#         return -1
#     mid = (start + end) // 2
#     if x == a[mid]:
#         return mid
#     elif x > a[mid]:
#         return binary_search_sub(a, x, mid + 1, end)
#     elif x < a[mid]:
#         return binary_search_sub(a, x, start, mid - 1)

# def binary_search(a, x):
#     return binary_search_sub(a, x, 0, len(a) - 1)
    
# l = [1, 2, 3, 5, 7, 8, 11, 13, 15, 17, 19, 21, 22, 23, 24]
# print(binary_search(l, 3))

# def palindrome_with_stack_queue(s):
#     qu = []
#     st = []
#     for x in s:
#         if x.isalpha():
#             qu.append(x.lower())
#             st.append(x.lower())
            
#     while qu:
#         if qu.pop(0) != st.pop():
#             return False
#     return True

# print(palindrome_with_stack_queue("WOWOW"))

# def palindrome(s):
#     n = len(s)
#     i = 0
#     j = n - 1
#     while i < j:
#         if s[i].isalpha() == False:
#             i += 1
#         elif s[j].isalpha() == False:
#             j -= 1
#         elif s[i].lower() != s[j].lower():
#             return False
#         else:
#             i += 1
#             j -= 1
#     return True
# print(palindrome("132"))
# print(palindrome("Abcba"))
# print(palindrome("ajsdlfjasdnfl"))

# num_ = 0
# cnt = 1
# sum = 0
# while num_ <= 0 :
#     num_ = int(input("정수를 몇개 입력 할까요? "))
# while cnt <= num_:
#     num = float(input("숫자를 입력해주세요: "))
#     cnt += 1
#     sum += num
    
# print("입력한 숫자의 평균은 = ", sum / num_)

# name = ' '
# cnt = 1
# while name[0] != '김' and name[0] != '최' and name[0] != '이' and cnt <= 5:
#     name = input("이름을 입력해 주세요 ")
#     cnt += 1

# if cnt > 5:
#     print("이름은 5번까지 입력할 수 있습니다.")
# else:
#     print("성씨는 김, 이, 최 중에 있습니다.")

# #1
# for i in range(0, 11):
#     print("*" * i)

# #2
# for i in range(10, 0, -1):
#     print("*" * i)

# i = 0
# for i in range(1, 11):
#     print(' ' * (10 - i), '*' * (i * 2), ' ' * (10 - i))

# fruit = input("과일 이름을 영어로 입력해주세요: ")
# cnt = 0

# for char in fruit:
#     if char == 'a':
#         cnt += 1
    
# print(cnt, "개입니다.")

# dan = int(input("몇 단 까지 출력하고 싶은지 숫자로 입력해주세요: "))
# for i in range(2, dan + 1):
#     for j in range(1, 10):
#         print(i, "X", j, "=", i * j)

# def find_same_name(a):
#     name_dic = {}
#     for name in a:
#         if name in name_dic:
#             name_dic[name] += 1
#         else:
#             name_dic[name] = 1
            
#     result = set()
#     for name in name_dic:
#         if name_dic[name] >= 2:
#             result.add(name)
            
#     return result

# name = ["Tom", "J", "H", "H", "K", "P"]
# print(find_same_name(name))

# def find_name(a):
#     cnt = int(input("학생 번호를 입력해주세요: "))
#     if cnt in a:
#         print(a[cnt])
#     else:
#         print("???")
# name_ = {
#     39 : "Justin",
#     14 : "John",
#     67 : "Mike",
#     105 : "Summer"
# }
# find_name(name_)

# def print_all_friends(g, start):
#     qu = []
#     done = set()
#     qu.append(start)
#     done.add(start)
#     while qu:
#         p = qu.pop(0)
#         print(p)
#         for x in g[p]:
#             if x not in done:
#                 qu.append(x)
#                 done.add(x)
                
# fr_info = {
#     "Summer" : ["John", "Justin", "Mike"],
#     "John" : ["Summer", "Justin"],
#     "Justin" : ["John", "Summer", "Mike", "May"],
#     "Mike" : ["Summer", "Justin"],
#     "May" : ["Justin", "Kim"],
#     "Kim" : ["May"],
#     "Tom" : ["Jerry"],
#     "Jerry" : ["Tom"]
# }

# print_all_friends(fr_info, "Jerry")
# print()
# print_all_friends(fr_info, "Summer")

# def print_all_friends_friendship(g, start):
#     qu = []
#     done = set()
#     qu.append((start, 0))
#     done.add(start)
#     while qu:
#         (p, d) = qu.pop(0)
#         print(p, d)
#         for x in g[p]:
#             if x not in done:
#                 qu.append((x, d + 1))
#                 done.add(x)
                
# fr_info = {
#     "Summer" : ["John", "Justin", "Mike"],
#     "John" : ["Summer", "Justin"],
#     "Justin" : ["John", "Summer", "Mike", "May"],
#     "Mike" : ["Summer", "Justin"],
#     "May" : ["Justin", "Kim"],
#     "Kim" : ["May"],
#     "Tom" : ["Jerry"],
#     "Jerry" : ["Tom"]
# }

# print_all_friends_friendship(fr_info, "Jerry")
# print()
# print_all_friends_friendship(fr_info, "Summer")

# def find_graph_algo(g, start):
#     qu = []
#     done = set()
#     qu.append(start)
#     done.add(start)
#     while qu:
#         p = qu.pop(0)
#         print(p)
#         for x in g[p]:
#             if x not in done:
#                 qu.append(x)
#                 done.add(x)


# graph_info = {
#     "1" : ["2", "3"],
#     "2" : ["1", "4", "5"],
#     "3" : ["1"],
#     "4" : ["2"],
#     "5" : ["2"]
# }
# find_graph_algo(graph_info, "1")

##################################################BFS##################################################
# graph = dict()
 
# graph['A'] = ['B', 'C']
# graph['B'] = ['A', 'D']
# graph['C'] = ['A', 'G', 'H', 'I']
# graph['D'] = ['B', 'E', 'F']
# graph['E'] = ['D']
# graph['F'] = ['D']
# graph['G'] = ['C']
# graph['H'] = ['C']
# graph['I'] = ['C', 'J']
# graph['J'] = ['I']

# def bfs(graph, start_node):
#     need_visited, visited = [], []
#     need_visited.append(start_node)
    
    
#     while need_visited:
#         node = need_visited[0]
#         del need_visited[0]
        
#         if node not in visited:
#             visited.append(node)
#             need_visited.extend(graph[node])
            
#     return visited


# print(bfs(graph, 'A'))

##################################################DFS##################################################

# graph = dict()
 
# graph['A'] = ['B', 'C']
# graph['B'] = ['A', 'D']
# graph['C'] = ['A', 'G', 'H', 'I']
# graph['D'] = ['B', 'E', 'F']
# graph['E'] = ['D']
# graph['F'] = ['D']
# graph['G'] = ['C']
# graph['H'] = ['C']
# graph['I'] = ['C', 'J']
# graph['J'] = ['I']

# def dfs(graph, start_node):
     
#     ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
#     need_visited, visited = list(), list()
 
#     ## 시작 노드를 시정하기 
#     need_visited.append(start_node)
    
#     ## 만약 아직도 방문이 필요한 노드가 있다면,
#     while need_visited:
 
#         ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
#         node = need_visited.pop()
        
#         ## 만약 그 노드가 방문한 목록에 없다면
#         if node not in visited:
 
#             ## 방문한 목록에 추가하기 
#             visited.append(node)
 
#             ## 그 노드에 연결된 노드를 
#             need_visited.extend(graph[node])
            
#     return visited

# print(dfs(graph, 'A'))

# def dfs_recursive(graph, start, visited = []):
#     ## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
#     visited.append(start)
 
#     for node in graph[start]:
#         if node not in visited:
#             dfs_recursive(graph, node, visited)
#     return visited

# maze = {
#     'a' : ['e'],
#     'b' : ['c', 'f'],
#     'c' : ['b', 'd'],
#     'd' : ['c'],
#     'e' : ['a', 'i'],
#     'f' : ['b', 'g', 'i'],
#     'g' : ['f', 'h'],
#     'h' : ['g', 'l'],
#     'i' : ['e', 'm'],
#     'j' : ['f', 'k', 'n'],
#     'k' : ['j', 'o'],
#     'l' : ['h', 'p'],
#     'm' : ['i', 'n'],
#     'n' : ['m', 'j'],
#     'o' : ['k'],
#     'p' : ['i']
# }

# def solve_maze(g, start, end):
#     qu = []
#     done = set()
#     qu.append(start)
#     done.add(start)
#     while qu:
#         p = qu.pop(0)
#         v = p[-1]
#         if v == end:
#             return p
#         for x in g[v]:
#             if x not in done:
#                 qu.append(p + x)
#                 done.add(x)
#     return "?"

# print(solve_maze(maze, 'a', 'p'))

# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightpink")
# a = turtle.Turtle()
# a.color("grey")
# a.pensize(5)
# for i in range(20, 110, 20):
#     a.penup()
#     a.goto(i, i)
#     a.pendown()
#     for j in range(4):
#         a.forward(120)
#         a.left(90)
        
# import turtle

# def square(t, size, color):
#     t.color(color)
#     for i in range(4):
#         t.forward(size)
#         t.right(90)
        
# t1 = turtle.Turtle()
# t1.pensize(5)
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'darkgreen', 'hotpink', 'grey', 'black']
# i = 25
# for color in colors:
#     square(t1, i, color)
#     i+=25

# import turtle
# t=turtle.Turtle()
# def drawPoly(sideL, num, color):
#     t.color(color)
#     turn = 360/num
#     for i in range(num):
#         t.pendown()
#         t.forward(sideL)
#         t.right(turn)
# t.penup()
# t.setposition(-50, 0)
# drawPoly(50, 5, 'blue')
# t.penup()
# t.setposition(100, 0)
# drawPoly(50, 8, 'hotpink')

# import random

# def random_picker(lists, number):
#     for i in range(number):
#         print(random.choice(lists))
        
# num_list = [3, 1, 7, 11, 25, 5, 4, 9]

# random_picker(num_list, 3)

# import random

# def gen_random(a, b):

#     r = random.randrange(a,b)
#     c = chr(65 + r)
#     print(r, c)

# for i in range(10):
#     gen_random(i + 1, i + 10)

# from datetime import date

# def cal_birthday(month, day):
#     today = date.today()
#     birthday = date(today.year, month, day)
#     due = birthday - today
#     if due.days < 0 :
#         next_birthday = date(today.year + 1, birthday.month, birthday.day)
#         due = next_birthday - today
#     print("생일까지 남은 날짜는: ", due.days)

# import math
# import cmath
# def deter(a, b, c):
#     return math.pow(b, 2) - 4*a*c

# def roots_formula(a, b, c):
#     if deter(a,b,c) >= 0:
#         root01 = (-b + math.sqrt(deter(a,b,c)))/ (2*a)
#         root02 = (-b - math.sqrt(deter(a,b,c)))/ (2*a)
#     else:
#         root01_real = -b/(2*a)
#         root01_imag = (math.sqrt(math.fabs(deter(a,b,c))))/ (2*a)
#         root02_real = -b/(2*a)
#         root02_imag = (math.sqrt(math.fabs(deter(a,b,c))))/ (2*a)
#         root01 = root01_real + root01_imag * 1j
#         root02 = root02_real - root02_imag * 1j
#     return [root01, root02]

# def fibo(n) :
#     if n == 1 or n == 2 :
#         return 1
#     else :
#         return fibo(n-1) + fibo(n-2)
# for i in range(1,15) :
#     print(fibo(i))

# def mult3(n) :
#     mul=0
#     if n >=1 :
#         for I in range(n):
#             mul=mul+3
#     return mul
# for i in range(1,10) :
#     print(mult3(i))

# import random
# namelist= []
# oxlist= []
# count = int(input("인원을 입력하세요: "))
# for i in range (count) :
#     name = input("이름을 입력하세요: ")
#     namelist.append(name)
# for i in range (count) :
#     oxlist.append(random.choice(['o', 'x']))
# tname = tuple(namelist)
# print(tname)
# t = list(zip(tname, oxlist))
# print(t)

# s = 'abcdefghijklmnopqrstuvwxyz'
# Num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# Tu_SNum = list(zip(s, Num))
# print(Tu_SNum)

# Subjects = {'김경미':['수학','과학'],'최영희':['영어', '수학'], '강동원':'영어', '정필수':['사회', '역사'], '박희수':'국어', '이승철':['수학', '과학']}
# lec = input('담당교사명을 입력하시오: ')
# print(Subjects[lec])

# def find_teacher(sub):
#     Subjects = {'김경미':['수학','과학'],'최영희':['영어', '수학'], '강동원':'영어', '정필수':['사회', '역사'], '박희수':'국어', '이승철':['수학', '과학']}
#     teacher = []
#     for key in Subjects.keys():
#         if sub in Subjects[key]:
#             teacher.append(key)
#     return teacher
# sub = input('과목을 입력하시오: ')
# print(find_teacher(sub))

# inf = open('number.txt')
# s = inf.readlines()
# total = 0
# mean = 0
# for i in range(len(s)):
#     total = total + int(s[i])
# mean = total / len(s)
# print('Number list = ', s, '\nTotal = ', total, '\nMean = ',
# round(mean,2))

# inf = open('poem_sp.txt', 'r')
# sm = inf.readlines()
# for i in range(len(sm)) :
#     s=sm[i].strip(" ")
#     slist = s.split()
#     print(slist)
# inf.close()

# inf = open('poem.txt', 'r')
# NumWord = []
# for i in range(9):
#     fline = inf.readline()
#     flist = fline.split()
#     NumWord.append(len(flist))
# print(NumWord)
# inf.close()

# try:
#     f = open('poem.txt', 'r')
#     outf = open('numpoem.txt', 'w')
# except IOError as err:
#     print("unable to handle files")
# Numword=[]
# count=len(f.readlines())
# f.close()
# f = open('poem.txt', 'r')
# for i in range(count) :
#     fline=f.readline()
#     flist=fline.split()
#     outf.write(str(len(flist))+ "\n")
# f.close()
# outf.close()

# import os
# import shutil
# shutil.copy('numpoem.txt', 'nump.txt')
# os.remove('numpoem.txt')
# try:
#     inf = open('nump.txt', 'r')
#     s = inf.readlines()
#     sum = 0
#     for i in range(len(s)) :
#         sum = sum + int(s[i])
#     print("평균 = ", sum/len(s))
# except IOError as err:
#     print("I/O error: {0}".format(err))
# inf.close()

# from tkinter import *
# from tkinter import Tk, Canvas
# from PIL import ImageTk, Image
# root =Tk()
# canvas = Canvas(root, width=400, height=300)
# canvas.pack()
# def oneclick(event) :
#     im = Image.open('dog.jpeg')
#     canvas.image = ImageTk.PhotoImage(im)
#     canvas.create_image(0, 0, image=canvas.image, anchor='nw')
# def doubleclick(event) :
#     im = Image.open('cat.jpeg')
#     canvas.image = ImageTk.PhotoImage(im)
#     canvas.create_image(0, 0, image=canvas.image, anchor='nw')
# widget = Button(None, text='Mouse Clicks')
# widget.pack()
# widget.bind('<Button-1>', oneclick)
# widget.bind('<Double-1>', doubleclick)
# root.mainloop()

from tkinter import *
from tkinter.colorchooser import *
def NewFile() :
    print("New File!")
def OpenFile() :
    print("Open File!")
def About() :
    print("This is a simple example of a menu")
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
canvas = Canvas(root, width=500, height=500)
color = "red"
result = '#476042'
def callback() :
    global result
    result = askcolor(title = "Colour Chooser")
    result = result[1]
button = Button(root, text='Choose Color', fg="darkgreen", command=callback)
button.pack(side=LEFT, padx=10)
lastx, lasty = 0, 0
def xy(event) :
    global lastx, lasty
    lastx, lasty = event.x, event.y
def addLine(event) :
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=result)
    lastx, lasty = event.x, event.y
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas.pack()
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
root.mainloop()
