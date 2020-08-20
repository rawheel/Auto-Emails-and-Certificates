import time 
import threading

def check(a):
	a1 = int(round(100/a,2))
	for i in range(1,a+1):
		a2=a1*i
		print(a2,i)
			
check(50)
