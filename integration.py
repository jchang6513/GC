# part 2. integration

def anonymous(x):    
#	return 10 
	return x**2 + 1
def integrate(fun, start, end):  
	step = 0.1
	intercept = start    
	area = 0   
	while intercept < end:
		intercept += step
		area += fun(intercept)*step
#		print(intercept,area)
	return area
	
print(integrate(anonymous, 0, 10))
