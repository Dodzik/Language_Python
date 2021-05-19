import random
import matplotlib.pyplot as plt

def fun1 (n,los):
	x = random.random()
	y = random.random()
	argumenty=[]
	wartosci=[]
	
	with open('wyniki1.txt','w') as f:
		f.write(str(x) + " "+ str(y)+'\n')
		argumenty.append(x)
		wartosci.append(y)
		for i in range(n):
			chos = random.choices(los,[1,7,7,85])
			chos = chos[0]
			x,y = chos[0]*x+chos[1]*y+chos[2],chos[3]*x+chos[4]*y+chos[5]	
			argumenty.append(x)
			wartosci.append(y)
			f.write(str(x) + " "+ str(y)+'\n')

	plt.plot(argumenty,wartosci,'bo', markersize='0.1' )
	plt.savefig("zad1.png")

import scipy.integrate

def fun2(funkcja,q,p):
	wynik_squad = scipy.integrate.quad(funkcja,q,p)

	with open('wyniki2.txt','w' )as f:
		f.write("właściwy wynik: \n"+str(wynik_squad)+'\n')
		t=0
		step=0.0001
		min= 0
		max= 0
		lso = q
		
		#szukanie najwiekszej wartości i najmniejszej 
		while lso <p:
			if funkcja(lso)>max:
				max = funkcja(lso)
			if funkcja(lso)<min:
				min = funkcja(lso)
			lso = lso + step
		num_iteration =0
		while True:
			x = random.uniform(q,p)
			y = random.uniform(min, max)


			if 0 < y and y <= funkcja(x):
				t = t+1
			if y >= funkcja(x) and y < 0:
				t = t-1
			num_iteration = num_iteration + 1
			
			if wynik_squad[0] - step < abs(max - min)*abs(max - min)*t/num_iteration and abs(max - min)*abs(max - min)*t/num_iteration < wynik_squad[0] + step:
				f.write("wynik z funkcji:\n" + str(abs(max - min)*abs(max - min)*t/num_iteration) +"\nilosc iteracji "+str(num_iteration))
				break

def fun3(funkcja,q,p):
	wynik_squad = scipy.integrate.quad(funkcja,q,p)
	with open('wyniki3.txt','w' )as f:
		f.write("właściwy wynik: \n"+str(wynik_squad)+'\n')
		step=0.0001
		suma=0
		num_iteration =0
		while True:
			x = random.uniform(q,p)
			suma = suma + funkcja(x)
			num_iteration = num_iteration + 1
			#nieskonczonba petla
			break
			if wynik_squad[0] - step < abs(q,p)*suma/num_iteration and abs(q,p)*suma/num_iteration < wynik_squad[0] + step:
				f.write("Wynik z funkcji" + str(abs(q,p)*suma/num_iteration) + "ilosc iteracji"+str(num_iteration))
				break