# 집합 자료형

print(f'{'집합 자료형은 어떻게 만들까?':=^50}')

# 집합 자료형은 다음과 같이 Set 키워드를 이용하여 만든다.
s1 = set([1,2,3])
print(s1)

s2 = set("Hello")
print(s2)

print(f'{'집합 자료형의 특징':=^50}')

# 집합 자료형은 중복을 허용하지않는다. 순서가 없다 (Unordered)
s3 = set([1, 2, 3])
l1 = list(s3)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

print(f'{"교집합, 합집합, 차집합 구하기":=^50}')

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# 교집합 (s1.intersection_update(s2) -> s1의 데이터가 변경됨)
intersection = set1 & set2
print(intersection)

# 합집합 (s1.union_update(s2) -> s1의 데이터가 변경됨)
union = set1 | set2
print(union)

# 차집합 (...)
difference1 = set1 - set2
difference2 = set2 - set1
print(difference1)
print(difference2)

print(f'{"집합 자료형 관련 함수":=^50}')

set_1 = {1,2,3}
print(set_1)
set_1.add(4)
print(set_1)
set_1.update({5,6})
print(set_1)
set_1.remove(6)
print(set_1)

