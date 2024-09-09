# 파일 생성하기
f = open("새파일.txt", "w")
f.close()
# 동일 디렉토리에 새로운 파일이 생성된다.
# 파일 열기모드 세가지 (r = 읽기모드, w = 쓰기모드, a = 추가모드) -> 쓰기모드를 사용할때 동일 이름의 파일이 있을경우 기존 파일을 삭제하고 생성하며 파일이 없을경우 그냥 생성한다.
# 만약 파일의 경로를 지정하고 싶을 경우 아래처럼 하면 된다.
f1 = open("sample/sample2/새파일2.txt", "w")
f1.close() # 해당 구문은 생략해도 무관하다 단순히 열려있는 파일 객체를 닫아주는 역할이다.

# 쓰기모드에서 내용 쓰기

f3 = open("sample/sample2/text1.txt", "w")
for i in range(1, 11) :
    data = "%d번째 줄입니다.\n" % i
    f3.write(data)
f3.close()

# readLine

f = open("sample/sample2/text1.txt", "r")
line = f.readline()
print(line)
f.close()

f = open("sample/sample2/text1.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#while True:
#    data = input()
#    if not data: break
#    print(data)

# readLines

f = open("sample/sample2/text1.txt", "r")
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()

f = open("sample/sample2/text1.txt", "r")
data = f.read()
print(data)
f.close()

# for 문과 함께 파일 객체 사용

f = open("sample/sample2/text1.txt", "r")
for lines  in f:
    print(lines)
f.close()

# 데이터 추가하기

f = open("sample/sample2/text1.txt", "a")

for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with 문 사용하기
# 매번 open과 close를 사용하지않고 다음처럼 자동으로 동착할수 있다.

with open("sample/sample2/text2.txt", "w") as f:
    f.write("Life is too short, you need python")