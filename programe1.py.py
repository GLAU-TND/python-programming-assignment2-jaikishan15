str1 = bin(int(input()))
str2=''
d = []
for i in range(2,len(str1)):
	str2 = str2 + str1[i]
for j in range(0,len(str2)):
	c = 1
	for k in range(j,len(str2)-1):
		if str2[k] is '1':
			if str2[k] is str2[k+1]:
				c = c+1
	d.append(c)
d.sort()
print(d[-1])
		
	
