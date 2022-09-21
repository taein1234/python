####튜플 (tuple)
# list = [1, 2, 3]
# tuple = (1, 2, 3)
# t1 = (1, 2, 3, 4, 5)
# t2 = ('a', 'b', 'c')

##튜플연산
# print(t1 + t2)
# print(t2 * 3)

##튜플인덱스
# print(t1[2])
# print(t1[1:4])
# print(t2[1:3])
# print(t2[:])

##리스트 vs 튜플
# l1 = [1, 2, 3]
# l2 = l1[:] #l1의 값 전체를 l2에 복사 #l2 = l1 : 링크만 연결 (복사x)
# print(l1)
# print(l2)
# print(l1 == l2) #값이 같은지 여부 확인
# print(l1 is l2) #주소가(링크) 같은지 확인
# l2[1] = 4
# print(l1)
# print(l2)

# t1 = (1, 2, 3)
# t2 = t1[:] #t1의 값 전체를 t2에 복사 #t2 = t1 : 링크만 연결 (복사x)
# print(t1)
# print(t2)
# print(t1 == t2) #값이 같은지 여부 확인
# print(t1 is t2) #주소가(링크) 같은지 확인
# t2 = (4, 5, 6)
# print(t1)
# print(t2)
# print(t1 == t2) 
# print(t1 is t2)


##딕셔너리(dictionary)##
# dic = {'name':'taein', 'age':'14', 'school':'과천중'}
# print(dic, type(dic))
# print(dic['name'])

# ##딕셔너리 추가
# dic['height'] = 164.5
# print(dic)

# ##딕셔너리 수정
# dic['age'] = 15
# print(dic)

# ##딕셔너리 삭제
# del dic['school']
# print(dic)

##미션
fruits = {'apple':500, 'banana':2500, 'mango':2000}
# print(fruits)
# print('망고는 1개당 %d원 입니다.'%fruits['mango'])
# print('망고는 1개당 {}원 입니다.'.format(fruits['mango']))

# fruits['apple'] = 700
# fruits['str'] = 400
# del fruits['banana']
# print(fruits)

###딕셔너리 함수
fruits_list = list(fruits.keys())
print(fruits_list)

print(fruits.keys()) #key들을 묶어서 반환
print(fruits.values()) #value들을 묶어서 반환
print(fruits.items()) #key와 value가 쌍으로 묶여서 반환
print(fruits.get('apple')) #key에 해당하는 value값을 반환

fruits.update({'apple':700, 'orange':1200}) #key에 해당하는 value값을 반환 (수정, 추가, 삭제 기능)
print(fruits)

fruits.clear() #딕셔너리의 모든 item을 삭제(모두 삭제)
print(fruits)
