##김밥 만들기

# item0 = '김'
# item1 = '밥'
# item2 = '단무지'
# item3 = '계란'
# item4 = '햄'
# item5 = '시금치'

# print(item0, item1, item2, item3, item4, item5)

###리스트

# items = ['김', '밥', '단무지', '계란', '햄', '시금치']
# print(items)

###리스트 인덱스
friends = ['민수', '철수', '민준', '재현']
# print(friends)
# print(type(friends))

# print(friends[0])
# print(friends[-2])
# print(friends[2:])

# score = [90, 70, 80, 100]
#print(score[1:3])


###리스트 연산
# print(friends + score) #병합
# print(friends *3) #반복

###리스트 함수
##내장 함수
# print(max(score)) #최대값 반환
# print(min(score)) #최소값 반환
# print(len(score)) #리스트의 길이(갯수)

# name = "taein"
# print(type(name))
# name = list(name)
# print(type(name))

# print(sum(score)) #리스트 안에 있는 값의 총 합을 반환

score = [90, 100, 80, 100]

# score.append(50) #리스트 마지막 값에 x값 추가(50 추가)
# print(score) 
# score.insert(2, 70) #리스트의 n번째 위치에 x값추가(2번째 위치에 70추가)
# print(score)
# score.pop() #리스트의 마지막 값 삭제
# print(score)
# score.remove(70) #리스트에서 x값 삭제(70삭제)(동일한 값이 여러개인 경우 맨앞에서 부터 삭제)
# print(score)
# score.extend(friends) #리스트에 다른 리스트 병합
# print(score)

##정보
# print(score.index(80)) #리스트에서 해당 값의 인덱스 반환
# print(score.count(100)) #리스트에서 해당값의 개수 반환


##정렬
# print(score)
# score.reverse() #역순 정렬
# print(score)
# score.sort() #오름차순 정렬(기본)
# print(score)
# score.sort(reverse=True) #내림차순 정렬
# print(score)
