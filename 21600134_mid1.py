print("한동 병원 온라인 예약 시스템")
res = []
name = []
sym = []
more = 'y'
line = "-------------------- 신규예약 --------------------"
line2 = "-------------------- 예약목록 --------------------"
while True:
    if more == 'y':
        print(line)
        while True:
            res_ = input("예약 날짜를 입력해 주세요: ")
            if res_.isdigit() != True or len(res_) != 4:
                print("잘못된 입력입니다.")
                continue
            elif res_ in res:
                print("이미 예약된 날짜입니다.")
                continue
            else:
                res.append(res_)
            break

    
        while True:
            name_ = input("환자의 이름을 입력해 주세요: ")
            if len(name_) < 2:
                print("2글자 이상 입력해 주세요.")
                continue
            else:
                name.append(name_)
            break
        sym_ = input("증상을 입력해 주세요: ")
        sym.append(sym_)
        more = input("예약을 추가로 더 하시겠습니까? (y)")
        if more != 'y':
            break
    
    
if more != 'y':
    print(line2)
    cnt = 1
    for i in range(0, len(res)):
        print("+++ 아이템", cnt, "+++")
        print("예약 날짜: " + res[i])
        print("환자 이름: " + name[i])
        print("증상: " + sym[i]) 
        cnt += 1
    