#한 줄 주석

'''
여러줄 주석
1
2
...
'''

"""
여러줄 주석
1
2
...
"""

# print("hello world!")

## 기본연산
# print(33+5)  #덧셈
# print(5-4)   #뺄셈
# print(3*8)   #곱셈
# print(10/3)  #나눗셈
# print(10//3) #나눗셈 몫만
# print(10%3)  #나눗셈 나머지만
# print(10**2) #제곱근

### 자료형
##type() : 어떠한 값의 자료형을 알려주는 함수
# print(type("text")) #모든 문자는 str(string)형
# print(type(2)) #모든 정수는 int(integer)형
# print(type(10/3)) #식을 입력하면 식의 값의 자료형을 알려준다 #모든 실수(소수점을 가진 숫자)는 float형 

###자기소개
###변수 선언
# name = "한태인"
# age = 14
# height = 163.9

# name = "hantaein"
# age += 1 #age = age + 1
# age -= 1 #age = age - 1

# print("제 이름은", name, "입니다.")
# print("과천중학교에 다니고 있고 나이는", age,"살 입니다")
# print("좋아하는 것은 축구 입니다.")
# print("나는 키가", height,"야")

##응용
age = 14
age += 1
print(age)

hw = 8
hw -= 3
print(hw)

balance = 1000
balance *= 2
print(balance)

num = 10
print(num == 10)