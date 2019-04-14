#Question 1
def squa(a):
	return a**2

def show(string):
	print(string)

def params(a,b,c,d=4,e=6):
	return a+b+c+d+e

def div2(a):
	return a/2

def mult4(b):
	return b*4

print(mult4(div2(2)))

def converttofloat(string):
	try:
		float(int(string))
	except:
		print("invalid entry")

converttofloat("HIHIHI")
