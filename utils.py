from cmath import sqrt
from gc import garbage
from math import factorial

from scipy import interpolate 
from scipy.integrate import quad



def fact(n):
	i=0
	factoriel = 1
	if n>=0:
		while i<n:
			print(factoriel)
			factoriel *=n-i
			i +=1
			
		return factoriel # si on ne retourne pas la dernière valeur factorielle, elle sera tjrs =1
	else: print('ValueError')
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	pass

def roots(a, b, c):
	
	h= (b*b)-a*4*c
	h2=sqrt(h)
	
	if h>0:
		x1=(-b+h2)/(2*a)
		
		return x1
		
	
	else :
		
		return -b/2*a  
		
	



	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	pass

def integrate(f, l, u):
	y = lambda f: f
	print('y',y)
	i=quad(lambda x: eval(f, {'x':x}), l, u) # intègre n'importe quelle equation f avec variable x dans l'equation
	
	return i
	
	
	eval(f,{"x":1}) 
	eval(f,{"x":1})

	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
