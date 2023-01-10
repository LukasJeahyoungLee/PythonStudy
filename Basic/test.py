t=int(input('첫번째 숫자 입력하세요(00 입력시 종료):'))
a=input('연산자를 입력하세요( +, -, *, /) :')
k=int(input('두번째 숫자를 입력하세요:'))

result = 0

if a == '+':
    result = t+k
elif a =='-':
    result = t-k
elif a == '*':
    result = t*k
elif a == '/':
    result = t/k
else :
    print('연산자를 잘 못 입력하였습니다.')

print('결과: ',t,a,k,'=',result)