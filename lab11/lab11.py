#zad1

from random import randint
import copy


class Automat:
	def __init__(self, num, rule, bol=False):
		self.tab = []
		self.it = 0
		self.len = num
		self.rul = ''
		while rule > 0 or len(self.rul) < 8:
			self.rul = str(rule % 2) + self.rul
			rule = rule // 2
			# print(len(self.rul))

		print("kod reguly " + self.rul)
		for i in range(num):
			if bol == False:
				self.tab.append(0)
			else:
				self.tab.append(randint(0, 1))
		if bol == False:
			self.tab[num // 2] = 1

	def ewol(self):
		self.it += 1
		prev = copy.deepcopy(self.tab)
		# print(prev)
		if (prev[1] == 1):
			self.tab[0] = 1
		if (prev[self.len - 2] == 1):
			self.tab[self.len - 1] = 1
		for i in range(1, self.len - 1):
			# print(i)
			# count = 0
			if prev[i - 1] == 1 and prev[i] == 1 and prev[i + 1] == 1:
				self.tab[i] = int(self.rul[0])

			if prev[i - 1] == 1 and prev[i] == 1 and prev[i + 1] == 0:
				self.tab[i] = int(self.rul[1])

			if prev[i - 1] == 1 and prev[i] == 0 and prev[i + 1] == 1:
				self.tab[i] = int(self.rul[2])

			if prev[i - 1] == 1 and prev[i] == 0 and prev[i + 1] == 0:
				self.tab[i] = int(self.rul[3])

			if prev[i - 1] == 0 and prev[i] == 1 and prev[i + 1] == 1:
				self.tab[i] = int(self.rul[4])

			if prev[i - 1] == 0 and prev[i] == 1 and prev[i + 1] == 0:
				self.tab[i] = int(self.rul[5])

			if prev[i - 1] == 0 and prev[i] == 0 and prev[i + 1] == 1:
				self.tab[i] = int(self.rul[6])

			if prev[i - 1] == 0 and prev[i] == 0 and prev[i + 1] == 0:
				self.tab[i] = int(self.rul[7])
			# 	count +=1
			# if prev[i]:
			# 	count +=1
			# if prev[i+1]:
			# 	count +=1
			# if count ==3 or count ==0:
			# 	self.tab[i] = 0
			# else:
			# 	self.tab[i] = 1
			# print(prev)
			# print(self.tab)
			# print()

	def paint(self):
		chain = ''
		for i in self.tab:
			if i == 0:
				chain += ' '
			else:
				chain += '*'
		return chain

	def __str__(self):
		chain = 't=' + str(self.it) + ": \t"
		for i in self.tab:
			chain += str(i)
		return chain


print("Automat(31,30)")
dummy = Automat(31, 30)
print(dummy)
for i in range(16):
	dummy.ewol()
	print(dummy)

print("Automat(31,90)")
dummy2 = Automat(31, 90)
print(dummy2.paint())
for i in range(16):
	dummy2.ewol()
	print(dummy2.paint())

print("Automat(31,94)")
dummy3 = Automat(31, 94)
print(dummy3.paint())
for i in range(16):
	dummy3.ewol()
	print(dummy3.paint())

print("Automat(31,182)")
dummy4 = Automat(31, 182)
print(dummy4.paint())
for i in range(16):
	dummy4.ewol()
	print(dummy4.paint())

#zad2
from math import sqrt


class Vector:
	def __init__(self, *wsp):
		self.tab = []
		for i in wsp:
			self.tab.append(i)

	def __add__(self, v):
		if type(v) is Vector and len(self.tab) == len(v.tab):
			dummy = Vector()
			for i in range(len(self.tab)):

				dummy.tab.append(self.tab[i] + v.tab[i])
			return dummy

	def __iadd__(self, v):
		if type(v) is Vector and len(self.tab) == len(v.tab):
			for i in range(len(self.tab)):

				self.tab[i] += v.tab[i]
			return self

	def __sub__(self, v):
		if type(v) is Vector and len(self.tab) == len(v.tab):
			dummy = Vector()
			for i in range(len(self.tab)):

				dummy.tab.append(self.tab[i] - v.tab[i])
			return dummy

	def __isub__(self, v):
		if type(v) is Vector and len(self.tab) == len(v.tab):
			for i in range(len(self.tab)):

				self.tab[i] -= v.tab[i]
			return self

	def __mul__(self, v):

		dummy = Vector()
		for i in range(len(self.tab)):
			dummy.tab.append(self.tab[i] * v)
		return dummy

	def __imul__(self, v):

		for i in range(len(self.tab)):
			self.tab[i] *= v
		return self

	def __str__(self):
		chain = 'vector =[ '
		for i in self.tab:
			chain += str(i) + " "
		chain += "]"
		return chain

	def __len__(self):
		return len(self.tab)

	def len(self):
		return sqrt(sum(i**2 for i in self.tab))

	def __eq__(self, v):
		if type(v) is Vector and len(self.tab) == len(v.tab):
			for i in range(len(self.tab)):

				if self.tab[i] != v.tab[i]:
					return False

			return True
		return False

	def __getitem__(self, num):
		if num < len(self.tab):
			return self.tab[num]


d = Vector(2, 3, 4)
q = Vector(1, 1, 1)
print(d)

print(d + q)
d += q
print(d - q)

print(d * 3)

d *= 3
print(d)

print(len(d))
o = Vector(1, 1, 1)

print(q == o)
d -= q
print(q == d)

print(d[2])
