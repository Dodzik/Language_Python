from time import time
from sys import version
import random

#zad1
powt=1000
N=10000

#def forStatement():
#	tab=[]
#	for i in range(N):
#		tab.append(i)
#	return tab
#
#def listComprehension():
#	return [i for i in range(N)]
#
#def mapFunction():
#	return map(lambda x:x ,range(N))
#
#def generatorExpression():
#	return (i for i in range(N))

#def forStatement():
#	tab=[]
#	for i in range(N):
#		tab.append(i**2)
#	return tab
#def listComprehension():
#	return [i**2 for i in range(N)]
#def mapFunction():
#	return map(lambda x:x**2 ,range(N))
#def generatorExpression():
#	return (i**2 for i in range(N))

#def forStatement():
#	tab=[]
#	for i in range(N):
#		tab.append(i)
#	q=0
#	for i in tab:
#		q=q+i
#	return q
#
#def listComprehension():
#	tab= [i for i in range(N)]
#	q=0
#	for i in tab:
#		q=q+i
#	return q
#
#def mapFunction():
#	tab= map(lambda x:x ,range(N))
#	q=0
#	for i in tab:
#		q=q+i
#	return q
#
#def generatorExpression():
#	tab= (i for i in range(N))
#	q=0
#	for i in tab:
#		q=q+i
#	return q	

#def forStatement():
#	tab=[]
#	for i in range(N):
#		tab.append(i)
#	return sum(tab)
#
#def listComprehension():
#	tab= [i for i in range(N)]
#	return sum(tab)
#def mapFunction():
#	tab= map(lambda x:x ,range(N))
#	return sum(tab)
#def generatorExpression():
#	tab= (i for i in range(N))
#	return sum(tab)	

#def forStatement():
#	tab=[]
#	for i in range(N):
#		tab.append(i)
#	return tab
#def listComprehension():
#	return [i for i in range(N)]
#def mapFunction():
#	return list(map(lambda x:x ,range(N)))
#def generatorExpression():
#	return list((i for i in range(N)))
#
#def tester(fun):
#	t = time()
#	for i in range(powt):
#		fun()
#	t-=time()
#	return t
#
#print(version)
#test=(forStatement, listComprehension, mapFunction, generatorExpression)
#for testFunction in test:
#    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

####

#[GCC 7.5.0]
#forStatement         => -3.3065946102142334
#listComprehension    => -1.7447032928466797
#mapFunction          => -0.0018432140350341797
#generatorExpression  => -0.0022678375244140625

#######
#i**2
#forStatement         => -11.795621395111084
#listComprehension    => -9.114720344543457
#mapFunction          => -0.0012106895446777344
#generatorExpression  => -0.0013108253479003906

#######
#sumowanie forem
#forStatement         => -5.324860572814941
#listComprehension    => -3.0568926334381104
#mapFunction          => -0.00128936767578125
#generatorExpression  => -4.1363914012908936

########
#sumowanie funckją sum()
#forStatement         => -4.095221281051636
#listComprehension    => -1.8850619792938232
#mapFunction          => -3.721184492111206
#generatorExpression  => -1.9019041061401367

####
#konwersja map i generatora  list(map(lambda x:x ,range(N))) list((i for i in range(N)))
#forStatement         => -2.9679503440856934
#listComprehension    => -1.5871281623840332
#mapFunction          => -2.922259569168091
#generatorExpression  => -2.19962215423584


#zad3
print("zad 3")
proby=50000
pkt=[(random.uniform(-1,1)**2 + random.uniform(-1,1)**2)**(1/2) for i in range(proby)]
pi= len(list(filter(lambda x:x<=1,pkt)))*4/proby
print("pi = ",pi)

#zad4
print("zad 4")
macierz=[[1,2,3],[4,5,6],[1,8,9]]
macierz2=[[4,5,6],[1,8,9],[1,2,3]]

for i in macierz:
	print(i)
print()
print("najwieksze z wierszy")
print(list(map(max,macierz)))
print("Najwieksze z kolumn")
print(list((map(max,zip(*macierz)))))
#print(list((map(max,zip(macierz[0],macierz[1],macierz[2])))))
print("suma dwuch macierzy")
print([list(map(sum,zip(*i)))for i in zip(macierz,macierz2)])

#zad5
print("zad 5")

x=[1,2,34,6,46,4545,74]
y=[12,423,5,64,6,6,6]
def fun5(x,y):
	l=len(x)