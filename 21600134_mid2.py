#Handong University has a mission to cultivate 21st-century leaders who change the world’s nations with a Christian spirit. Such leaders require distinctive lifestyles based on honesty and integrity. The Handong Honorary System speaks of how to live a sanctified life that is pleasing to God in all spheres of life. Accordingly, it fosters distinctive leaders who combine academic excellence and Christian character. Through this Honor system, all Handong students, faculty and staff contribute to achieving Handong University’s vision, and are responsible for maintaining and developing this Honor system.  “Do not conform any longer to the pattern of this world but be transformed by the renewing of your mind. Then you will be able to test and approve what God’s will is – his good, pleasing and perfect will.”- Romans 12:2 Handong Honor Code 1. The people of Handong are responsible for all we do, say, and write. 1. The people of Handong are honest and diligent in our academic and social life. 1. The people of Handong respect the personal dignity and rights of all members of the community. 1. The people of Handong help and serve others humbly. 1. The people of Handong are willing to sacrifice ourselves for others. 1. The people of Handong are careful with university resources and respect the property of others.
import random
import datetime
now = datetime.datetime.now()
text = input("Enter text: ")
# print(text)
t = text.split()
up = []
up_al = []
# print(t)
for x in t:
    if x[0].isupper():
        if x not in up:
            up.append(x)
print(up)
        
        

for x in up:
    if x.isalnum():
        up_al.append(x)
print(up_al)
        
up_al.sort()
cnt = 0
for i in range(len(up_al) - 1):
    if up_al[i] in t:
        cnt += 1
        print(up_al[i], cnt)

rand = random.choice(up_al)
print(rand)
end = False
up_al1 = []
last = input("끝말잇기를 할 단어를 입력해 주세요: ")
while True:
    if rand[-1] != last[0]:
        print("컴퓨터가 이겼습니다!", now.strftime('%Y/%m/%d %H:%M:%s'))
        break
