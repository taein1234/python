# school = input("학교:")
# grade = int(input("학년:"))
# s_class = int(input("반:"))
# num = int(input("번호:"))
### 출력 : "과천중학교 1학년 8반 27번"
# print("%s %d학년 %d반 %d번" %(school, grade, s_class, num))  #포맷기호
# print("{} {}학년 {}반 {}번".format(school, grade, s_class, num))  #포맷함수
# print(f"{school} {grade}학년 {s_class}반 {num}번")  #f-string

###문자열 연산
# fruit1 = "딸기"
# fruit2 = "귤"

# print(fruit1 + fruit2) #병합
# #print(fruit1 - fruit2) #연산불가 
# print(fruit1 * 2) #반복
# #print(fruit1 / 2) #연산불가

# s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYC"
# s2 = "abcdefghijklmnopqrstuvwxyz"

# firstname = s1[-7] + s2[0] + s2[4] + s2[8] + s2[13]
# print(firstname)

###인덱스 활용
# text = "hello, world!" 
# print(text[0:5]) #hello출력
# print(text[-6:-1]) #world출력
# print(text[:]) #전체출력
# print(text[:4]) #처음부터 4번째 인덱스 전까지 출력
# print(text[-2:]) #-2번째 인덱스 부터 끝까지 출력

###이스케이프 코드

# \n 문자열 안에서 줄 바꿈 
# \T 문자열 사이에 탭 간격
# \\ 문자 \를 그대로 표현
# \' 문자 '를 그대로 표현
# \" 문자 "를 그대로 표현
text1 = "\t\"There is no one \nwho loves pain itself, \nwho seeks after it \nand wants to have it, \nsimply because it is pain...\""
# print(text1)

# print(text1.count("h")) #특정 문자의 갯수 반환
# print(text1.upper()) #문자열을 대문자로 변환
# print(text1.lower()) #문자열을 소문자로 변환
# print(text1.replace("who", "it")) #문자열에서 a를 b로 치환

# print(text1.isalpha()) #문자로만 구성되었는지 확인
# print(text1.isdigit()) #숫자로만 구성되었는지 확인

#print(text1.split()) #띄어쓰기를 기준으로 문장에서 문자 분리
#print(text1.split(",")) #쉼표를 기준으로 

#print(len(text1)) #문장의 길이 반환

