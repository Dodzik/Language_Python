

#zad 1

def fun1(plik , n):
	with open(plik) as f:
		q = f.readlines()
	print(q[:n])
	print(q[-n:])
	print(q[::n])
	print([i.split(' ')[n-1] for i in q])
	print([i[n-1] for i in q]);

fun1("tekst.txt",2)


import glob
import numpy

print("zadanie 2")

ysr=[0 for i in range(50)]
yod=[0 for i in range(50)]
for file in glob.glob("data*"):
	ysr_pom=[0 for i in range(50)]
	yod_pom=[0 for i in range(50)]
	with open(file)as f:
		q = f.readlines()
	for i in range(len(q)):
		
		ysr_pom[i]=(float(q[i]))
		yod_pom[i]=(float(q[i]))
	for i in range(50):
	
		ysr[i]+=ysr_pom[i]/6
		yod[i]+=(yod_pom[i]-ysr[i])/6
	
print(ysr)
print()
print(yod)

wyniki = open("zad2","w")

for i in range(50):
	wyniki.write(str(i)+" "+ str(ysr[i])+ " "+str(yod[i])+"\n")
wyniki.close()



print("zadanie 3")

def fun3():
	file = open("zad3","w")
	file.write('''import matplotlib.pyplot as plt
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')
A to może się przydać do łatwego wczytywania plików (ale dzisiaj można z
tego skorzystać tylko w skrypcie generującym wykresy)
import numpy
x,y=numpy.loadtxt(nazwa, unpack=True)''')
	file.close();
fun3()

print("zadanie 4")
tab={}
for file in glob.glob("20*"):
	count=0;
	with open(file) as f:
		q = f.readlines()
	for i in q:
		line=i.split(' ')
		if(line[0] in (tab.keys())):
			tab[line[0]]+= " "+str(line[1].strip('\n'))
		else:
			tab[line[0]]= str(line[1].strip('\n'))
	for x in tab.keys():
		if(x not in q):
			tab[x]+= " - "
		


		
file = open("zad4","w")
file.write("Nazwisko")
for i in range(21):
	file.write(" "+str(2000+i))
file.write("\n")
for x,y in tab.items():
	file.write(x+" "+ y + '\n')
