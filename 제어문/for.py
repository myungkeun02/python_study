# for문 기본구조

# for 변수 in 리스트(튜플, 문자열 가능):
#   수행항 문장_1
#   수행항 문장_2
#   수행항 문장_3 ...

# 전형적인 for 문

test_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i in test_list:
    print(i)

# 다양한 활용

a = [(1,2), (3,4), (5,6)]

for (first, last) in a:
    print(first + last)

# 응용

marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d 번 학생은 불합격 입니다." % number)
    else:
        print("%d 번 학생은 합격 입니다." % number)


# continue

marks2 = [90, 25, 67, 45, 80]

number = 0

for mark in marks2:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생은 합격입니다. 축하합니다." % number)

# range

a = range(10)
print(a)

b = range(1, 11)
print(b)

add = 0

for i in range(1, 11):
    add = add + i
    print(add)

marks3 = [90, 25, 67, 45, 80]
for number in range(len(marks3)):
    if marks3[number] >= 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# 구구단

for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print("\n")


# list comprehension
a = [1,2,3,4]

result = []
for num in a:
    result.append(num)
print(result)

result = []
for num in a:
    if num % 2 == 0:
        result.append(num)
print(result)

gugu = [x*y for x in range(2, 10)
        for y in range(1, 10)]
print(gugu)