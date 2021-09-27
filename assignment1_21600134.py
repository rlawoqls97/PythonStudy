# 1.
sleep_hour = input("어제 몇시간 잠을 잤는지 실수형으로 입력해주세요. 7시간 30분일 경우 7.5: ")
if float(sleep_hour) < 0:
    print("자는 시간은 음수일 수 없습니다.")
    quit()
# 2.
print("당신이 입력한 잔 시간은 ", sleep_hour, ", ", "Bool값으로 변환하면 " ,bool(sleep_hour), sep='')
# 3.
print("당신이 입력한 잔 시간은 ", float(sleep_hour), ", ", "Bool값으로 변환하면 " ,bool(float(sleep_hour)), sep='')
# 6.
if float(sleep_hour) == 0:
    why_nsleep = input("잠을 못잔 이유가 무엇인가요? 숙제, 시험, 스트레스, 불면증, 그외의 이유를 입력해주세요: ")
    if why_nsleep == '숙제':
        print("마음이 편안해지는 곡인 쇼팽의 녹턴을 추천드립니다.")
    elif why_nsleep == '시험':
        print("마음이 편안해지는 곡인 쇼팽의 녹턴을 추천드립니다.")
    elif why_nsleep == '스트레스':
        print("마음이 편안해지는 곡인 쇼팽의 녹턴을 추천드립니다.")
    elif why_nsleep == '불면증':
        print("잠이 잘 오는 곡인 태연의 사계를 추천드립니다.")
    else:
        print("사랑에 관한 곡인 sg워너비의 라라라를 추천드립니다.")
    quit()
# 4.
m_walk = input("오늘 당신이 걸은 걸음의 수를 정수로 입력해주세요: ")
if int(m_walk) < 0:
    print("걸음 수는 음수일 수 없습니다.")
    quit()
avg = int(m_walk) // int(24.0 - float(sleep_hour))
# 5.
mes = input("파이팅 문구를 최소 6글자 이상 입력해주세요: ")
l = len(mes)
mes_l = list(mes)
list = []
if l < 6:
    print("6글자 이상 입력해주세요")
    quit()
# 7. 
if 0 < float(sleep_hour) <= 6 and 0 <= int(m_walk) <= 8000:
    for i in range(1, l - 1):
        mes_l[i] = '+'
    mes_l_to_str = ''.join(mes_l)
    print("바뀐 글자를 포함한 메세지는", mes_l_to_str, "입니다.")
# 8.
if float(sleep_hour) <= 6 and int(m_walk) > 8000:
    print((int(float(sleep_hour)) * 2) * "*", "오늘은", float(sleep_hour) * 2, "시간만큼 자야 합니다.", (int(float(sleep_hour)) * 2) * "*")
# 9.
if float(sleep_hour) > 6 and float(sleep_hour) < 9 :
    print("당신의 평균 걸음 수는", avg, "입니다. 당신은 정말 건강하게 지내고 있습니다.")
# 10.
if 9 <= float(sleep_hour) < 24:
    fav_num = input("2 ~ 9사이에서 가장 좋아하는 숫자를 입력하세요: ")
    if int(fav_num) < 2 or int(fav_num) > 9:
        print("2에서 9 사이의 숫자를 입력해 주세요")
        quit()
# 11.
if int(fav_num) <= l:
    if float(sleep_hour) >= 9 and int(m_walk) >= 8000 and avg >= 1000 and (int(fav_num) % 2 == 0 or int(fav_num) % 3 ==0) and int(fav_num )!= 6:
        for i in range(0, int(fav_num)):
            list.append(mes_l[i])
            mes_l_to_str = ''.join(list)
        print("좋아하는 숫자까지의 파이팅 문구는", mes_l_to_str, "입니다")
    elif int(m_walk) >= 8000 and avg >= 1000 and (int(fav_num) % 4 == 0 or int(fav_num) % 5 == 0 or int(fav_num) % 7 == 0):
        print("파이팅문구를 좋아하는 숫자 만큼 출력하면", mes * int(fav_num), "입니다.")    
    if float(sleep_hour) >= 9 and int(m_walk) >= 8000 and avg >= 1000 and int(fav_num) % 6 == 0 :
        print("2의 배수이며 동시의 3의 배수인 6이 입력되었습니다. 출력은 파이팅 문구인", mes, "을(를) 출력합니다.")
else:
    print("좋아하는 숫자까지의 파이팅 문구는", mes, "입니다.")
    quit()
# 12.
if float(sleep_hour) >= 9 and int(m_walk) >= 8000 and avg < 1000:
    print("오늘 깨어 있었던 시간은", float(24 - float(sleep_hour)), "평균 걸음수는", avg, "입니다.")
# 13.
if float(sleep_hour) >= 9 and int(m_walk) < 8000:
    print("파이팅 문구 길이만큼 좋아하는 숫자를 출력하면", fav_num * l, "입니다.")