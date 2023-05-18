print(1, 2, 3, sep=', ')    # sep에 콤마와 공백을 지정

print(4, 5, 6, sep=',')    # sep에 콤마만 지정
print('Hello', 'Python', sep='')    # sep에 빈 문자열을 지정

print(1920, 1080, sep='x')    # sep에 x를 지정


print('1\n2\n3')    # 문자열 안에 \n을 사용하여 줄바꿈
print(1, 2, 3, sep='\n') # 두 경우 출력 결과는 같다 

# 파이썬의 print 는 기본적으로 \n을 추가한다. 이를 하지 않으려면 end 문자열을 지정해줄 수 있다. 
print(1, end='')    # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
print(2, end='')
print(3)

print(1, end=' ')    # end에 공백 한 칸 지정
print(2, end=' ')
print(3) 