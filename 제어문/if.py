# if 문
print(f'{"if문":=^50}')

money = True

if money :
    print("택시를 타고 간다.")
else:
    print("걸어 간다.")

# indentation(들여 쓰기) 필수


# 비교 연산자

x = 3
y = 2

print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)


money = 2000
card = True

if money >= 3000 or card == True:
    print("택시 ㄱ")
else:
    print("걸어 ㄱ")

list1 = [1,2,3]

print(1 in list1)
print(2 in list1)
print(3 in list1)
print(4 in list1)
print(4 not in list1)

# 주머니에 돈이 있으면 택시를 타고가고 없으면 걸어가라.

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# elif

pocket = ['paper', 'cellphone']
card  = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print('걸어가라')
# 이걸 아래처럼 쓸수 있음

if 'money' in pocket:
    print('택시를 타고가라')
elif card:
    print('택시를 타고가라')
else:
    print('걸어가라')

# 조건부 표현식

score = 80

message = "success" if score >= 80 else "failure"

print(message)