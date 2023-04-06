Python="Python is amazing"
print(Python.lower())#lower= 모든 문자를 소문자로 바꿈
print(Python.upper())#upper= 모든 문자를 대문자로 바꿈
print(Python[0].isupper())#0번째 글자가 대문자인지 확인 isupper= 몇번째 문자가 대문자인지 확인
print(len(Python))#len= Python 변수의 글자 수를 확인
print(Python.replace("Python", "java"))#replace= 변수 안의 글자를 바꿈 replace("바뀔 글자", ("바꿀 글자"))

index= Python.index("n")#index= 변수 안의 특정글자의 위치를 확인 
print(index)
index=Python.index("n", index+1)#n의 다음부터 다른 n을 찾음
print(index)

print(Python.find("java"))#find는 index와 다른점은 찾으려는 문자가 없다면-1로 표시
print(Python.find("n"))
print(Python.index("java"))#index는 오류가 남 

print(Python.count("n"))#count= 특정 문자가 몇번 나오는지 알려줌

