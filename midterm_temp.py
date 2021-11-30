print('본문을 입력하면 검색 기능을 제공합니다.\n언제든지 "도움말" 이라고 입력하면 도움말을 볼 수 있습니다.\n')
searchContents = input('검색 대상 본문을 입력하시오: ')
searchContentsList = searchContents.split(".")
endList = ['바이', '끝', '종료']
while True:
    searchWord = input("본문에서 검색하고 싶은 단어를 입력하시오: ")
    if searchWord == ' ' or searchWord.isspace():
        print("잘못된 입력입니다.")
    elif searchWord == '본문보기':
        for verse in searchContentsList:
            print(verse.strip())
    elif searchWord.isdecimal():
        searchWord = int(searchWord)
        if 0 < searchWord <= len(searchContentsList):
            print(searchContentsList[searchWord - 1])
        else:
            print('잘못된 번호 입니다.')
    elif searchWord in endList:
        print("서비스를 이용해 주셔서 감사합니다. \n프로그램을 종료합니다.")
        break
    elif searchWord == '도움말':
        print('검색하고 싶은 단어를 입력하면 그 단어가 포함된 모든 문장이 검색됩니다.')
        print('단어를 입력하지 않거나 공백을 입력하면 검색이 안됩니다.')
        print('"본문보기"를 입력하면 전체 본문을 볼 수 있습니다.')
        print('숫자를 입력하면 해당 위치의 문장을 볼 수 있습니다.')
        print('"바이", "끝", "종료" 셋 중 하나를 입력하면 서비스가 종료됩니다.')
    else:
        searchList = []
        for verse in searchContentsList:
            if verse.find(searchWord) >= 0:
                searchList.append(verse)
        if searchList == []:
            print('결과 없음')
        else:
            for verse in searchList:
                print(verse.strip())
                
                
                
# #####################################2019기출
# # Q1 
# def drawCard(dear, congratulations, yours):
#   # Q1-a 
#   print('\t'+dear)
#   # Q1-b 
#   print()
#   # Q1-c 
#   mlines = len(congratulations)/31
#   if mlines != int(mlines):
#     mlines = mlines+1
#   mlines=int(mlines)
#   for i in range(mlines):
#     print(congratulations[i*31:(i+1)*31])
#   # Q1-d 
#   print()
#   # Q1-e 
#   print(' '*(31-len('Sincerely yours'))+'Sincerely yours')
#   print(' '*(31-len(yours))+yours)

# name = ''
# # Q2 
# while name == "" or name.isspace(): 
#   name = input('Enter the name of the birthday person: ')

# dearname = ''
# # Q3 
# if len(name) < 5:
#   for c in name:
#     dearname += c+"-"
#   dearname+='!'
# else:
#   dearname='Dear '+name

# # Q4 
# messagelist = ['Happy birthday!', 'Count your life by smiles, not tears. Count your age by friends, not years. Happy birthday!', 'Your birthday is the first day of another 365-day journey. Be the shining thread in the beautiful tapestry of the world to make this year the best ever. Enjoy the ride.']

# message = ""
# # Q5
# if len(name) < 5:
#   message = messagelist[0]
# elif len(name) < 10:
#   message = messagelist[1]
# else:
#   message = messagelist[2]

# sender=''
# # Q6 
# while sender=='' or sender.isspace() or len(sender) >31:
#   # Q2 
#   sender = input("Enter the sender's name: ")

# # Q7 
# print()
# # Q2 
# drawCard(dearname, message, sender)
