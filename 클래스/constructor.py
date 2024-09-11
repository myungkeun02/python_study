# 기존 foulCal 에서 보완함
# 만약, class를 변수에 담아 add를 호출한다고 할떄 매개변수에 아무런 값을 전달하지않으면 오류가 발생함. 이를 생성자(constructor)로 해결함 - 초기값 설정

class FourCal:
    # 생성자는 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다 아래처럼 setData를 사용하기보다 생성자를 둠으로 초깃값을 자동 설정하는 부분이 좋다.
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second


a = FourCal(1, 2) # 이렇게 객체를 생성할 때 매개변수를 입력하면 자동으로 __init__ 함수를 불러와 적용한다.
print(a.first)
print(a.second)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())


# class의 상속
# inheritance 란 물려받다 라는 뜻으로 어떤 클래스를 만들때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.
# class 를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
# 이렇게 moreFoulCal class 는 기존 foulCal class의 기능을 모두 사용할 수 있고 동시에 추가된 기능을 사용할 수 있다. (강화!!)
class MoreFourCal(FourCal):
    def pow(self):
        return self.first**self.second

b = MoreFourCal(4, 2)
print(b.first)
print(b.second)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
print(b.pow())

# 매서드 오버라이딩
# c = FourCal(4, 0)
# print(c.div())
# 위 코드에서는 ZeroDivisionError: division by zero 에러 문구가 발생한다 원인은 4를 0으로 나눌수 없기 때문이다.
# 아래처럼 fourCal 을 상속하는 class 를 생성해보자
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0  # 나누는 값이 0일 경우에는 0을 리턴
        else:
            return self.first/self.second

# fourCal class 에 있는 div 메서드를 동일한 이름을 다시 작성했다. 이처럼 상속한 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩 이라고 한다.
# 메서드 오버라이딩을 하면 부모 클래스의 메서드 대신 오버라이딩한 자식 클래스의 메서드가 호출된다.
c = FourCal(4, 0)
print(c.div())

# 클래스 변수

class Family :
    lastName = "김"

# Family 클래스에 선언한 lastname이 클래스 변수이다. 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.
# 클래스 변수는 다음과 같이 사용할 . 있다.

print(Family.lastName)

# 또한 다음과 같이 family 클래스로 만든 객체를 이용해도 클래스 변수를 사용할 수 있다.
a = Family()
b = Family()

print(a.lastName)
print(b.lastName)

# 만약 Family.lastname을 바꾸면 어떻게 될까?
Family.lastName = "박"
print(Family.lastName)
print(a.lastName)
print(b.lastName)
# 이처럼 모든 lastName 의 값이 바뀌게된다. 즉, 클래스 변수는 객체 변수와 달리 클래스로 만든 모든 객체에 공유된다.
a.lastName = "김"
print(a.lastName)
print(b.lastName)