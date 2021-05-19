import sys
import random


def fun1(chain):
	a =random.randrange(0,10)
	b =random.randrange(0,10)
	print(a,b)
	num=""
	# for i in chain:
	# 	if( i.isdigit()):
	# 		num+=i
	# x=int(num)
	# print(chain)
	# print(eval(chain))

	zb=[]
	for i in range(10):
	
		p=random.randrange(0,10)
		chain2=chain.maketrans("x","p")
		zb.append((p,eval(chain.translate(chain2))))
	return(zb)

def fun2(*arg):
	first=arg[0]
	print(arg)
	count=0
	values=[]
	for i in first:
		for l in arg:
			if(i in l):
				count+=1 
		# print(count)
		if (count==len(arg)):
			values.append(i)
		count=0
		# print()
	return values

def fun3(tab1,tab2,piv=True):
	values=[]
	if piv:
		for i in range(min(len(tab1),len(tab2))):
			values.append((tab1[i],tab2[i]))
	else :
		for i in range(max(len(tab1),len(tab2))):
			values.append((tab1[i],tab2[i]))
	return values


def fun4(money,nominals=[10,5,2]):
	rest=[]
	for i in nominals:
		# print(i)
		rest.append((i,int(money/i)))
		if money>=i:
			money%=i
	# 	print(money)
	# print()
	# print(money)
	if money==0:
		return rest
	else:
		return "nie można rozmienić"
count2=0
def fun5(search,down,upper,method="r"):
	global count2
	if search>down and search<upper:
		
		count=0;
		q=None
		if method=="r":
			while(q!=search):
				q = random.randrange(down,upper)
				count+=1
			return count

		# print("druga metoda")
		else:
			# print(count2)
			# print(int((down+upper)/2))
			if(search==int((down+upper)/2)):
				# print("znalazłem")
				print(count2)
				return count2
			else:	
				if(search<int((down+upper)/2)):
					count2+=1
					# print(down,int((down+upper)/2))
					fun5(search,down,int((down+upper)/2),"p")
					# count2+=1
				else:
					count2+=1
					# print(int((down+upper)/2),upper)
					fun5(search,int((down+upper)/2),upper,"p")
					# count2+=1
	else:
		return "nie z przedziału"
if(len(sys.argv)<2):
	print('należy podać argument wywołania')
else:
	
	chain=""
	for i in range(1,len(sys.argv)):
		chain+= sys.argv[i]
	print(chain)
	print(fun1(chain))

	print(fun2([1,2,3],[2],[1,2]))
	print(fun3([1,2,3],[2]))

	print(fun4(12))
	print(fun4(1732,[25,16,8,3,1]))

	print(fun5(12,6,17))
	
	print(fun5(12,6,17,"o"))
