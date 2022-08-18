
a = 10
b = 20
###비교연산자
'''
print(a == b) #같다 - false
print(a != b) #다르다 - true
print(a > b)  #크다 - false
print(a < b)  #작다 - true 
print(a >= b) #크거나 같다 - false 
print(a <= b) #작거나 같다 - true
'''
###논리연산자
#and_논리곱 
#or_논리합
#not_부정
'''
print(a < b and a == 10) 
print(a > b and a == 10)
print(a > b and a != 10)
print(a < b or a == 20)
print(a > b or a == 10)
print(a > b or a != 10)
print(not a > b)
print(not a < b)
print(not a == 10)
'''

###포맷팅###
name = '한태인'
age = 14
height = 163.9

## 출력 예시
#print('이름:', name, ', 나이:', age,', 키:', height,)

## 포맷기호
#형식
# % + 서식문자
# %d : 정수
# %f : 실수 
# %s : 문자열
#print('이름: %s, 나이: %d, 키:%.2f ' %(name, age, height)) #자료형에 맞는 순서로 변수를 써줘야 한다 #소수점 둘째자리 까지나오게 하려면 %.2f를 사용한다

## 포맷함수
#print('이름: {}, 나이: {}, 키: {:.2f}'.format(name, age, height)) #소수점 둘째자리까지 나오게 할려면 :.2f를 사용한다
#print('이름: {2:.2f}, 나이: {0}, 키: {1}'.format(name, age, height)) #인덱스 활용

## f-string
#print(f'이름:{name}, 나이:{age}, 키:{height:.2f}') 

###input() : 입력함수
#input() #사용자가 enter키를 누르면 종료 #모든 문자를 문자형으로 인식하기 때문에 숫자일 경우 그에 맞는 자료형 함수를 써줘야 한다
#int() : 정수형 함수
#float() : 실수형 함수
#str() : 문자형 함수

id = input('아이디를 입력하세요:')
pw = int(input('비밀번호를 입력하세요:'))

print(id, type(id))
print(pw, type(pw))