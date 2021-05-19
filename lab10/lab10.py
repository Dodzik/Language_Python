
from datetime import date

#zad 1
def fun1(pesel, data, plec):
	print(pesel+ "  "+ data + " "+plec)
	kontrolna = int(pesel[10])
	suma = int(pesel[0]) + 3* int(pesel[1]) + 7 * int(pesel[2]) + 9 * int(pesel[3])+ int(pesel[4]) + 3* int(pesel[5]) + 7 * int(pesel[6]) + 9 * int(pesel[7])+ int(pesel[8]) + 3* int(pesel[9])
	# print(suma)
	suma = 10 - (suma % 10)
	suma = suma % 10
	assert (kontrolna == suma), "zła liczba kontrolna"
	data=data.split(" ")
	# print(data)

	assert( (int(pesel[0])*10 +int(pesel[1]) ) == int(data[2][2])*10 + int(data[2][3])) , "niepoprawne 2 piewsze cyfry peselu"
	num=0
	mies = data[1]
	miesiace = {"styczenia": 1, "lutego": 2, "marca":3, "kwietnia":4, "maja": 5, "czerwiec": 6, "lipca": 7, "sierpienia":8, "wrzesnia": 9, "pazdziernika": 10, "listopada":11, "grudnia":	12}
	num = miesiace.get(mies)
	# print(num)
	wiek = 0
	kry= int(data[2][0])*10 + int(data[2][1])
	wi={19: 0,20: 20,21 : 40,22: 60,18: 80}
	wiek = wi.get(kry)
	
	assert int(pesel[2])*10 + int(pesel[3]) == wiek + num, "niepoprawne 3-4 cyfry peselu"
	
	dzien = int(data[0])
	assert int(pesel[4])*10 + int(pesel[5]) == dzien, "niepoprawne 5-6 cyfry peselu"

	pl =0
	if(plec == "mężczyzna"):
		pl = 1
	
	assert (int(pesel[6])*1000 + int(pesel[7])*100 + int(pesel[8]) *10 + int(pesel[9]))%2 == pl, "niepoprawne 7-10 cyfry peselu"

	print("poprawny pesel")


fun1('02070803628', '8 lipca 1902', "kobieta")
fun1("02270803624", "8 lipca 2002", "kobieta")
fun1("02270812350", "8 lipca 2002", "mężczyzna")
print()
print()
# 02070803628, 8 lipca 1902, kobieta
# 02270803624, 8 lipca 2002, kobieta
# 02270812350, 8 lipca 2002, mężczyzna
# dla lat 1800 - 1899 - 80
# dla lat 1900 - 1999 - 0
# dla lat 2000 - 2099 - 20
# dla lat 2100 - 2199 - 40
# dla lat 2200 - 2299 - 60

# PESEL
# cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
# cyfry 3-4 to dwie cyfry miesiąca urodzenia
# cyfry 5-6 to dwie cyfry dnia urodzenia
# cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
# cyfra 11 suma kontrolna


# 1 3 7 9 1 3 7 9 1 3 

#zad2
def fun2():
	suma =0
	count =0
	bledy =0
	jeszcze_nie=0
	dzis = ["4","5","2021"]
	with open("daty.in") as f:
		q = f.readlines()
		# print(q)
		for i in q:
			
			i=i.split(" ")
			
			if(int(i[0])==29 and int(i[1])==2 and int(i[2])%4!=0 ):
				bledy = bledy+1
				continue

			if(len(i) == 3 and int(i[1]) < 13 and int(i[0]) < 32) :
				if( int(i[1]) > int(dzis[1]) and int(i[2]) >= int(dzis[2]) ):
					jeszcze_nie=1
				else:
					jeszcze_nie=0
				suma =suma + int(dzis[2]) - int(i[2])-jeszcze_nie
				count =count+1
			else:
				bledy = bledy+1
	print("ilosc blednmych wierszy: "+str(bledy))
	return suma/count

print(fun2())


#zad3
def fun3(lista):
	assert len(lista)!=0 , "lsita ma nieprawidłową długosc"
	trojka = 0
	# czworka =0
	for a in lista:
		for b in lista:
			for c in lista:
				if((a*a + b*b) == c*c):
					trojka += 1
	
	#zakomentowane przez długi czas kompilacji

	# for a in lista:
	# 	for b in lista:
	# 		for c in lista:
	# 			for d in lista:
	# 				if((a*a + b*b + c*c) == d*d):
	# 					czworka += 1
	trojka=trojka/2
	# czworka = czworka/9
	print("ilosc trojek " + str(trojka))
	# print(" ilosc czworek: "+str(czworka))



l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
fun3(l)
# l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)

# l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)

# l=(1,2,3,4,5,6,7,8,9)