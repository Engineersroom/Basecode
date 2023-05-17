x = input('문자열을 입력하세여')
print(x)

a = input('첫 번째 숫자를 입력하세요: ')
b = input('두 번째 숫자를 입력하세요: ')

print(a + b)  # 입력값 10, 20  출력 값 1020 type으로 확인해보면
# 타입이 str이라 두 문자열을 이어 붙여서 출력한 것에 지나지 않음

a = int(input('첫 번째 숫자를 입력하세요: '))    # int를 사용하여 입력 값을 정수로 변환
b = int(input('두 번째 숫자를 입력하세요: '))    # int를 사용하여 입력 값을 정수로 변환

print(a + b)

a, b = input('문자열 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
 
print(a)
print(b)

a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
 
print(a + b)