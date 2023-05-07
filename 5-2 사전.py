a = {3:"김덕원",100:"김태호"}
#print(a[3])
#print(a[100])

#print(a.get(3))
#print(a.(5))#없는 키는 오류나고 시스템 꺼짐

print(a.get(5))#값이 없,음으로 NONE출력
print(a.get(5,"사용가능"))# 