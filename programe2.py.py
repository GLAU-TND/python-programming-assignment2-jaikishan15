str = input().split()
str.sort()
str1 = [str[0]]
while len(str1) != len(str):
	for i in str:
		if i not in str1 and str1[-1][-1]==i[0]:
			str1.append(i)
print(str1)