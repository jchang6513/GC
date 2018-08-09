# part1: Multiples of 3 and 5. 

thres = 1000

sum = 0
for i in range(1,thres):
	if i%3 == 0:
		sum += i
	elif i%5 == 0:
		sum += i
		
print('The sum of these multiples is ',sum)		