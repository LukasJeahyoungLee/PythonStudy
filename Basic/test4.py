'''
print('a가 0보다 크면 실행, 작으면 정지')

a=int(input('a:'))

a=10
while a>0:
    print('실행')
    n=n-1

n=int(input('n:'))
while n:
    print(n)
    n=n-1
#(1)1~10까지 숫자 반복하기 
n=1
while n<=10:
    print(n)
    n=n+1


#(2) yes를 입력하면 반복하기

text='yes'

while text=='yes':
    text=input('yes 입력 시 반복')

print("종료")


#(3)e 또는 E가 입력될때까지 반복하기
text=input('e 또는 E 입력 시 종료')

while text!='e'and text!='E':
    text=input('e또는 E 입력 시 종료 ')

print('종료')
'''


