a = input().split()
b = ''
n = len(a)
for i in range(0,n):
	for j in range(0,n-i-1):
		if a[i][0] < a[i+1][0]:
			temp = a[i]
			a[i] = a[i+1]
			a[i+1] = temp
		elif a[i][0] == a[i+1][0]:
			if len(a[i]) >= 2:
				if a[i][1] == a[i+1][1]:
					temp = a[i]
					a[i] = a[i+1]
					a[i+1] = temp
for k in a:
	b = b + k
print(b)