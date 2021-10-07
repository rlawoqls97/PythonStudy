#1
m_list1 = ["Star wars1", "1999", "SF", "English", "Jedi Knights Qui-Gon Jinn and Obi-Wan Kenobi set out to stop the Trade Federation from invading Naboo. While travelling, they come across a gifted boy, Anakin, and learn that the Sith have returned.", 0, False]
m_list2 = ["Star wars2", "2002", "SF", "English", "While pursuing an assassin, Obi Wan uncovers a sinister plot to destroy the Republic. With the fate of the galaxy hanging in the balance, the Jedi must defend the galaxy against the evil Sith.", 0, False]
m_list3 = ["Star wars3", "2005", "SF", "English", "Anakin joins forces with Obi-Wan and sets Palpatine free from the evil clutches of Count Doku. However, he falls prey to Palpatine and the Jedis' mind games and gives into temptation.", 0, False]
m_list4 = ["Star wars4", "1978", "SF", "English", "After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.", 0, False]
m_list5 = ["Star wars5", "1980", "SF", "English", "Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.", 0, False]
m_list6 = ["Star wars6", "1987", "SF", "English", "Luke Skywalker attempts to bring his father back to the light side of the Force. At the same time, the rebels hatch a plan to destroy the second Death Star.", 0, False]
m_list7 = ["Inception", "2010", "SF", "English", "Cobb steals information from his targets by entering their dreams. Saito offers to wipe clean Cobb's criminal history as payment for performing an inception on his sick competitor's son.", 0, False]
m_list8 = ["Interstellar", "2014", "SF", "English", "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.", 0, False]
m_list9 = ["Tenet", "2020", "SF", "English", "When a few objects that can be manipulated and used as weapons in the future fall into the wrong hands, a CIA operative, known as the Protagonist, must save the world.", 0, False]
#2
m_list_all = [m_list1, m_list2, m_list3, m_list4, m_list5, m_list6, m_list7, m_list8, m_list9]
#3
m_tag = ["Title", "Date", "Genre", "Language", "Story", "Likes"]
#4
ascrip = "****************************************"
#13
all = 1
while True:
    print(ascrip)
    #5
    cnt = 0
    for i in m_list_all:
        if all == 1:
            cnt += 1
            print(cnt, i[0])
        #14
        elif all == 2:
            cnt += 1
            if i[6] == False:
                print(cnt, i[0])
    #6
    print(ascrip)
    #7
    while True:
        choose = input("Choose a movie number: ")
        if choose.isdecimal() == False or int(choose) < 1 or int(choose) > 9:
            print("Wrong number")
            continue
        break
    #8
    if m_list_all[int(choose) - 1][6] == True:
        rewatch = input("You have watched it. Do you like to watch it againg? (y): ")
    #9 
    if m_list_all[int(choose) - 1][6] == False or rewatch == "y":
        print(ascrip)
        for i in range(0, len(m_tag)):
            print(m_tag[i] + ":", m_list_all[int(choose) - 1][i])
        m_list_all[int(choose) - 1][6] = True
            
        print(ascrip)
        like = input("Do you like it? (y): ")
        if like == "y" or like == "Y":
            while True:
                like_num = input("How many likes do you want to add?: ")
                if like_num.isdecimal() != True:
                        continue
                break
            m_list_all[int(choose) - 1][5] += int(like_num)
    #10
    print(ascrip)
    #11
    next = input("Next movie? (y): ")
    if next != "y":
        quit()
    #12
    while True:
        all = int(input("1. All, 2. Not watched: "))
        if all != 1 and all != 2:
            continue
        break