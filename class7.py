####제어문####
## 조건문 if
# num = int(input("숫자입력: "))

# if num > 5:
#     print("{}은/는 5보다 큽니다.".format(num))
# elif num == 5: 
#     [print(f'{num}은/는 5입니다.')]
# else: #예외처리
#     print(f"{num}은/는 5보다 작습니다.")

##중첩if
# num = int(input("숫자입력: "))

# if num > 5:
#     print("{}은/는 5보다 큽니다.".format(num))
#     if num%2 == 0: #만일짝수라면
#         print("짝수 입니다.")
#     else: #elif num%2 != 0: #elif num%2 == 1 #짝수가 아니라면
#         print("홀수입니다.")
# elif num == 5: 
#     print(f'{num}은/는 5입니다.')
#     print("홀수 입니다.")
# else: #예외처리
#     print(f"{num}은/는 5보다 작습니다.")
#     if num%2 == 0: #만일짝수라면
#         print("짝수 입니다.")
#     elif num%2 != 0: #짝수가 아니라면
#         print("홀수입니다.")
#     else:
#         print("0입니다.")

#######
##논리연산 활용

# num = int(input("숫자입력: "))
# if num > 5 and num%2 == 0: #5보다 크고 짝수라면
#     print(f"{num}은/는 5보다 크고 짝수 입니다.")
# elif num > 5 and num%2 == 1: #5보다 크고 홀수라면
#     print(f"{num}은/는 5보다 크고 홀수입니다.")
# elif num < 5 and num%2 == 0: 
#     print(f"{num}은/는 5보다 작고 짝수입니다.")
# elif num < 5 and num%2 == 1:
#     print(f'{num}은/는 5보다 작고 홀수입니다.')
# else num == 5: 
#     print(f'{num}은/는 5입니다.')
#     print("홀수 입니다.")

#########
###멤버십 연산자 in
# l = [1, 3, 5, 7, 9]
# print(3 in l) #3이 리스트l에 있는지
# print(4 not in l) #3이 리스트l에 없는지

# t = 'Hello World'
# print('h' in t)
# print('World' in t)

# members = ['Tommy', 'Marry', 'taein1234']
# id = input('가입하실 ID를 입력해주세요:')

# if len(id) > 4 and id not in members :
#     print(f'{id}로 가입하였습니다.')
# elif len(id) > 4 and id in members :
#     print('이미 가입되어있는 아이디 입니다.')
# else :
#     print('아이디를 5자 이상으로 입력해주세요')


