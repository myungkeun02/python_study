# while 문의 구조

#while 조건문:
#    수행할_문장1
#    수행할_문장2
#    수행할_문장3

# while 조건문은 조건문이 참인 동안 while 문 안에 속한 문장들이 반복 수행된다.

# 열 번 찍어 안 넘어가는 나무 없다.

treeHit = 0

while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무는 넘어갑니다.")


prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
    Enter number:"""

number = 0

while number != 4:
    print(prompt)
    number = int(input())


# break 활용

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다.")
        break


coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# continue 활용

a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


# 무한 루프
while True:
    print(1)
    print(2)
    print(3)

# while 문의 조건이 항상 참이므로 무한 루프 발생