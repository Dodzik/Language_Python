
import math
#zad1
print("zad1")
class A:

	def __init__ (self , min , max):
		self.min = min;
		self.max = max;
	
	def __iter__(self):
		return self
	
	def __next__(self):
		count = 0
		self.min+=1
		for i in range(2,self.min//2):
			if self.min % i ==0:
				count+=1
		if count == 0:
			return self.min
		
		# self.min+=1
		if self.min > self.max:
			raise StopIteration
		return next(self)


class B:
	def __init__ (self, min , max):
		self.min = min
		self.max = max
	def __iter__(self):
		return C(self.min,self.max)

class C:
	def __init__(self,min,max):
		self.min = min
		self.max = max

	def __next__(self):
		count = 0
		self.min+=1
		for i in range(2,self.min//2):
			if self.min % i ==0:
				count+=1
		if count == 0:
			return self.min
		
		if self.min > self.max:
			raise StopIteration
		return next(self)
	# Gdy nie ma na końcu "return next(self)" potrzebne są ify w forze ponieważ iteracje zwracają "None"

a = A(6,20)


for i in a:
	# if(i):
	print(i)
print()
b = B(6,20)
for i in b:
	# if(i):
	print(i)

#zad2

#Newtona-Raphsona: xn+1=xn-f(xn)/f'(xn) 
# f(x)=sin(x)-(0.5x)^2, x=1.5 i eps=10^(-5) 
print()
print("zad2")
import scipy.misc

f = lambda x : math.sin(x) - (1/2 * x) ** 2
x = 1.5 
eps = 10**(-5)
print(f'dokładność: {eps}')
class NewR:
	def __init__(self,fun,x,eps):
		self.f=fun
		self.x=x
		self.eps=eps
		self.count=0
	def __iter__(self):
		return self
	def __next__(self):
		self.count+=1
		x_prev = self.x
		self.x = x_prev - self.f(x_prev) / scipy.misc.derivative(self.f,x_prev)
		if(abs(self.x - x_prev)) < self.eps:
			raise StopIteration
		return (self.count, self.x)


N = NewR(f,x,eps)

for i in N:
	print(i)



#zad3
#Xn+1 = (aXn + c) mod m, dla m = 2^(31)-1, a = 7^5, c = 0, x0 = 1.
#0.1*n, gdzie n∈[1,10].
#10^5 par liczb z przedziału [0,1)
print()
print("zad3")

import random


m = 2**31 -1 
a = 7**5
c = 0
x0 = 1
num = 10**5

class los:
	def __init__ (self,m,a,c,x0):
		self.m = m
		self.a = a 
		self.c = c
		self.x = x0
	def __iter__(self):
		return self

	def __next__(self):
		x_prev = self.x
		self.x = (a * x_prev + c) % m
		return self.x/self.m

n = 10
tab = [0 for i in range(10)]
tab2 = [0 for i in range(10)]
def inSQ(point , a):
	if point[0] < a and point[1] < a and point[0] > 0 and point[1] > 0 :
		return 1
	return 0

ran = los(m,a,c,x0)
for i in range(num):
	# ran = los(m,a,c,x0)
	point=(next(ran),next(ran))
	# print(point)
	point2=(random.random(),random.random())
	for j in range(1,n+1):
		
		tab[j-1] += inSQ(point,j*0.1)
		tab2[j-1] += inSQ(point2,j*0.1)

for i in range(len(tab)):
	tab[i] = tab[i]/num *100
	tab2[i] = tab2[i] / num * 100

print()
print("Własny generator liczb pseudolosowych:")
print(tab)
print()
print("Generator liczb z języka Python:")
print(tab2)

diff = [0 for i in range(10)]

for i in range (len(tab)):
	diff [i] = abs(tab[i]-tab2[i])

print()
print("Różnica: ")
print(diff)

