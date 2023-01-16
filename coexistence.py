def print_coexistence(a,b):
	n = max(a,b)
	for i in range(2,n+1):
		if (a%i == b%i):
			print(i,end=" ")
a, b = map(int, input("").split())
print_coexistence(a,b)