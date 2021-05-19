import random
import copy
k= 10
n =[]
for i in range(k):
	n.append(random.randrange(0,5*k))
n_copy=copy.deepcopy(n)

count = dict.fromkeys(n,0)

print()
print()

print(n)

print()
print()
print(count.items())

for i in range(100):
	random.shuffle(n_copy)
	for i in range(k):
		if n[i] ==n_copy[i]:
			
			count[n[i]]+=1
print()
print()
print(count.items())
chain=""
alf=random.sample('qwertyuiopasdfghjklzxcvbnm',k)
for i in alf:
	chain+=i
print()
print()
print(chain)
q=random.randrange(1,k)
chain_new=chain[0:q]
chain_new+='.'
chain_new+=chain[q:k]
print()
print()
print(chain_new)
print()
print()

num=[0 for i in range(100)]

for i in range(100):
	num[i]=random.randrange(0,20)

count_ite={}

for ind,ite in enumerate(num,0):
		count_ite.setdefault(ite,[]).append(ind)
print(count_ite)
print()
print()
count_ite2={}
p =0
for i in num:
	count_ite2.setdefault(i,[]).append(num.index(i)+p)
	num=num[1:len(num)+1]
	p+=1
	

print(count_ite2)

print()
print()

num_1000 =[]
count_num_1000={}
for i in range(1000):
	num_1000.append(random.randrange(100,999999))
for ind,i in enumerate(num_1000,0):
	# print(str(i), str(i)[::-1])
	if str(i) == str(i)[::-1]:
		count_num_1000.setdefault(i,[]).append(ind)
print(count_num_1000)

sl1=dict.fromkeys(range(10),random.randrange(1,100))
sl2=dict.fromkeys(range(10),random.randrange(1,100))

print()
print()

print(sl1)

print(sl2)

sl1_rev = dict((y,x) for x,y in sl1.items())

sl2_rev = dict((y,x) for x,y in sl2.items())

print(sl1_rev)

print(sl2_rev)