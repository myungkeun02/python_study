# 변수
from copy import copy

a = 1
b = "python"
c = [1,2,3]

# a, b, c 를 변수라고 한다.

# 변수_이름 = 변수에_저장할_값
# 파이썬은 자료형의 타입을 직접 지정하지 않는다.


# 파이썬에서 사용하는 변수는 객체를 가리키는 것이라고도 말 할 . 있다.
# 객체란 우리가 지금까지 보아 온 자료형의 데이터와 같은 것을 의미하는 말이다.
# 만약 아래 코드처럼 list1 을 선언하면 리스트 데이터가 자동으로 메모리에 생성되고
# 변수 list1 은 [1,2,3]을 저장한 메모리 주소를 가리키게 된다
# id는 변수가 가리키고 있는 객체의 주소 값을 리턴하는 파이썬의 내장 함수이다.
list1 = [1,2,3]
list1_id = id(list1)
print(list1_id)


# 리스트를 아래와 같이 복사하면 list2 라는 변수에 기존 list1이 가리키는 메모리으 주소가 담기게 된다.
list2 = list1
list2_id = id(list2)
print(list2_id)

# 그로인해 아래와같인 list2 의 데이터를 변경하려고 시도하면 list1의 데이터도 변경된다.
list2[0] = 4
print(list1)
print(list2)

print(f'{"리스트 복사하기":=^50}')
# 1. [:] 이용

li1 = [1,2,3]
li2 = li1[:]
li1[1] = 4
print(li1)
print(li2)

# 2. copy 모듈 이용하기

li3  = [1,2,3]
li4 = copy(li3)

print(li3 is li4)
print(id(li3))
print(id(li4))