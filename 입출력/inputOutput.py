# 사용자 입출력

# input 입력
a = input()
print(a)

# 프롬프트를 띄워 사용자 입력받기
number = input("숫자를 입력하세요: ")
print(number)

# 모든 입력은 문자열로 취급한다.

# print 출력
a = 123
print(a)

b = "Python"
print(b)

c = ["you", "need", b, 3]
print(c)

print("Life", "is", "too", "short")
print("Life"+ "is"+ "too"+"short")
# 위 아래 출력값이 같으나 , 는 띄워쓰기로 인식한다.

# end
# 한줄로 결과값 출력하기
for i in range(10) :
    print(i, end=" ")
    # end 를 이용해 끝 문자를 지정해준다. 기본적으론 \n <- 줄바꿈 기호 이다.