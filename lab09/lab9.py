import mojmodul 

#zad 1
los = ((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6))
mojmodul.fun1(100000,los)


#zad 2
funkcja= lambda x: -(x*x)+2

mojmodul.fun2(funkcja,-3,3)

#zad3
funkcja2= lambda x: (x*x)+2

mojmodul.fun3(funkcja2,-1,2)