# abs
# 절댓값 리턴
abs1 = abs(3)
abs2 = abs(-3)
abs3 = abs(-3.2)
print(abs1, abs2, abs3)

# all
# 반복가능한 데이터를 전달 받아 모두 참이면 Ture 하나라도 거짓이면 false 출력 -> 반복 가능한 데이터란 리스트, 튜플, 문자열, 딕셔너리와 같은 데이터를 의미
all1 = all([1,2,3,4])
all2 = all([1,2,3,0])
all3 = all([])
print(all1, all2, all3)

# any
# 반복가능한 데이터를 전달받아 하나라도 참이 있으면 True 출력 모두 거짓이면 false 출력
any1 = any([1,2,3,4])
any2 = any([1,2,3,0])
any3 = any([0, 0, 0, 1>3])
any4 = any([])
print(any1, any2, any3, any4)

# chr
# 유니코드를 전달받아 문자를 리턴
chr1 = chr(65)
car2 = chr(44032)
print(chr1, car2)

# dir
# 객체가 지닌 변수나 함수를 리턴
dir1 = dir([1,2,3])
print(dir1)
dir2 = dir({'1':'a'})
print(dir2)

# divmod
# a를 b로 나눈 몫과 나머지를 튜플로 리턴
divmod1 = divmod(7,3)
print(divmod1)

# enumerate
# 순서가 있는 데이터(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 객체로 리턴
for i, name in enumerate(['a','b','c']):
    print(i, name)

# eval
# 문자열로 구성된 표현식의 결과 문자열을 리턴
eval1 = eval('1+2')
eval2 = eval("'hi'+'a'")
print(eval1, eval2)

# filter
# 첫번째 인수로 함수를, 두번쨰 인수로 함수에 넣을 반복가능한 데이터를 받아 리턴값이 참인것만을 묶어 리턴.
def filter_def(a) :
    return a > 0
filter1 = filter(filter_def, [1, 2, -1, -2])
print(list(filter1))

# hex
# 정수를 입력받아 16진수 문자열로 변환하여 리턴
hex1 = hex(234)
print(hex1)

# id
# 객체를 받아 객체의 고유 주솟값을 리턴
id_a = 3
id_b = id_a
print(id(id_a))
print(id(id_b))

# input
# 사용자 입력을 받음. 입력 인수로 문자열을 전달하면 문자열이 프롬프트가 된다.
input1 = input()
print(input1)
input2 = input("Enter :")
print(input2)

# int
# 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴한다.
# int(x, radix) 는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴한다.
int1 = int('3')
int2 = int(3.14)
int3 = int('11',2)
int4 = int('1A', 16)
print(int1, int2, int3, int4)

# isinstance
# 첫번째 인수로 객체, 두번쨰 인수로 클래스를 받아 클래스가 객체의 인스턴스 인지 판단하여 True, False 를 리턴한다.
class InstanceClass: pass
a = InstanceClass()
b = 3
instance1 = isinstance(a, InstanceClass)
instance2 = isinstance(b, InstanceClass)
print(instance1, instance2)

# len
# 입력된 요소의 전체개수(길이)를 리턴
len1 = len('python')
len2 = len([1,2,3])
len3 = len((1,2))
print(len1, len2, len3)

# list
# 반복가능한 데이터를 받아 리스트로 만듬
list1 = list('python')
list2 = list((1,2,3))
print(list1, list2)


# map
# map(f, iterable)은 함수f와 반복가능한 데이터를 입력으로 받아 각 데이터를 순차적으로 f 함수에 적용한 결과를 리턴한다.
def two_times (numberList) :
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3])
print(result)
# 이런 형태를 map 함수를 이용해 만든다.

def two_times_map (x) :
    return x*2

map1 = list(map(two_times_map, [1, 2, 3]))
print(map1)


# max
# 인수로 반복가능한 데이터를 받아 최대값을 리턴
max1 = max([1,2,3,4,5])
max2 = max('python')
print(max1, max2)

# oct
# 정수를 8진수 문자열로 리턴
oct1 = oct(34)
oct2 = oct(1234)
print(oct1, oct2)

# open
# open(filename, [mode]) 파일이름과 읽기 방법을 입력 받아 파일 객체를 리턴 파일 읽기를 생략하면 읽기모드로 리턴
# w: 쓰기모드, r: 읽기모드, a: 추가모드, b: 바이너리 모드 -> b는 w,r,a 와 같이 쓰는 속성이다.

# ord
# 유니코드 숫자값을 리턴
ord1 = ord('A')
ord2 = ord('가')
print(ord1, ord2)

# pow
# pow(x,y)는 x 를 y 제곱한 결과를 리턴
pow1 = pow(2, 3)
pow2 = pow(3, 3)
print(pow1, pow2)

# range
# range([start,] stop [,step]) 은 for 문과 함께 자주 사용한다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴한다.
list1 = list(range(5))
print(list1)
list2 = list(range(5, 10))
print(list2)
list3 = list(range(1, 10, 2))
print(list3)
list4 = list(range(1, 10, -1))
print(list4)

# round
# 입력받은 숫자를 입력받은 자릿수까지 반올림하여 리턴 -> 자릿수를 입력하지않으면 정수형으로 반올림
round1 = round(4.6)
round2 = round(4.6111, 2)
print(round1, round2)

# sorted
# 입력데이터를 정렬한뒤 그 결과를 리턴 -> sort와 차이점은 정렬후 리턴을 한다는 차이점이 있음
sorted1 = sorted([3,1,2])
sorted2 = sorted([3,1,2], reverse=True)
sorted3 = sorted(['a', 'c', 'b'])
print(sorted1, sorted2, sorted3)

# str
# 문자열 형태로 객체를 변환하여 리턴한다.
str1 = str(3)
str2 = str([1,2,3])
print(str1, str2)

# tuple
# 반복가능한 데이터를 튜플로 바꾸어 리턴하는 함수이다.
tuple1 = tuple("abc")
tuple2 = tuple([1,2,3])
print(tuple1, tuple2)

# type
# 입력값의 자료형을 리턴
type1 = type('abc')
type2 = type([1,2,3])
type3 = type(open('test', 'w'))
print(type1, type2, type3)

# zip
# 동일한 개수로 이루어진 데이터들을 묶어서 리턴한다
zip1 = list(zip([1,2,3], [4,5,6]))
zip2 = list(zip([1,2,3], [4,5,6], [7,8,9]))
zip3 = list(zip('abc', 'def', 'ghi'))
print(zip1, zip2, zip3)



















































