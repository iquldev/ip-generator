import random as r

count = int(input('Enter the number of ip addresses: '))

for i in range(count):
	ip = [r.randint(0, 255),r.randint(0,255),r.randint(0,255),r.randint(0,255)]
	print(f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')
