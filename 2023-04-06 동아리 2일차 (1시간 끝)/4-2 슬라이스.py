jumin = "040130-3156713"

print("성별 :" , jumin[7])#첫번째 0은 0번째 숫자로 침 
print("연:", jumin[0:2])#0부터 2직전까지 (0~1)
print("월:",jumin [2:4])
print("일:",jumin[4:6])

print("생년월일:",jumin[:6])#0부터 시작하는 조건일시 없어도 됨
print("주민번호:",jumin[7:])#7부터 끝까지
print("주민번호(거꾸로):",jumin[-7:])#반대