print("======================================")
print("도형그리기에 오신것을 환영합니다.")
print("======================================")

num_list = []
len_list = []
width_list = []
more = 'y'
while True:
    if more == 'y':
        while True:
            try:
                num_side = input("다각형 변의 개수를 입력해 주세요: ")
                num_side = float(num_side)
                assert(num_side >= 3), print("입력된 값은 3보다 커야 합니다.")
                print("입력한 다각형 변의 개수는", int(num_side),"개 입니다.")
                num_list.append(num_side)
                break
            except ValueError as err:
                print("ValueError: {0}".format(err))
                print("숫자를 입력해 주세요.")
        
        limit = (800 / (int(num_side) / 2))

        while True:
            try:
                len_side = input("다각형 한 변의 길이를 입력해 주세요: ")
                len_side = float(len_side)
                assert(10 <= len_side <= limit), print("입력한 값은 10보다 커야하며 제한 크기보다 작아야 합니다.")
                print("입력한 다각형 변의 길이는", float(len_side),"입니다.")
                len_list.append(len_side)
                break
            except ValueError as err:
                print("ValueError: {0}".format(err))
                print("숫자를 입력해 주세요.")

        while True:
            try:
                border_side = input("다각형 테두리 두께를 입력해 주세요: ")
                border_side = float(border_side)
                assert(0 <border_side), print("입력한 값은 0보다 커야 합니다.")
                print("입력한 다각형 두께의 길이는", float(border_side), "입니다.")
                width_list.append(border_side)
                break
            except ValueError as err:
                print("ValueError: {0}".format(err))
                print("숫자를 입력해 주세요.")

        more = input("다각형을 추가로 더 그리시겠습니까: ")
        if more != 'y':
            break


import turtle
import random
t = turtle.Turtle()
hw3 = turtle.Screen()
hw3.title('hw3')
hw3.setup(800, 800)
colors = ["yellow", "red", "violet", "blue", "skyblue", "lightgreen", "white", "green", "brown", "magenta"]
hw3.bgcolor(random.choice(colors))


def drawPolygon(sideLength, numSides, width):
    color = random.choice(colors)
    while color == hw3.bgcolor():
        color = random.choice(colors)
    t.color(color)    
    turnAngle= 360 / numSides
    for i in range(int(numSides)):
        t.pensize(width)
        t.pendown()
        t.forward(sideLength)
        t.right(turnAngle)
        
for i in range(0, len(len_list)):
    t.speed(0)
    t.penup()
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    t.setposition(x, y)
    t.write(str(i) + ", " + str(x) + ", " + str(y))
    drawPolygon(len_list[i], num_list[i], width_list[i])
    t.penup()
    t.setposition(0, 0)       

