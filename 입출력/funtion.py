# 함수
# 입력에 대한 출력값을 리턴
# 반복되는 부분이 있을 경우 함수를 이용

# 기본구조
def add (input1, input2) :
    return input1 + input2

print(add(1, 2))

# 여기서 함수에 선언할떄 입력되는 input1, input2 는 parameter
# 함수를 호출할떄 입력되는 1, 2 는 arguments 이다.

# 입력값이 없는 함수

def hello () :
    return "Hello Python!"

print(hello())

# 리턴값이 없는 함수

def add2 (param1, param2) :
     print("%d + %d = %d" % (param1, param2, param1 + param2))

add2(1, 2)
print(add2(1, 2)) # 리턴되는 값이 없기에 None 출력

# 입력값과 리턴값이 둘 다 없는 함수

def say ():
    print("Hi?")

say()

# 매개변수를 지정하여 호출하기

def sub (a, b):
    return a - b

result = sub(b = 3, a = 7) # a에 7을 b에 3을 전달 이로써, 순서와 상관없이 매개변수를 전달 할 수 있다.
print(result)

# 입력값의 개수를 알 수 없을때
def add_may(*args) :
    result = 0
    for i in args :
        result += i
    return result

print(add_may(1, 2, 3, 4))

def add_mul(choice, *args) :
    if choice == "add":
        result = 0
        for i in args :
            result += i
    elif choice == "multiply":
        result = 1
        for i in args :
            result *= i
    return result

print(add_mul("multiply", 2, 3))

# 키워드 매개변수
def print_keyword (**kwargs) :
    print(kwargs)

print_keyword(a=1, b=2, c=3)
print_keyword(name = "poo", age = 3)

# 함수의 리턴값은 항상 하나이다
def add_and_mul (a,b) :
    return a * b, a * b

print(add_and_mul(1, 2))

result1, result2 = add_and_mul(1, 2)
print(result1, result2)

# 만약 하나의 함수에 리턴이 두개라도 첫번째로 만나는 리턴을 읽는 순간 함수를 빠져나온다


# 매개변수에 초깃값 미리 설정하기
def say_myself (name, age, man=True) :
    print("나의 이름은 %s 입니다." % name)
    print("나의 나이는 %d 입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("곽철용", 42)
say_myself("정마담", 40, False)

# 만약 위처럼 고정된 파라미터를 설정하고 싶다면, 항상 파라미터들의 맨 뒤쪽에 설정을하는것이 좋다. 모든 로직을 순서대로 읽기때문이다.

# 함수 안에서 선언한 변수의 효력 범위

a = 1
def varTest(a) :
    a = a + 1

varTest(a)
print(a)

# 함수 안에서 입력받는 매개변수는 함수 안에서만 사용하는 변수이기에 기본적으로는 함수 밖에 있는 데이터의 값에 관여를 할 수 없다.
# 하지만 아래와 같은 방법으로 외부의 값을 변경할 수 있다.

# 1. return 이용
a = 1

def varTestReturn (a) :
    a = a + 1
    return a

a = varTestReturn(a)
# 함수를 거친 값이 기존 a 변수에 대입된다.
print(a)

# 2. global 이용
a = 1

def varTestGloval () :
    global a
    a = a + 1
# global a 를 통해 전역 변수를 선언한 것이지만 이는 프로그래밍에 좋지 않은 방법이다. 함수 안의 변수는 함수 안에서만 독립적으로 사용되는것이 절대적으로 좋다.
varTestGloval()
print(a)

# 람다는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다. 보통 함수를 한 줄로 간결하게 만들 떄 사용한다.

# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식

add_lambda = lambda a, b: a + b
result3 = add(3, 4)
print(result)