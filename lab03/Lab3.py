import sys
import copy

uppers=[]
lowers=[]
decimals=[]
notletters=[]

if(len(sys.argv)<2):
	print('należy podać argument wywołania')
else:
	#zad 1
	print('zadanie 1')
	chain=sys.argv[1]
	print(chain)
	print(type(chain))
	for i in chain:
		if i.islower():
			lowers.append(i)
		elif i.isupper():
			uppers.append(i)
		else:
			notletters.append(i)
		if i.isdecimal():
			decimals.append(i)
	#zad 2
	print("zadanie 2 i 3")
	print("uppers")
	print(uppers)
	print("lowers")
	print(lowers)
	print("decimals")
	print(decimals)
	print("notletters")
	print(notletters)

	#lowers_no_dup=list(set(lowers))
	lowers_no_dup=[]
	for i in lowers:
		if i not in lowers_no_dup:
			lowers_no_dup.append(i)
	print('lowers without duplication')
	print(lowers_no_dup)
	

	
	letters_count=[]

	for i in lowers_no_dup:
		count=lowers.count(i)
		
		letters_count.append((i,count))

	print('lowers counting')
	print(letters_count)
	#zad 4
	print('zadanie 4')
	sorted_letters_count=copy.deepcopy(letters_count)
	sorted_letters_count.sort(key = lambda x : x[1],reverse=True)

	print('sorted lowers counting')
	print(sorted_letters_count)
	if len(decimals)>0:

		#zadanie 5
		print('zadanie 5')
		vowels=['a','e','i','o','u','y','A','E','I','O','U','Y']
		a=0
		b=0
		for q in chain:
			
			if q in vowels:
				a+=1
		b=len(lowers)+len(uppers)-a
		print("samogłoski")
		print(a)
		print("spolgloski")
		print(b)

		dec_para=[]
		for i in decimals:
			dec_para.append((i,(int(i)-b)/a))
		print(dec_para)

		#6.
		print('zadanie 6')
		#x_sr
		count=0
		for i in decimals:
			count+=int(i)
		x_sr=count/len(decimals)

		#y_sr
		count=0
		for i in range(len(dec_para)):
			count+=int(dec_para[i][1])
		y_sr=count/len(dec_para)

		#D
		count=0
		for i in decimals:
			count+=(int(i)-x_sr)**2
		D=count

		#a
		count=0
		for i in range(len(dec_para)):
			count+=int(dec_para[i][1])*(int(dec_para[i][0]) - x_sr)
		a=count/D

		#b
		b= y_sr - a * x_sr

		print("współczynnik a")
		print(a)
		print("współczynnik b")
		print(b)
	else:
		print('W podanym ciągu nie ma cyfr nie mozna wykonać działania')