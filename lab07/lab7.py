import random
import math

#1
#def Fibgen(n):
#    a, b = 0 ,1
#    for i in range(n +1):
#        yield a
#        a , b =b , a +b

def Fibgen():
	a, b = 0 ,1
	while True :
	    yield a
	    a , b =b , a +b

def filterlist(tab ,par):
    if par:
        for i in tab:
            if i % 2==0:
                yield i
    else:
        for i in tab:
            if i % 2:
                yield i

def mniejsze(tab,limit):
	for i in tab:
		if i<limit:
			yield i
		else:
			return


#print(list(Fibgen(12)))
# print(list(Fibgen()))
#tab =[1 ,23 ,2 ,346 ,546 ,45 ,645 ,74 ,745 ,6 ,456 ,456 ,45]
#print("Testy: ")
#print(list(filterlist(tab ,True)))
#print(list(filterlist(tab ,False)))
#print(list(mniejsze(tab,100)))
print()
print("Suma parzystych mniejszych od 100")
print(sum(mniejsze(filterlist(Fibgen(),True),100)))
print()
print("Suma nieparzystych mniejszych od 100")
print(sum(mniejsze(filterlist(Fibgen(),False),100)))

#2
print("my range")
def my_range(a,b=None,c=None):
	x=0
	if b==None and c==None:
		while a>x:
			yield x
			x+=1

	elif c == None:
		if a>b:
			x=a
			while x>b:
				yield x
				x-=1
		else:
			x=a
			while x<b:
				yield x
				x+=1
	else:
		if a<b and c>0:
			x=a
			while b>x:
				yield x
				x+=c
		else :
			if a>b and c<0:
				x=a
				while x>b:
					yield x
					x+=c



print("my_range(10) ",list(my_range(10)))
print("my_range(10,1) ",list(my_range(10,1)))
print("my_range(-5,0) ",list(my_range(-5,0)))
print("my_range(1,10,1) ",list(my_range(1,10,1)))
print("my_range(10,1,-2) ",list(my_range(10,1,-2)))
print("my_range(1,2,0.1) ",list(my_range(1,2,0.1)))


print("testowanie range:")
for i in range(1,10,-1):
	print(i)
print()
#3
print("Trójkąt pascala")
def pascal(n):
	
	def newline(line):
		prev=0
		for i in line:
			yield prev + i
			prev=i
		yield 1
	prevline=[1]
	yield prevline
	for i in range(n):
		prevline = list(newline(prevline))
		yield prevline

q=7
for i in pascal(q):
	print(" "*(q-len(i)),i,"    suma w wierszu",sum(i))

print()
#4

print("przybliżenie sinusa")
def my_sin(x,n):
 	count=0
 	for i in range(0,n):
 		count+=(((-1)**i)/math.factorial((1+2*i))) * x**(1+2*i)
 		yield count

#def my_sin(x):
#	count=0
#	i=0

	# while math.sin(x)-count>0.1:
#	while True:
#		i+=1
#		count +=(((-1)**i)/math.factorial((1+2*i))) * x**(1+2*i)
		
		#yield count
		# if(abs(math.sin(x)-count)<10):
		# 	print("ilość potrzebnych prób ",i)
		# 	break

print(list(my_sin(math.pi/2,10)))
# print(list(my_sin(math.pi/2)))
print("normalna wartość sinusa")
print(math.sin(math.pi/2))
#5
print()
N=40
def genlos(N):
	for i in range(N):
		yield random.randint(0,1)

def howmanyzeros(chain):
	count=0
	for i in chain:
		if i:
			yield count
			count=0
		else:
			count+=1
	
print("przykładowy ciag zer i jedynek",list(genlos(N)))
list_of_zeros = list(howmanyzeros(genlos(N)))

print("srednia odległość miedzy jedynkami: ",sum(list_of_zeros)/len(list_of_zeros))