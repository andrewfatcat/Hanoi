def move(n, x, y, z, s):
	if x[1]==n:
		s=s+1
		x.remove(n)
		y.insert(1,n)
		if x[0]=="a":
			if y[0]=="b": print(str(x[1:])+str(y[1:])+str(z[1:]))
			else: print(str(x[1:])+str(z[1:])+str(y[1:]))
		elif x[0]=="b":
			if y[0]=="a": print(str(y[1:])+str(x[1:])+str(z[1:]))
			else: print(str(z[1:])+str(x[1:])+str(y[1:]))
		else:
			if y[0]=="a": print(str(y[1:])+str(z[1:])+str(x[1:]))
			else: print(str(z[1:])+str(y[1:])+str(x[1:]))
	else:
		s=move(n-1, x, z, y, s)
		s=move(n, x, y, z, s)
		s=move(n-1, z, y, x, s)
	return s

def main():
	n=int(input("Enter the number of discs: "))
	a, b, c=[], [], []
	a.append("a")
	b.append("b")
	c.append("c")
	for i in range(n): a.append(i+1)
	print(str(a[1:])+str(b[1:])+str(c[1:]))
	steps=move(n, a, c, b, 0)
	print("Total steps= {0}".format(steps))

main()